from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {'listings': page_listings}
    return render(request, 'listings/listings.html', context)

def listing(request,listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')