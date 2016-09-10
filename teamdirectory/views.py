from django.shortcuts import render
from .models import Person


# Create your views here.
def team_directory(request):
    context = {"person": Person.objects.all()}
    return render(request=request, template_name="team.html", context=context)

