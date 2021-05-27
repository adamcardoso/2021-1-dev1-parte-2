from django.shortcuts import render

# Create your views here.
def home(request):
    #talvez tenha que trocar para 'base.html'
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)