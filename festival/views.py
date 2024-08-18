# show_hotplace/views.py

from django.shortcuts import render, get_object_or_404
from .models import Festival

def main_view(request):
    unique_region_names = Festival.objects.values('region_name').distinct()
    if request.method == "GET":
        region = request.GET.get('region', [None])
        if type(region) == str:
            region =region.strip()
        
        title = request.GET.get('title', [None])
        if type(title) == str:
            title =title.strip()
        
        if region and title:
            results = Festival.objects.filter(region_name=region,festival_name=title)
        elif region:
            results = Festival.objects.filter(region_name=region)
        elif title:
            results = Festival.objects.filter(festival_name=title)
        else:
            results = Festival.objects.all()
        
        
    context = {
        "unique_region_names" : unique_region_names,
        'filtered_festival': results
    }
    

    return render(request, 'main.html', context)
    

def click_address(request, title):
    print(f"title {title}")
    if title:
        result = get_object_or_404(Festival, festival_name=title)
    print(result)
    

    return render(request, 'result.html', {
        'festival': result
    })