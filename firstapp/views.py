from django.shortcuts import render
from . forms import Person_Form

# Create your views here.
def welcome(request):
    return render(request, "firstapp/demo.html")

def Login_form(request):
    form = Person_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form=Person_Form()
    context={'form':form}
    return render(request, "firstapp/demo1.html", context)

"""    # if request.method == 'POST':
    form = Person_Form(request.POST)
    if form.is_valid():
        form.save()
        context= {'form':form}
        return redirect(request, display, context)
    else:
        form = Person_Form()
        context={'form':form}
        return render(request, "firstapp/demo1.html", context)

def display(request):
    return render(request, "firstapp/demo2.html") """