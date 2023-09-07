from django.shortcuts import render
from .models import Blog

# Create your views here.


def indexView(request):
    # SELECT * FROM blog
    # queryset
    list_blogs = Blog.objects.all()
    context = {
        # keys           values
        'list_blogs': list_blogs
    }
    print(context)

    return render(request, 'blog/index.html', context)

def contactView(request):
    return render(request, 'blog/contact.html')

def aboutView(request):
    return render(request, 'blog/about.html')