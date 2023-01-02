from django.urls import path
from . import views

app_name = 'movies'


urlpatterns = [
    # POST
    path('save/', views.movies_save), # 추천 결과를 좋아요 함에 넣기 but, 프론트 기능 구현 못함
    path('question/', views.question), # 설문 결과 기준으로 추천영화 반환
    path('<int:movie_pk>/comments/', views.comment_save), # 영화에 대한 코멘트 저장
    path('<int:movie_pk>/comments/<int:comment_pk>/like/', views.comment_like_or_cancel), # 코멘트 좋아요 or 좋아요 취소                                     
    path('<int:movie_pk>/like/', views.movie_like), # 영화 좋아요

    # GET
    path('', views.all_movie_list), # 모든 영화 list 반환 (로딩 문제로 100개만)
    path('<int:movie_pk>/', views.movie_detail), # 영화 detail view
    path('search/<str:title>/', views.search_movies), # 검색한 영화 정보 반환

    # DELETE
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_delete), # 영화 코멘트 삭제

]