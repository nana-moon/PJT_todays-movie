from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Movie, Comment, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('pk', 'username')

# 디테일 뷰에서 사용
class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username',)   
    
    class CommentListSerializer(serializers.ModelSerializer):
        
        user = UserSerializer(read_only=True)
        
        class Meta:
            model = Comment
            fields = '__all__'
            
            
    like_users = UserSerializer(many=True, read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)
    
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    liked_count = serializers.IntegerField(source='like_users.count', read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    

    genres = GenreSerializer(many=True, read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'poster_path', 'genres', 'vote_average', 'release_date', 'runtime', 'adult', 'like_users',)


class CommentSerializer(serializers.ModelSerializer):
    
    class SimpleMovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)

    liked_count = serializers.IntegerField(source='like_users.count', read_only=True)
    
    movie = SimpleMovieSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
