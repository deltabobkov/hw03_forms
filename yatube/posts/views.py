from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from constants import POSTS_PER_PAGE

from .models import Group, Post, User
from .forms import PostForm


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group)
    paginator = Paginator(post_list, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "group": group,
        "page_obj": page_obj,
    }
    return render(request, "posts/group_list.html", context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"posts": posts, "page_obj": page_obj, "author": author}
    return render(request, "posts/profile.html", context)


def post_detail(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    author_posts = Post.objects.select_related("author").filter(
        author=posts.author
    )
    posts_count = author_posts.count()
    context = {
        "posts": posts,
        "posts_count": posts_count,
    }
    return render(request, "posts/post_detail.html", context)


@login_required
def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            group = form.cleaned_data["group"]
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect("posts:profile", posts.author)
        return render(request, "posts/create_post.html", {"form": form})
    form = PostForm()
    return render(request, "posts/create_post.html", {"form": form})


@login_required
def post_edit(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    is_edit = True
    if posts.author != request.user:
        return redirect("posts:post_detail", post_id)
    if request.method != "POST":
        form = PostForm(instance=posts)
    else:
        form = PostForm(instance=posts, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:post_detail", post_id)
    return render(
        request,
        "posts/create_post.html",
        {"form": form, "is_edit": is_edit, "posts": posts},
    )
