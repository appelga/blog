from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm
from .models import Comment, Post
"""
request = o que entra (o que o navegador envia)
response = o que retornamos para o navegador
"""
# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    return render(
        request, 
        'blog/post_list.html', 
        {'post_list': posts}
    )

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 

    return render(
        request, 
        'blog/post_detail.html', 
        {'post': post}
    )

def about(request):

    return render(
        request, 
        'blog/about.html',
        {}
    )

def add_comment(request, pk):
    post_obj = get_object_or_404(Post, pk=pk) 

    if request.method == 'POST':
        # quando o método da request é post
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_obj
            comment.save()
            return redirect('post_detail', pk=post_obj.pk)
        

    else:
        # quando o método da request é get
        form = CommentForm()

    return render(
        request,
        'blog/comment.html',
        {'form': form,
        'post': post_obj}
    )