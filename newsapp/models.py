from django.db import models
#This page is for database coding.
# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 100)
	roll_no = models.PositiveIntegerField()
	mobile_no = models.CharField(max_length = 20)
	email = models.EmailField()
	image = models.ImageField(upload_to = 'students')
	program = models.CharField(max_length = 100)
	cv = models.FileField(upload_to ='cv')
	about = models.TextField()

	def __str__(self):
		return self.name+"("+str(self.roll_no)+")"


class Teacher(models.Model):
	name = models.CharField(max_length = 100)
	mobile_no = models.CharField(max_length = 20)
	department = models.CharField(max_length = 50)
	subject = models.CharField(max_length = 50)
	about = models.TextField()


class Category(models.Model):
	title = models.CharField(max_length = 50)
	image = models.ImageField(upload_to = 'category')

	def __str__(self):
		return self.title

class News(models.Model):
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = "news")
	# category = models.OneToOneField(Category, on_delete = models.CASCADE)
	# category = models.ForeignKey(Category, on_delete = models.CASCADE)
	category = models.ManyToManyField(Category)

	detail = models.TextField()
	author = models.CharField(max_length = 100)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

class Album(models.Model):
	title = models.CharField(max_length = 50)
	date = models.DateTimeField(auto_now_add = True)
	description = models.TextField()

	def __str__(self):
		return self.title

class Photo(models.Model):
	album = models.ForeignKey(Album,on_delete = models.CASCADE)
	image = models.ImageField(upload_to ="photo")
	caption = models.TextField(null = True, blank = True)

	def __str__(self):
		return self.album.title




