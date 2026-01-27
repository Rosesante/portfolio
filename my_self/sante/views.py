from django.shortcuts import render
from .models import Portfolio, Education, Experience, ContactMessage, Project
from .forms import ContactForm

# Create your views here.

#Home page
def home(request):
    info = Portfolio.objects.first() #get my data
    return render(request, "sante/home.html", {"info": info})


#Contact page
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "sante/contact_success.html")
    else:
        form = ContactForm()

    return render(request, "sante/contact_success.html",)


#About page
def about(request):
    info = Portfolio.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    return render(request, "sante/about.html", {
        "info": info,
        "education": education,
        "experience": experience
    })


#Projects page
def projects(request):
    projects = Project.objects.all()
    return render(request, "sante/projects.html", {'projects': projects}) 