from django.shortcuts import render
from blog.models import Post

def get_index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


