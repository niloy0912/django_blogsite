from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    blog = Blog.objects.all()
        
    context = {"title" : blog, "content" : "text"}
    return render(request, "core/index.html", context)