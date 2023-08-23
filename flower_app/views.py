from django.shortcuts import render

def index(request):
    context = {
        'is_index_page': True
    }
    return render(request, 'index.html', context)

def catalog_api(request):
    return render(request, 'catalog.html')

def card(request):
    return render(request, 'card.html')