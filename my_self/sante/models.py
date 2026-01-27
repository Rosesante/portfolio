from django.db import models

# Create your models here.

#Portfolio model
class Portfolio(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.TextField()
    skills = models.TextField(help_text="HTML and CSS, Python, Django, React.")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    
    def __str__(self):
        return self.full_name

#Education model    
class Education(models.Model):
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.school}"

#Experience model        
class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_year = models.CharField(max_length=4, blank=True)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.position} - {self.company}"

#Contact model      
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default="17/11/2025")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
#Project model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(
        max_length=255,
        help_text="HTML&CSS, Python, Django, React"
    )
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
         