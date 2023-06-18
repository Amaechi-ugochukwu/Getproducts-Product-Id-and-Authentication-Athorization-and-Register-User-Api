from django.urls import path 
from base.views import users_views as views 

urlpatterns = [
     path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('register/' , views.registerUser , name='register')
]