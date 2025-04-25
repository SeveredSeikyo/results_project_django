from django.shortcuts import render
from .models import Result

# Create your views here.
def home(request):
    if request.method=='GET':
        return render(request,'index.html')
    if request.method=='POST':
        roll_number=request.POST.get('roll_number')
        try:
            result=Result.objects.get(roll_number=roll_number)
        except Result.DoesNotExist:
            error='Invalid Roll Number'
            context={'error':error}
            return render(request,'index.html',context)
        
        context={'result':result}
        return render(request,'results.html',context)