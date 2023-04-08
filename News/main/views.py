from django.shortcuts import render
from .models import Category, Post, TopPost, Comment
from django.views import View
from django.shortcuts import get_object_or_404, redirect

def index(request):
    cat_business = Category.objects.get(slug='bizness')
    cat_technology = Category.objects.get(slug='texnologiya')
    cats = Category.objects.all()
    print(cat_technology)
    print(cat_business)
    posts = Post.objects.all()
    post_business = Post.objects.all().filter(category=cat_business)
    post_technology = Post.objects.all().filter(category=cat_technology)

    topposts = TopPost.objects.all()
    return render(request, "main/index.html", {"cats": cats, "posts": posts,"topposts": topposts, "post_business": post_business, 'post_technology': post_technology})


def categories(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    # category = get_object_or_404(Category, slug=cat_slug)
    topposts = TopPost.objects.all()
    return render(request, "main/category.html", {"posts": posts, "cats": cats, "topposts": topposts})


class CategoryDetail(View):
    @staticmethod
    def get(request, cat_slug):
        cats = Category.objects.all()
        category = get_object_or_404(Category, slug=cat_slug)
        posts = Post.objects.filter(category=category)

        return render(request, "main/category.html",  {"posts": posts, "cats": cats})


class BlogSingle(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post)
        topposts = TopPost.objects.all()
        cats = Category.objects.all()
        return render(request, "main/single.html", {"topposts": topposts, "post": post, "comments": comments, "cats": cats})


    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Comment.objects.create(name=name, email=email, text=comment, post=post)

        return redirect('single', slug)
        # print(request.POST)
    
def contact(request):
    topposts = TopPost.objects.all()
    cats = Category.objects.all()
    return render(request, "main/contact.html", {"topposts": topposts, "cats": cats})
