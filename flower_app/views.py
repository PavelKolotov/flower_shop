from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bouquet

def index(request):
    context = {
        'is_index_page': True
    }
    return render(request, 'index.html', context)

def catalog_api(request):
    flower_list = Bouquet.objects.all()
    paginator = Paginator(flower_list, 6)

    page = request.GET.get('page')
    try:
        flowers = paginator.page(page)
    except PageNotAnInteger:
        flowers = paginator.page(1)
    except EmptyPage:
        flowers = paginator.page(paginator.num_pages)

    return render(
        request,
        template_name='catalog.html',
        context={
            'flowers': flowers
        }
    )


def card(request):
    return render(request, 'card.html')