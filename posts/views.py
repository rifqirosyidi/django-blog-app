from urllib.parse import quote_plus
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import Post
from .forms import PostForm


# Create your views here.
def post_create(request):
    # request files when you have image field / files to upload
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # or you can use form.cleaned_data.get('field')
        instance.save()
        messages.success(request, "Successfuly Created")
        return HttpResponseRedirect(f'/posts/{instance.slug}/')

    # Capture The Data From the Form (Not Recommend .. add request.POST to PostForm(...) is sugested)
    # if request.method == 'POST':
    #     print(request.POST.get('title'))
    #     print(request.POST.get('content'))

    context = {
        'form': form
    }
    return render(request, 'post_form.html', context)


def post_detail(request, slug):
    # this instance will raise an error , we dont want that so, use get_object_or_404
    # instance = Post.objects.get(id=99)

    instance = get_object_or_404(Post, slug=slug)  # This will return 404 page default. id not found, not an error
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }
    return render(request, 'post_detail.html', context)
    # return HttpResponse('Detail')


def post_list(request):
    query_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(query_list, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    query_set = paginator.get_page(page)

    context = {
            "title": "My User List",
            "object_list": query_set,
            "page_request_var": page_request_var
        }

    return render(request, 'post_list.html', context)


def post_update(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Updated")
        return HttpResponseRedirect(f'/posts/{instance.slug}/')

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, 'post_form.html', context)


def post_delete(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfuly Deleted")
    return redirect('posts:list')
