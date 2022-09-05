from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib.auth import get_user

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'


def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'add.html', context)
