from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('profile/',views.profile,name='profile'),
    path('profile/logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('profile/create_room/',views.create_room,name='create_room'),
    path('profile/QAF/',views.qaf,name='QAF'),
    path('profile/QAF/q/',views.post_q,name='q'),
    path('profile/QAF/domain/',views.qaf,name='domain'),
    path('profile/QAF/q/<str:id>/',views.view_q,name='q_specific'),
    path('profile/QAF/q/<str:id>/post_answer/',views.post_a,name='post_a'),
    path('profile/room/',views.rooms,name='search'),
    path('profile/room/<str:name>/',views.room,name='room'),
    path('profile/room/<str:name>/post_message/',views.post_message,name='post_message'),
    path('profile/room/<str:name>/follow/',views.follow,name='follow'),
    path('profile/room/<str:name>/unfollow/',views.unfollow,name='unfollow'),
    path('profile/search/room/<str:name>/follow/',views.follow,name='follow'),
    path('profile/search/room/<str:name>/unfollow/',views.unfollow,name='unfollow'),
    path('profile/search/room/<str:name>/',views.room,name='room'),
]