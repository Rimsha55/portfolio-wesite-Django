from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def blogs(request):
    myposts = Blogpost.objects.all()
    #print(myposts)
    return render(request, 'blog/blogs.html',
                    {'myposts':myposts} )

def blogpost(request, id ):
    post = Blogpost.objects.filter(post_id = id)[0]
    #print(post)
    return render(request, 'blog/blogpost.html',
                 {'post':post} )
#we write id here bcs we wnt to identify the each blogpost seperatly and
# fetch in are  blog page