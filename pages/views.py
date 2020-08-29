from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import state_choices
from realtors.models import Realtor
from .models import About

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        }
    return render(request, 'pages/index.html', context)

def about(request):
    about = About.objects.all()
    realtors = Realtor.objects.order_by('-hire_date')
    context = {'realtors': realtors,
                'about': about
                }
    return render(request, 'pages/about.html', context)


def agent(request):
    realtors = Realtor.objects.order_by('-hire_date')
    context = {'realtors': realtors}
    return render(request, 'pages/agents.html', context)
