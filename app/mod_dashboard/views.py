from django.shortcuts import render


def dashboard(request):
    return render(request=request, template_name='mod_dashboard.html')