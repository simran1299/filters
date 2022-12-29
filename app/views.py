from django.shortcuts import render

# Create your views here.

def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'HAi Django AND Python','dt':dt,'c':2}
    return render(request,'filters.html',d)

def userdefinedfilters(request):
    d={'data':'Hi Python HOW R yoU'}
    return render(request,'userdefinedfilters.html',d)