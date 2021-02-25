from django.urls import path
from .views import *

app_name = "newsapp"
urlpatterns = [
    path("",HomeView.as_view(), name="home"),
    path("contact/",ContactView.as_view(), name="contact"),
    path("about/",AboutView.as_view(), name="about"),
    path("leeza/",ProfileView.as_view(), name="profile"),
    path("nepal/",CountryView.as_view(), name="country"),
    path("news/list/",NewsListView.as_view(), name="newslist"),
    path("student/list/",StudentListView.as_view(), name="studentlist"),
    path("news/<int:pk>/detail/",NewsDetailView.as_view(), name="newsdetail"),
    path("student/<int:pk>/detail/",StudentDetailView.as_view(), name="studentdetail"),
    path("album/list/",AlbumListView.as_view(), name ="albumlist"),
    path("album/<int:pk>/detail/",AlbumDetailView.as_view(), name="albumdetail"),
    path("news/create/",NewsCreateView.as_view(), name="newscreate"),
    path("category/create/",CategoryCreateView.as_view(), name="categorycreate"),
    path("news/<int:pk>/update/",NewsUpdateView.as_view(), name="newsupdate"),
    path("student/create/",StudentCreateView.as_view(), name="studentcreate"),
    path("student/<int:pk>/update",StudentUpdateView.as_view(), name="studentupdate"),
    path("category/<int:pk>/detail/",CategoryDetailView.as_view(), name="categorydetail"),
    path("news/<int:pk>/delete/",NewsDeleteView.as_view(),name="newsdelete"),
    path("student/<int:pk>/delete/",StudentDeleteView.as_view(),name="studentdelete"),
    



]
