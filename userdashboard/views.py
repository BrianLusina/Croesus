from django.shortcuts import render


def dashboard(request):
    render(request=request, template_name='userdashboard.html')
