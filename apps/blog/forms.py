from django import forms
from django.contrib.auth.models import User
from material import Layout, Row

from apps.blog.models import Post, UserProfile


class CommentForm(forms.Form):
	comment_field = forms.CharField()

	def clean_comment_field(self):
		a = self.cleaned_data['comment_field']
		# if a == 'aaa':
		# 	raise forms.ValidationError('hehe')
		# else:
		# 	a = 'qwe'
		return a


class PostForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = Post
		fields = ('title', 'content', 'picture')

	# def __init__(self, *args, **kwargs):
	# 	islogin = kwargs.pop("user")
	# 	super().__init__(*args, **kwargs)

	# 	self.fields["user"] = forms.ChoiceField(choices=islogin)


class UserForm(forms.ModelForm):
	class Meta():
		model = User
		fields = ('username', 'email')


class UserProfileForm(forms.ModelForm):
	layout = Layout(
				Row('gender', 'birthday'),
				'signature', 'portrait')

	class Meta():
		model = UserProfile
		fields = ('gender', 'birthday', 'signature', 'portrait')