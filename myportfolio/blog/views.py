from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import blog
# Create your views here.
def allblogs(request):
    blogs=blog.objects.order_by('-pubdate')
    return(render(request,'blog/allblogs.html',{'blog':blogs}))
def detail(request,blog_id):
    blog_detail=get_object_or_404(blog,pk=blog_id)
    return(render(request,'blog/detail.html',{'blog_d':blog_detail}))

    