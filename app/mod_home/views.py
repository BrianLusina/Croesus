from . import home
import newspaper
from flask import render_template
from app.forms import ContactForm


@home.route("")
def home():
    """
    Entry point into the app
    :param request that will be handle by the url
    :return: renders the home page
    """
    return render_template("home/index.html")


def fetch_news():
    """
    fetch the news and blog posts for the blogs and news section
    :return: a dictionary with the blogs and news items
    """
    investopedia = newspaper.build("http://www.investopedia.com/")

    for categories in investopedia.category_urls():
        print(categories)


def contact(request):
    """
    Handles the contact form, picks data and sends the contact form to server
    :param request: the request handle by this function
    :return:
    """
    if request.method == "POST":
        form = ContactForm(request.POST)

    pass


def team_directory(request):
    context = {"person": Person.objects.all()}
    if request.user.is_authenticated():
        return render(request=request, template_name='team.html', context=context)
    else:
        return redirect(to='/login/google-oauth2')


# takes in a request and a slug field which will enable a display like this brian-lusina-ombito
def member_detail(request, slug):
    person = Person.objects.get(slug=slug)
    context = {"person": person}
    return render(request=request, template_name="member_detail.html", context=context)


def member_edit(request, slug):
    person = Person.objects.get(slug=slug)
    if request.method == "POST":
        # update existing person
        form = PersonForm(data=request.POST, instance=person)
        if form.is_valid():
            form.save(commit=True)
        return redirect(reverse("member_detail", args=[slug, ]))
    else:
        person_dict = model_to_dict(person)
        form = PersonForm(person_dict)
        context = {"form": form}
        return render(request=request, template_name='member_edit.html', context=context)


def verify_email(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        existing_person = Person.objects.filter(email=kwargs.get('details').get('email'))
        if not existing_person:
            return HttpResponse("You don't have access!")
