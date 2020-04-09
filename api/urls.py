from django.conf.urls import url
from django.urls import path

from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

     # url(r'^$', schema_view),

     # auth
     url(r'^auth/verify_code/$', views.verify_code, name='verify_code'),
     url(r'^auth/send_code/$', views.send_code, name='send_code'),

     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

     # News List
     path('news', views.news, name='news'),
     path('newst', views.normal_list, name='news'),
     path('news/<str:category>/<str:country>/<int:limit>/', views.news, name='news_filter'),
     path('news/search/<str:keyword>/', views.news_custom_search, name='search_the_right_way'),

]