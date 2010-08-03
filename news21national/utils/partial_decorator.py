

def partial_template(template):
	"""
	Wrap the result of a function in a `tag` HTML tag.
	"""
	def _dec(func):
		def _new_func(*args, **kwargs):
			return "<%s>%s</%s>" % (template, func(*args, **kwargs), template)
		return _new_func
	return _dec