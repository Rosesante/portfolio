from django.shortcuts import render
from .models import Portfolio, Education, Experience, ContactMessage, Project
from .forms import ContactForm

# Create your views here.

#Home page
def home(request):
    info = Portfolio.objects.first() #get my data
    skills_list = []
    if info and info.skills:
        skills_list = [s.strip() for s in info.skills.split(",") if s.strip()]
    projects = Project.objects.all()[:3]
    return render(request, "sante/home.html", {
        "info": info,
        "skills_list": skills_list,
        "projects": projects,
    })


#Contact page
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    return render(request, "sante/contact.html", {"form": form})


#About page
def about(request):
    info = Portfolio.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills_list = []
    if info and info.skills:
        skills_list = [s.strip() for s in info.skills.split(",") if s.strip()]
    skill_icon_map = {
        "html": "fa-html5",
        "css": "fa-css3-alt",
        "javascript": "fa-js",
        "python": "fa-python",
        "django": "fa-django",
        "react": "fa-react",
        "bootstrap": "fa-bootstrap",
        "git": "fa-git-alt",
        "github": "fa-github",
    }
    default_progress = 80
    progress_map = {
        "html": 80,
        "css": 80,
        "javascript": 70,
        "js": 70,
        "django": 78,
        "react": 78,
    }
    skills_with_meta = []
    for skill in skills_list:
        key = skill.lower()
        icon = skill_icon_map.get(key, "fa-code")
        progress = progress_map.get(key, default_progress)
        skills_with_meta.append({
            "name": skill,
            "icon": icon,
            "progress": progress,
        })
    return render(request, "sante/about.html", {
        "info": info,
        "education": education,
        "experience": experience,
        "skills_with_meta": skills_with_meta,
    })


#Projects page
def projects(request):
    projects = Project.objects.all()
    info = Portfolio.objects.first()
    return render(request, "sante/projects.html", {
        "projects": projects,
        "info": info,
    }) 
