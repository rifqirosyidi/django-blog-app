from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def post_create(request):
    return HttpResponse('Create')


def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request, 'index.html', context)
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
