from django.shortcuts import render
from .models import Person


# Create your views here.
def team_directory(request):
    context = {"person": Person.objects.all()}
    return render(request=request, template_name="team.html", context=context)


# takes in a request and a slug field which will enable a display like this brian-lusina-ombito
def member_detail(request, slug):
    pass
