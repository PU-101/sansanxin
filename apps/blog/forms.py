from django import forms


class CommentForm(forms.Form):
	comment_field = forms.CharField()

	def clean_comment_field(self):
		a = self.cleaned_data['comment_field']
		print(a)
		# if a == 'aaa':
		# 	raise forms.ValidationError('hehe')
		# else:
		# 	a = 'qwe'
		return a