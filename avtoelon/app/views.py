from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Brand, Model, CustomUser, Comment
from .forms import ModelForm, RegisterForm, LoginForm, CommentForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    brands = Brand.objects.all()
    models = Model.objects.all()
    data = {'brands': brands, 'models': models}
    return render(request, 'app/index.html', context=data)


def models_by_brands(request, id):
    brands = Brand.objects.all()
    models = Model.objects.filter(brand_id=id)
    data = {'brands': brands, 'models': models}
    return render(request, 'app/index.html', context=data)


def detail(request, id):
    model = Model.objects.get(id=id)
    model.views += 1
    model.save()
    comments = Comment.objects.filter(model_id=id)
    data = {'model': model,
            'form': CommentForm(),
            'comments': comments}
    return render(request, 'app/detail.html', context=data)


def add(request):
    form = ModelForm(request.POST, request.FILES)
    if form.is_valid():
        model = form.save()
        messages.success(request, f'{model.name}\n retsept muvaffaqiyatli qo\'shildi!')
        return redirect('index')
    form = ModelForm()
    data = {'form': form}
    return render(request, 'app/model_form.html', context=data)


def edit(request, id):
    post = Model.objects.get(pk=id)

    form = ModelForm(data=request.POST or None, instance=post, files=request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'app/model_form.html', {"form": form})


def delete(request, id):
    model = Model.objects.get(pk=id)

    if request.method == 'POST':
        model.delete()
        return redirect('index')

    return render(request, 'app/delete.html', {"model": model})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'{user.username} Saytga xush kelibsiz!')
            return redirect('index')

        if form.errors:
            for error in form.errors.values():
                messages.error(request, f'{error}')

    form = LoginForm()
    data = {
        'form': form,
        'title': 'Login'
    }
    return render(request, 'app/login.html', context=data)


def user_logout(request):
    logout(request)
    messages.warning(request, 'Siz saytdan chiqdingiz!')
    return redirect('user_login')


def user_register(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        messages.success(request,
                         f'{user.username} Registratsiya muvaffaqqiyatli yakunlandi login parol terib saytga kiring!')
        return redirect('user_login')
    form = RegisterForm()
    data = {
        'form': form,
        'title': 'Registratsiya'
    }
    return render(request, 'app/register.html', context=data)


def user_profile(request, username):
    if request.user.username == username or request.user.is_superuser:
        user = User.objects.get(username=username)
        models = Model.objects.filter(autor=user)
        data = {
            'user': user,
            'models': models
        }
        try:
            custom_user = CustomUser.objects.get(user=user)
            data['custom_user'] = custom_user
        except:
            pass
        return render(request, 'app/profile.html', context=data)
    return HttpResponse('Page not found')


def save_comment(request, model_id):
    if request.method == 'POST':
        model = Model.objects.get(pk=model_id)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.model = model
            comment.comentator = request.user
            comment.save()
            messages.success(request, f'Komment qo\'shildi!')
            return redirect('detail', id=model_id)
    return HttpResponse("No comment found")
