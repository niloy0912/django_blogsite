from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    blog = Blog.objects.all()
    content = [b.content for b in blog]
    
    context = {"blog" : blog}
    #print(context)
    return render(request, "core/index.html", context)