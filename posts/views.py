from django.shortcuts import render
from django.http import HttpResponse


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

    context = {
            "title": "My User List"
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
