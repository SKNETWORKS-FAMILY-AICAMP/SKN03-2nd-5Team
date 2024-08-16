from django.shortcuts import render
# Create your views here.
from .models import Festival

def main(req):

    return render (req,"main.html")


# from .models import Festival  # 모델 파일에서 필요한 모델을 가져옵니다

def search_results(req):
    if req.method == "GET":
        title = req.GET.get("search")
        if title:
            results = Festival.objects.filter(title=title)

    context = {
        'results': results
    }

    return render(req, 'main.html', context)

def click_address(req, title):
        if title:
            result = Festival.objects.filter(title=title)

        context = {
        'result':result
        }

        return render(req, 'result.html', context)