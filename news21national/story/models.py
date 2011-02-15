from datetime import datetime
from django.db import models
import django.contrib.auth.models as auth
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField
from tagging.models import Tag
from geotagging.models import Geotag
from news21national.newsroom.models import Newsroom
from news21national.story.constants import STATUS_CHOICES, STATUS_DEFAULT, STAGE_DEFAULT, STAGE_CHOICES
import news21national
from django.contrib.contenttypes.models import ContentType
from news21national.coderepo.models import CodeRepo
from news21national.core.models import Profile
from django.conf import settings

class Project(models.Model):
	name = models.CharField(max_length=150,verbose_name="Name Of Project")
	description = models.TextField(verbose_name="Description")
	started_at = models.DateTimeField(verbose_name="Started On")
	thumbnail = models.ImageField(_('image'), upload_to='uploads/photos/%Y/%m/%d', max_length=255)
	screenshot = models.ImageField(_('image'), upload_to='uploads/photos/%Y/%m/%d', max_length=255,null=True)
	created_by = models.ForeignKey(auth.User, related_name="project_created_by")
	created_at = models.DateTimeField(editable=True)
	updated_by = models.ForeignKey(auth.User, related_name="project_updated_by")
	updated_at = models.DateTimeField(editable=False)
	
	def __unicode__(self):
		return unicode(self.name)

	def __str__(self):
		return self.name

	def admin_image(self):
	  return '<img src="%s"/>' % self.thumbnail.url
	admin_image.allow_tags = True
	
	def admin_screenshot(self):
		if self.screenshot == None:
			return '<img src="%stemplates/%s/images/placeholder.png"/>' % (settings.MEDIA_URL,settings.SITE_STYLE)
		return '<img src="%s"/>' % self.screenshot.url
	admin_screenshot.allow_tags = True
	
	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Project, self).save()


class MetaStory(models.Model):
	newsrooms = models.ManyToManyField(Newsroom, related_name="metastory_newsrooms")
	headline = models.CharField(max_length=200,help_text="<a class='helptip'>Example</a>")
	sub_headline = models.CharField(max_length=200,null=True,blank=True)
	slug = models.SlugField(unique=True,help_text="<a class='helptip'>What's this? Shorten it!</a>")
	summary = models.TextField(verbose_name="Summary/Project in Brief",help_text="<a class='helptip'>Example</a>")
	process = models.TextField(verbose_name="About the Reporting Process",help_text="<a class='helptip'>Example</a>",null=True,blank=True)
	interest = models.TextField(help_text="<a class='helptip'>Example</a>")
	original_url = models.URLField(verify_exists=False,verbose_name="Final Package URL",null=True,blank=True)
	is_active = models.BooleanField(default=True)
	status = models.CharField(max_length=50, choices = STATUS_CHOICES, default=STATUS_DEFAULT,)
	stage = models.CharField(max_length=50, choices = STAGE_CHOICES, default=STAGE_DEFAULT,null=True,blank=True,)
	primary_image = models.IntegerField(null=True,blank=True,)
	secondary_image = models.IntegerField(null=True,blank=True,)
	created_by = models.ForeignKey(auth.User, related_name="metastory_created_by")
	created_at = models.DateTimeField(editable=True)
	updated_by = models.ForeignKey(auth.User, related_name="metastory_updated_by")
	updated_at = models.DateTimeField(editable=False)
	project = models.ForeignKey(Project, null=True,blank=True)
	tags = TagField()

	def __unicode__(self):
		return unicode(self.headline)

	def __str__(self):
		return self.headline

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(MetaStory, self).save()

	def _set_tags(self, tags):
		Tag.objects.update_tags(self, tags)

	def _get_tags(self):
		return Tag.objects.get_for_object(self)

	def get_members(self):
		return auth.User.objects.filter(newsroom_members__in=self.newsrooms.values_list('id',flat=True)).distinct()
	
	def get_primary_thumb(self):
		if self.primary_image != None:
			image = news21national.multimedia.models.Media.children.get(id=self.primary_image,_child_name="photo",status="Approved")
			if image.img_url != None:
				return image.img_url
		return ''
	primary_thumb = property(get_primary_thumb)
	
	def get_secondary_thumb(self):
		if self.secondary_image != None:
			image = news21national.multimedia.models.Media.children.get(id=self.secondary_image,_child_name="photo",status="Approved")
			if image.img_url != None:
				return image.img_url
		return ''
	secondary_thumb = property(get_secondary_thumb)
	
	def get_metastory_newsrooms(self):
		ns = self.newsrooms.values_list('short_name',flat=True).order_by('short_name')
		s = []
		for n in ns:
			s.append(n)
		return ''.join(s)
	metastory_newsrooms = property(get_metastory_newsrooms)
	
	def _get_geotags(self):
		gtags = []
		stories = Story.objects.filter(metastory__id=self.id)
		for s in stories:
			assets = news21national.multimedia.models.Media.children.filter(story=s)
			for asset in assets:
				gtag = Geotag.objects.get_for_object(asset)
				if gtag is not None:
					gtags.append({'asset':asset.get_child_name,'geotag':gtag})
		return gtags


