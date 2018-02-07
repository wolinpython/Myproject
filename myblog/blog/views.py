from django.shortcuts import render
from .models import *
from .forms import CommentForm
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created')
    context = {'blogs': blogs}
    return render(request, 'blog/list.html', context)


def get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog/detail.html', ctx)
