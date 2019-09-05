from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def post_create(request):
    return HttpResponse('Create')


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


def post_update(request):
    return HttpResponse('Update')


def post_delete(request):
    return HttpResponse('Delete')
