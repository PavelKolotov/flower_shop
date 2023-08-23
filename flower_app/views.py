from django.shortcuts import render
from .models import Bouquet

def index(request):
    context = {
        'is_index_page': True
    }
    return render(request, 'index.html', context)

def catalog_api(request):
    return render(
        request,
        template_name='catalog.html',
        context={
            'bouquets': Bouquet.objects.all()
        }
    )


def card(request):
    return render(request, 'card.html')