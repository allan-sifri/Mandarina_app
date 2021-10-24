from django.shortcuts import render

from .calendar_API import *

def calendario(request):
    return render(request,
     'index.html',
		 {}
		 )

def demo(request):
    results = create_event()
    context = {"results": results}
    return render(request, 'index.html', context)


	