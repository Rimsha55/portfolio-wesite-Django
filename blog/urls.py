from django.urls import path,include
from .import views

urlpatterns = [
  path('', views.blogs,),
 path("blogpost/<int:id>", views.blogpost, name="Blogpost")

]


