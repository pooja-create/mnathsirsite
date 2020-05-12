from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from jobs.models import job,categorytable

# Create your views here.
def home(request):
    
    if request.method == "POST":
        message = request.POST.get('dropdown')
        
        if message=="ALL" :
            
            jobs=job.objects
            search=categorytable.objects
            return render(request,'jobs/home.html',{'jobs':jobs,'search':search,})
        else :
        
            jobs=job.objects.filter(category_id=message)
            search=categorytable.objects
            return render(request,'jobs/home.html',{'jobs':jobs,'search':search,})
    else:   
        jobs=job.objects
        search=categorytable.objects
        return render(request,'jobs/home.html',{'jobs':jobs,'search':search,})

def detail(request,job_id):
    job_detail=get_object_or_404(job,pk=job_id)
    return(render(request,'jobs/detail.html',{'job_d':job_detail}))

