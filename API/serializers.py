from rest_framework import serializers 
from .models import Book, Profile, Author 

# HyperlinkedModelSerializer is a layer of abstraction over the default serializer that allows 
# to quickly create a serializer for a model in Django.
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['authorname', 'authoremail', 'authormobile' ,'authoraffliation']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
