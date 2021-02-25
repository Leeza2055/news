from django.views.generic import *
from .models import *
from .forms import *


class HomeView(ListView):
	template_name = "home.html"
	queryset = Category.objects.all()
	#Model = Category
	context_object_name = "myallcategory" 


class ContactView(TemplateView):
	template_name = "contact.html"


class AboutView(TemplateView):
	template_name = "about.html"


class ProfileView(TemplateView):
	template_name = "leeza.html"


class CountryView(TemplateView):
	template_name = "nepal.html"

class NewsListView(ListView):
	template_name = "newslist.html"
	queryset = News.objects.all().order_by("-id")
	context_object_name = "allnews" 

class StudentListView(ListView):
	template_name = "studentlist.html"
	queryset = Student.objects.all().order_by("-id")
	context_object_name = "allstudents"

class NewsDetailView(DetailView):
	template_name = "newsdetail.html"
	model = News
	#queryset = News.objects.all()
	context_object_name = "newsobject"

class StudentDetailView(DetailView):
	template_name = "studentdetail.html"
	model = Student
	context_object_name = "studentobject"

class AlbumListView(ListView):
	template_name = "albumlist.html"
	model = Album
	context_object_name = "allalbums"

class AlbumDetailView(DetailView):
	template_name = "albumdetail.html"
	model = Album
	context_object_name = "albumobject"

class NewsCreateView(CreateView):
	template_name = "newscreate.html"
	form_class = NewsForm
	success_url = "/news/list/"

class CategoryCreateView(CreateView):
	template_name = "categorycreate.html"
	form_class = CategoryForm
	success_url = "/"

class NewsUpdateView(UpdateView):
	template_name = "newscreate.html"
	form_class = NewsForm
	model = News
	success_url = "/news/list/"

class StudentCreateView(CreateView):
	template_name = "studentcreate.html"
	form_class = StudentForm
	model = Student
	success_url = "/student/list/"

class StudentUpdateView(UpdateView):
	template_name = "studentcreate.html"
	form_class = StudentForm
	model = Student
	success_url = "/student/list/"

class CategoryDetailView(DetailView):
	template_name = "categorydetail.html"
	model = Category
	context_object_name = "categoryobject"

class NewsDeleteView(DeleteView):
	template_name = "newsdelete.html"
	model = News
	success_url = "/news/list/"

class StudentDeleteView(DeleteView):
	template_name = "studentdelete.html"
	model = Student
	success_url = "/student/list"






		


# Create your views here.
