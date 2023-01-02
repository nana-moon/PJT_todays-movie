from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from movies.models import Movie, Comment


class FakeUserSerializer(serializers.ModelSerializer):
    
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
    
    class CommentListSerializer(serializers.ModelSerializer):
        
        class MovieSimpleSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('id', 'title','poster_path',)
                
        movie = MovieSimpleSerializer(read_only=True)
                
        class Meta:
            model = Comment
            fields = '__all__'

    like_movies = MovieListSerializer(many=True, read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)
    like_comments = CommentListSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()        
        fields = '__all__'
        
        
class UserSerializer(FakeUserSerializer):
    # followings = FakeUserSerializer(many=True, read_only=True)
    # followers = FakeUserSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'

class CustomRegisterSerializer(RegisterSerializer):

    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=6)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', '')
        data['gender'] = self.validated_data.get('gender', '')

        return 