from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    unorderedPosts = Post.objects.filter(published_date__lte = timezone.now())
    posts = unorderedPosts.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'posts': posts})
