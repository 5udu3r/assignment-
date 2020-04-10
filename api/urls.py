from django.conf.urls import url
from django.urls import path

from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

     # url(r'^$', schema_view),


     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

     # News List
     path('news', views.normal_list, name='news'),

     # url(r'^auth/verify_code_from_cellphone/$', views.verify_code, name='verify_code'),
     # url(r'^auth/send_code_to_cellphone/$', views.send_code, name='send_code'),

]
