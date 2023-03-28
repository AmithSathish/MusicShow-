from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request,"index.html")
def page2(request):
    return render(request,"ticket.html")
