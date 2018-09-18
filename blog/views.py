from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, Http404
from .models import Post
from .forms import BlogPostForm

def get_posts(request):
    """ Returns published posts within a html page """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})

def post_detail(request, pk):
    """ Returns a single post based on post ID """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})

def create_or_edit_post(request, pk=None):
    """ Allows us to create or edit a blog post """
    if not request.user.is_authenticated():
        raise Http404
    else:    
        post = get_object_or_404(Post, pk=pk) if pk else None
        if request.method == "POST":
            form = BlogPostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save()
                post.user = request.user
                post.save()
                return redirect(post_detail, post.pk)
        else:
            form = BlogPostForm(instance=post)
        return render(request, 'blogpostform.html', {'form': form})