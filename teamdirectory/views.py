from django.shortcuts import render
from .models import Person
from .forms import PersonForm


# Create your views here.
def team_directory(request):
    context = {"person": Person.objects.all()}
    return render(request=request, template_name="team.html", context=context)


# takes in a request and a slug field which will enable a display like this brian-lusina-ombito
def member_detail(request, slug):
    person = Person.objects.get(slug=slug)
    context = {"person": person}
    return render(request=request, template_name="member_detail.html", context=context)


def member_edit(request, slug):
    form = PersonForm
    context = {"form": form}
    return render(request=request, template_name='member_edit.html', context=context)
