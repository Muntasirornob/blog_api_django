from django.urls import path,include
from. import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('api/',views.blogapi,name='api'),
    path('api/<int:pk>/',views.blogdetailapi,name='api_detail'),
    path('api/post/',views.blogpostapi,name='api_post'),
    path('api/update/<int:pk>/',views.blogpostupdateapi,name='api_update'),
    path('api/delete/<int:pk>/',views.blogdeleteapi,name='api_delete'),
    path('users/',views.profilesapi,name='users'),
    path('api/register',views.register,name='register'),
    path('api/login',obtain_auth_token,name='login')
 
]