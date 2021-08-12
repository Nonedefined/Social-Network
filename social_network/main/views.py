from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def home(request):
    users = Account.objects.all()
    context = {"users": users, "title": "Main"}
    return render(request, "main/main.html", context)


def view_user(request, user_id):
    try:
        if request.user.is_authenticated:
            user = Account.objects.get(pk=user_id)
            posts = Post.objects.filter(user=user)

            if request.method == "POST" and "post_form" in request.POST:
                post_form = PostForm(request.POST, request.FILES)
                if post_form.is_valid():
                    text = post_form.cleaned_data['text']
                    photo = post_form.cleaned_data['photo']
                    post = Post.objects.create(text=text, user=user, photo=photo)
                    return redirect(post)

            elif request.method == "POST" and "edit_form" in request.POST:
                edit_form = UserEditForm(request.POST, request.FILES)
                if edit_form.is_valid():
                    for i in edit_form.cleaned_data:
                        if i == "first_name":
                            user.first_name = edit_form.cleaned_data[i]

                        elif i == "last_name":
                            user.last_name = edit_form.cleaned_data[i]

                        elif i == "mobile":
                            user.mobile = edit_form.cleaned_data[i]

                        elif i == "address":
                            user.address = edit_form.cleaned_data[i]

                        elif i == "bio":
                            user.bio = edit_form.cleaned_data[i]

                        elif edit_form.cleaned_data[i] and i == "photo":
                            user.photo = edit_form.cleaned_data[i]

                        user.save()
                    messages.success(request, "Edited")
                    return redirect(user)

            else:
                post_form = PostForm()
                edit_form = UserEditForm(initial={'first_name': user.first_name, 'last_name': user.last_name,
                                             'mobile': user.mobile, 'address': user.address, 'bio': user.bio})

            context = {"user": user, "post_form": post_form, "edit_form": edit_form, "posts": posts, "title": user.username}

            return render(request, "main/view_user.html", context)
        else:
            return redirect("login")
    except:
        return render(request, "main/page_not_found.html")


def view_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        user = request.user
        comments = PostComment.objects.filter(post=post)
        likes_amount = len(PostLike.objects.filter(post=post, is_liked=True))
        try:
            is_liked = PostLike.objects.get(post=post, user=user).is_liked
        except:
            is_liked = False
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['text']
                PostComment.objects.create(text=text, user=user, post=post)
                return redirect(post)
        else:
            form = CommentForm()

        context = {"post": post, "form": form, "comments": comments, "likes_amount": likes_amount,
                   "is_liked": is_liked, "title": f"{user.username}-post"}

        return render(request, "main/view_post.html", context)
    except Exception as e:
        return render(request, "main/page_not_found.html")


def delete_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        if request.user.pk == post.user.pk:
            post.delete()
            messages.success(request, "Post was deleted")
    except:
        pass
    return redirect(request.user)


def like_post(request, post_id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=post_id)
        user = request.user
        if len(PostLike.objects.filter(post=post, user=user)) > 0:
            post_like = PostLike.objects.get(post=post, user=user)
            post_like.is_liked = not post_like.is_liked
            post_like.save()
        else:
            post_like = PostLike.objects.create(post=post, user=user, is_liked=True)
        return redirect(post)
    else:
        return redirect("login")



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successful registration")
            return redirect(user)
        else:
            messages.error(request, "Registry error")
    else:
        form = UserRegisterForm()

    return render(request, "main/register.html", {"form": form, "title": "Registration"})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(user)
    else:
        form = UserLoginForm()
    return render(request, "main/login.html", {"form": form, "title": "Authorization"})


def user_logout(request):
    logout(request)
    return redirect("login")

