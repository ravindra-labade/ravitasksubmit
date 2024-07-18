from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm



def create_post(request):
    template_name = 'app1/add.html'
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def show_post(request):
    posts = Post.objects.all()
    template_name = 'app1/show.html'
    context = {'posts': posts}
    return render(request, template_name, context)


def update_post(request, pk):
    template_name = 'app1/add.html'
    obj = Post.objects.get(id=pk)
    form = PostForm(instance=obj)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def delete_post(request,pk):
    obj = Post.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, template_name='app1/delete.html')


