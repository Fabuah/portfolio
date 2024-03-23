from django.shortcuts import render

from resume_app.models import Home, About, Profile, Category, Skills, Portfolio

def index (request):
    
    # Home
    home = Home.objects.latest('updated')
    
    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    
    
    # Skills
    categories = Category.objects.all()
    
    # Portfollio
    portfolios = Portfolio.objects.all()
    
    
    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }
    
    
    
    return render(request, 'index.html', context)
# Create your views here.



