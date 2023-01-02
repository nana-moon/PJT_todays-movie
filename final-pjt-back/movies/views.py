import json
import urllib.request

from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Comment, Genre
from .serializers import MovieListSerializer, CommentSerializer, MovieSerializer
from accounts.serializers import FakeUserSerializer

from collections import Counter
import random


# Create your views here.


User = get_user_model()

# 모든 영화 list 반환
@api_view(['GET'])
def all_movie_list(request):
    movies = get_list_or_404(Movie)[:100]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 영화 detail view
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)  
    return Response(serializer.data)


# 영화에 대한 코멘트 저장
@api_view(['POST'])
def comment_save(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 영화 코멘트 삭제
@api_view(['DELETE'])
def comment_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    data = {
        'delete' : f'코멘트 {comment_pk}번이 삭제 되었습니다.',
    }
    return Response(data, status=status.HTTP_204_NO_CONTENT)

# 영화 좋아요
@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    me = request.user
    if me.like_movies.filter(pk=movie_pk).exists():
        me.like_movies.remove(movie)
        serializer = FakeUserSerializer(me)
        return Response(serializer.data)
    else:
        me.like_movies.add(movie)
        serializer = FakeUserSerializer(me)
        return Response(serializer.data)


# 코멘트 좋아요 or 좋아요 취소
@api_view(['POST'])
def comment_like_or_cancel(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    me = request.user

    if me.like_comments.filter(pk=comment_pk).exists():
        me.like_comments.remove(comment)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        me.like_comments.add(comment)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 추천 결과를 좋아요 함에 넣기 but, 프론트 기능 구현 못함
@api_view(['POST'])
def movies_save(request):
    str_like_movies = request.POST.get('like_movies')
    str_like_movies = str_like_movies[1:-1].replace(" ", "").replace(",", "")
    print(str_like_movies)

    for movie_id in str_like_movies:
        movie_id = int(movie_id)
        movie = get_object_or_404(Movie, pk=movie_id)
        me = request.user
        if me.like_movies.filter(pk=movie_id).exists():
            pass
        else:
            me.like_movies.add(movie)
        
    serializer = FakeUserSerializer(me)
    return Response(serializer.data)


# 검색한 영화 정보 반환
@api_view(['GET'])
def search_movies(request, title):
    movies = Movie.objects.filter(title__contains=title) | Movie.objects.filter(original_title__contains=title)

    movies = movies.distinct().order_by('-popularity')
    serializer = MovieListSerializer(movies, many=True)       
    return Response(serializer.data)



# 추천 알고리즘 구현
@api_view(['POST'])
def question(request):

    firstSelected = request.data.get('firstSelected')
    secondSelected = request.data.get('secondSelected')
    thirdSelected = request.data.get('thirdSelected')
    fourthSelected = request.data.get('fourthSelected')
    
    genre_list = []
        
    all_genre = Genre.objects.all()
    
    if firstSelected == "good":
        for genre in all_genre:
            genre_list.append(genre)
    else:
        for genre in all_genre:
            if genre.name not in ['공포', '미스터리', '전쟁', '스릴러']:
                genre_list.append(genre)
                
    if secondSelected == "sunny":
        for genre in all_genre:
            if genre.name in ['액션', '모험', '애니메이션', '음악', '판타지', '드라마', '코미디']:
                genre_list.append(genre)
    elif secondSelected == "cloudy":
        for genre in all_genre:
            if genre.name in ['드라마', 'SF', '범죄', '미스터리' , '가족', '로맨스', '역사', '다큐멘터리','TV 영화']:
                genre_list.append(genre)
    elif secondSelected == "hot":
        for genre in all_genre:
            if genre.name in ['액션', '모험', '범죄', '공포', '스릴러', 'SF', '코미디', '서부', '미스터리']:
                genre_list.append(genre)
    else:
        for genre in all_genre:
            if genre.name in ['음악', '판타지', '애니메이션', '가족', '스릴러','TV 영화', '로맨스', 'SF', '공포']:
                genre_list.append(genre)
                
    if fourthSelected == "couple":
        for genre in all_genre:
            if genre.name == "로맨스":
                genre_list.append(genre)
        
    elif fourthSelected == "family":
        for genre in all_genre:
            if genre.name in ['애니메이션', '가족']:
                genre_list.append(genre)
    
    common_genres = [i[0] for i in Counter(genre_list).most_common()][:5]
    
    
    if thirdSelected == 90:
        # movie_list = Movie.objects.filter(genres__in=common_genres, vote_count__gte=5000, runtime__lte=90).distinct().order_by('-vote_count')
        movie_list = Movie.objects.filter(genres__in=common_genres, vote_count__gte=5000, runtime__lte=90).distinct()

    elif thirdSelected == 120:
        movie_list = Movie.objects.filter(genres__in=common_genres, vote_count__gte=5000, runtime__lte=120).distinct()

    else:
        movie_list = Movie.objects.filter(genres__in=common_genres, vote_count__gte=5000).distinct()
   
    # serializer = MovieSerializer(movie_list, many=True)
    serializer = MovieListSerializer(movie_list, many=True)

    if len(serializer.data) < 12:
        result = serializer.data
    else:
        result = random.sample(serializer.data, 12)
    return Response(result)
