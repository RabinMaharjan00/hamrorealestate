from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from  .models import Land

# Create your views here.
def index(request):
    lands = Land.objects.order_by('-list_date').filter(is_published = True)
    paginator = Paginator(lands, 6)
    page = request.GET.get('page')
    land_listings = paginator.get_page(page)
    context = {'land_listings': land_listings} 
    return render(request,'lands/lands.html', context)

def land(request, land_id):
    land = get_object_or_404(Land, pk=land_id)
    context = {'land': land}
    return render(request, 'lands/land.html', context)