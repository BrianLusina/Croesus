from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request=request, template_name='index.html')
