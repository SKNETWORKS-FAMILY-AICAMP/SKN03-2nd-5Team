# Create your views here.
from django.shortcuts import render
from show_hotplace.models import Festival

def detail_view(request, festival_name):
    festival = Festival.objects.get(festival_name=festival_name)
    
    context = {
        'festival': festival
    }
    return render(request, 'show_details/result.html', context)
