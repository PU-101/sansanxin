def user_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.username, filename)


def default_portrait():
	return 'default/default_portrait.jpg'