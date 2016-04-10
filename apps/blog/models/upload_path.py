import os, random


def user_directory_path(instance, filename):
	"""
	media/
	"""
	return os.path.join('user_{0}'.format(instance.user.username), filename)


def default_portrait(gender):
    """
    static/
    """
    index = random.randint(1, 5)
    return os.path.join('images', 'default_portrait', gender, '{0}.jpg'.format(index))