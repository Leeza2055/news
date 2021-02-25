from django import forms
from .models import *


class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['title','image','category','detail','author']

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['title','image']

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = "__all__"


		