from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from listings.choices import state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {'listings': page_listings}
    return render(request, 'listings/listings.html', context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, 'listings/listing.html', context)

def search(request):
     queryset_list = Listing.objects.order_by('-list_date')

     #KEYWORDS
     if 'keywords' in request.GET:
         keywords = request.GET['keywords']
         if keywords:
             queryset_list = queryset_list.filter(description__icontains=keywords)
             
 #city
     if 'city' in request.GET:
         city = request.GET['city']
         if city:
             queryset_list = queryset_list.filter(city__iexact=city)
             


    # state
     if 'state' in request.GET:
         state = request.GET['state']
         if state:
             queryset_list = queryset_list.filter(state__iexact=state)

     context = {
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET
        }
     return render(request, 'listings/search.html', context)