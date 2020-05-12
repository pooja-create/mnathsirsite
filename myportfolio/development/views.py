from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from development.models import development,categorytable

# Create your views here.
def alldev(request):
    if request.method == "POST":
        message = request.POST.get('dropdown')
        if message=="ALL":
            developments=development.objects
            search=categorytable.objects
            return render(request,'development/alldev.html',{'dev':developments,'search':search,})
        else:
            search=categorytable.objects
            developments=development.objects.filter(category_id=message)        
            return render(request,'development/alldev.html',{'dev':developments,'search':search,})
        
    else:    
    
        developments=development.objects
        search=categorytable.objects
        return render(request,'development/alldev.html',{'dev':developments,'search':search,})
def detail(request,development_id):
    development_detail=get_object_or_404(development,pk=development_id)
    return(render(request,'development/detail.html',{'dev_d':development_detail}))