class Story(models.Model):
	metastory = models.ForeignKey(MetaStory)
	headline = models.CharField(max_length=200,verbose_name="Story Info",help_text="<a class='helptip'>Headline</a>")
	slug = models.SlugField(unique=True,verbose_name="Story Slug",help_text="<a class='helptip'>What's this? Shorten it!</a>")
	summary = models.TextField(verbose_name="Story Summary",help_text="<a class='helptip'>Example</a>")
	process = models.TextField(verbose_name="About the Reporting Process",help_text="<a class='helptip'>Example</a>",null=True,blank=True)
	sort = models.IntegerField(default=1)
	status = models.CharField(max_length=50, choices = STATUS_CHOICES, default=STATUS_DEFAULT,)
	stage = models.CharField(max_length=50, choices = STAGE_CHOICES, default=STAGE_DEFAULT,null=True,blank=True,)
	original_url = models.URLField(verify_exists=False,verbose_name="Original Story URL",null=True,blank=True)
	authors = models.ManyToManyField(auth.User, related_name="story_authors")
	primary_image = models.IntegerField(null=True,blank=True)
	secondary_image = models.IntegerField(null=True,blank=True)
	created_by = models.ForeignKey(auth.User, related_name="story_created_by")
	created_at = models.DateTimeField(editable=True)
	updated_by = models.ForeignKey(auth.User, related_name="story_updated_by")
	updated_at = models.DateTimeField(editable=False)
	tags = TagField()


	def __unicode__(self):
		return unicode(self.headline)

	def __str__(self):
		return self.headline

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Story, self).save()

	def _set_tags(self, tags):
		Tag.objects.update_tags(self, tags)

	def _get_tags(self):
		return Tag.objects.get_for_object(self)

	def get_placements(self):
		return news21national.partner.models.StoryPlacements.objects.filter(story=self)

	def get_repos(self):
		return CodeRepo.objects.get_for_object(self)
	repos = property(get_repos)

	def get_authors(self):
		return Profile.objects.filter(user__in=self.authors.values_list('id',flat=True)).distinct().order_by('last_name')

	def _get_geotags(self):
		gtags = []
		assets = news21national.multimedia.models.Media.children.filter(story=self)
		for asset in assets:
			gtag = Geotag.objects.get_for_object(asset)
			if gtag is not None:
				gtags.append({'asset':asset.get_child_name,'geotag':gtag})
		return gtags

	def get_newsrooms(self):
		ns = MetaStory.objects.get(pk=self.metastory.id).newsrooms.values_list('short_name',flat=True).order_by('short_name')
		s = []
		for n in ns:
			s.append(n)
		return ''.join(s)
	newsrooms = property(get_newsrooms)

	def get_newsroom_shortcodes(self):
		ns = MetaStory.objects.get(pk=self.metastory.id).newsrooms.values_list('shorter_code',flat=True).order_by('shorter_code')
		s = []
		for n in ns:
			s.append(n)
		return s
	newsroom_shortcodes = property(get_newsroom_shortcodes)

	def get_story_authors(self):
		na = Profile.objects.filter(user__in=self.authors.values_list('id',flat=True)).distinct().order_by('last_name')
		s = []
		for n in na:
			f = n.first_name+' '+n.last_name
			s.append(f)
		return ', '.join(s)
	story_authors = property(get_story_authors)
	
	def get_story_shorturls(self):
		rstories = Story.objects.filter(pk=self.id)
		rewrites = []
		for r in rstories:
			for n in r.newsroom_shortcodes:
				if r.original_url != '':
					rewrites.append({"from":"/"+str(n)+""+str(r.id),"to":str(r.original_url)})
		return rewrites
	story_shorturls = property(get_story_shorturls)
	
	def get_primary_thumb(self):
		if self.primary_image != None:
			image = news21national.multimedia.models.Media.children.get(id=self.primary_image,_child_name="photo",status="Approved")
			if image.img_url != None:
				return image.img_url
		return ''
	primary_thumb = property(get_primary_thumb)
	
	def get_secondary_thumb(self):
		if self.secondary_image != None:
			image = news21national.multimedia.models.Media.children.get(id=self.secondary_image,_child_name="photo",status="Approved")
			if image.img_url != None:
				return image.img_url
		return ''
	secondary_thumb = property(get_secondary_thumb)

class StoryPublishDate(models.Model):
	story = models.ForeignKey(Story)
	title = models.CharField(max_length=200)
	available_at = models.DateTimeField()
	expires_at = models.DateTimeField()
	created_by = models.ForeignKey(auth.User, related_name="storydate_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="storydate_updated_by")
	updated_at = models.DateTimeField(editable=False)

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(StoryPublishDate, self).save()

class StoryGeoTag(models.Model):
	story = models.ForeignKey(Story)
	placement = models.CharField(max_length=200)
	region = models.CharField(max_length=200)
	lat = models.DecimalField(max_digits=10,decimal_places=6)
	lon = models.DecimalField(max_digits=10,decimal_places=6)
	created_by = models.ForeignKey(auth.User, related_name="storygeo_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="storygeo_updated_by")
	updated_at = models.DateTimeField(editable=False)
