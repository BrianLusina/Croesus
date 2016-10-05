from django.shortcuts import render


def home(request):
    """
    Entry point into the app
    :param request that will be handle by the url
    :return: renders the home page
    """
    return render(request=request, template_name='index.html')
