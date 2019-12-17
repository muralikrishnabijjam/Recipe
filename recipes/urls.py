from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "recipes"
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
   # path('', views.login_view, name='login'),
   # path('register/', views.register, name='register'),
   # path('index/', views.index, name='index'),
   # path('create_recipes/', views.create_recipes, name='create-recipes'),
   # path('<int:name_id>', views.details, name='details'),
   # path('<int:del_id>/delete/', views.delete_view(), name='delete')
]
