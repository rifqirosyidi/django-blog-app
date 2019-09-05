from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # or you can use form.cleaned_data.get('field')
        instance.save()
        return HttpResponseRedirect(f'/posts/{instance.id}/')

    # Capture The Data From the Form (Not Recommend .. add request.POST to PostForm(...) is sugested)
    # if request.method == 'POST':
    #     print(request.POST.get('title'))
    #     print(request.POST.get('content'))

    context = {
        'form': form
    }
    return render(request, 'post_form.html', context)


def post_detail(request, id):
    # this instance will raise an error , we dont want that so, use get_object_or_404
    # instance = Post.objects.get(id=99)

    instance = get_object_or_404(Post, id=id)  # This will return 404 page default. id not found, not an error
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, 'post_detail.html', context)
    # return HttpResponse('Detail')


def post_list(request):
    query_set = Post.objects.all()

    context = {
            "title": "My User List",
            "object_list": query_set
        }

    # if request.user.is_authenticated:
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }

    return render(request, 'index.html', context)
    # return HttpResponse('List')


def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(f'/posts/{instance.id}/')

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, 'post_form.html', context)


def post_delete(request):
    return HttpResponse('Delete')
