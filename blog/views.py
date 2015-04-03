from django.shortcuts import render

from django.http import HttpResponse
from .models import Post,Comment
def index(request):
    context_dict={'user':request.user}
    return render(request,'blog/index.html',context_dict)
# Create your views here.
