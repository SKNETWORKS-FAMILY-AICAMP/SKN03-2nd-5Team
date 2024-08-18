# show_hotplace/views.py

from django.shortcuts import render, get_object_or_404
from .models import Festival
import os 
from django.conf import settings
from django.utils import timezone

def main_view(request):
    today = timezone.now().date()
    future_objects = Festival.objects.filter(start_date__gt=today).order_by('start_date')
    
    up_coming = _preprocess_future(future_objects)
    unique_region_names = Festival.objects.values('region_name').distinct()
    

    unique_region_names = Festival.objects.values('region_name').distinct()
    
    if request.method == "GET":
        region = request.GET.get('region', [None])
        if type(region) == str:
            region =region.strip()
        
        title = request.GET.get('title', [None])
        if type(title) == str:
            title =title.strip()

        results = _search_data(region,title)
        up_coming = _preprocess_future(results)
        
        
        
    context = {
        "future_objects" : up_coming,

        "unique_region_names" : unique_region_names,
        'filtered_festival': results
    }
    

    return render(request, 'main.html', context)
    

def click_address(request, title):    
    if title:
        result = get_object_or_404(Festival, festival_name=title)
        image_path = _check_img(title)
        

    return render(request, 'result.html', {
        'festival': result,
        'image_path': image_path
    })

def _search_data(region,title):
    if region and title:
            results = Festival.objects.filter(region_name=region,festival_name=title)
    elif region:
        results = Festival.objects.filter(region_name=region)
    elif title:
        results = Festival.objects.filter(festival_name=title)
    else:
        results = Festival.objects.all()    
    
    return results.order_by('festival_name')

def _check_img(title):
    image_path = f'img/poster/{title}.jpg'
    full_image_path = os.path.join(settings.STATIC_PATH, image_path)

    if not os.path.exists(full_image_path):
        image_path = 'img/poster/no_img.png'
    return image_path
    
def _preprocess_future(future_objects):
    today = timezone.now().date()
    future_objects = future_objects.filter(start_date__gt=today).order_by('start_date')
    if len(future_objects) > 4:
        future_objects = future_objects[:4]
    model_img = list()
    for future in future_objects:
        model_img.append({"model":future,"img_path":_check_img(future.festival_name)})
    
    return model_img
