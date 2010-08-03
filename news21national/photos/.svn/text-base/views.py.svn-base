import simplejson as json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.template.defaultfilters import slugify
from photos.forms import PhotoForm, ImageForm
from photos.models import Photo
from stories.models import RelatedContent

def photo_add_edit( request, media_id=None, template='photos/photo_add_edit.html', redirect_to='', context_dict={}, story=None):

    if media_id:
        photo = get_object_or_404(Photo,pk=media_id)
    else:
        photo = None

    if request.method == 'POST':

        # Create edit or add form
        if photo:
            form = PhotoForm(request.POST,request.FILES, instance=photo)
            image_form = ImageForm(
                            request.POST, request.FILES,instance=photo.image)
        else:
            form = PhotoForm(request.POST,request.FILES)
            image_form = ImageForm( request.POST, request.FILES)

        if form.is_valid() and image_form.is_valid():
            photo = form.save(commit=False)
            image = image_form.save(commit=False)
            photo.modified_by = request.user
            photo.slug = slugify(photo.title)
            image.modified_by = request.user
            
            if not media_id:
                photo.created_by = request.user
                image.created_by = request.user

            image.save()
            photo.image = image
            photo.save()

            image_form.save_m2m()
            form.save_m2m()

            if story:
                try:
                    # check if the relation exists, if not create it.
                    RelatedContent.objects.get(story=story, object_id=photo.id)
                except ObjectDoesNotExist:
                    RelatedContent(story=story, object=photo).save()

                if story.sites.count() > 0:
                    photo.sites = story.sites.all()
                    photo.save()

            request.user.message_set.create(
                        message='Your photo was saved.')            
            return HttpResponseRedirect(redirect_to)

    else:
        if photo:
            form = PhotoForm(instance=photo)
            image_form = ImageForm(instance=photo.image)
        else:
            form = PhotoForm()
            image_form = ImageForm()
            
    c = {'object':photo, 'form':form, 'image_form':image_form,}
    context_dict.update(c)

    return render_to_response(
                template,
                context_dict,
                context_instance=RequestContext(request))

def gallery_detail(request, media_id, slug=False, json=False) :
    object = get_object_or_404(Gallery,pk=media_id)
    pass

def photo_detail(request, media_id, slug=False, 
                 template='photos/photo_detail.html', 
                 serializer='json', 
                 context_dict={}):
    
    photo = get_object_or_404(Photo,pk=media_id)

    if request.is_ajax():
        data = json.dumps(photo.get_json_object())
        print data
        return HttpResponse(data, mimetype='application/json')

    context_dict.update({'object':photo,})

    return render_to_response(
                template,
                context_dict,
                context_instance=RequestContext(request))
