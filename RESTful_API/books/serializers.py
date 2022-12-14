from rest_framework import serializers

from .models import Books,Post
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Books
        fields=['id','name_book', 'owner', 'description','img']

        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields='__all__'