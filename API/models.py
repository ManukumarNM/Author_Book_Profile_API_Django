from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    useremail = models.EmailField()

    def __str__(self):
        return self.username

class Author(models.Model):
    authorname = models.CharField(max_length=250)
    authoremail = models.EmailField()
    authormobile = models.IntegerField()
    authoraffliation = models.CharField(max_length=250)

    def __str__(self):
        return self.authorname

class Book(models.Model):
    bookname = models.CharField(max_length=250)
    bookuser = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bookauthor = models.ManyToManyField(Author)
    publisher = models.CharField(max_length=250)
    published_year = models.DateField()
    isbn_number = models.CharField(max_length=250)

    # The __str__ method just tells django what to print when it need to print out an instance of Book model  
    def __str__(self):
        return self.bookname
