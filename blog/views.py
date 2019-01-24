from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def posts_list(request):
    n = ['MyName','YourName']
    return  render(request, 'blog/index.html', context={'names': n})