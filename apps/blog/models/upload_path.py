import os


def user_directory_path(instance, filename):
	"""
	media/
	"""
	return os.path.join('user_{0}'.format(instance.user.username), filename)


def default_portrait(gender):
	"""
	static/
	"""
	return os.path.join('images', 'default_portrait', '{0}.jpg'.format(gender))