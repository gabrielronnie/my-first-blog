from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    unorderedPosts = Post.objects.filter(published_date__lte = timezone.now())
    posts = unorderedPosts.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
