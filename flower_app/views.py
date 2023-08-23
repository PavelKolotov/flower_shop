from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bouquet

def index(request):
    flowers = Bouquet.objects.order_by('?')[:3]
    context = {
        'is_index_page': True,
        'flowers': flowers
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


def card(request, id):
    flower = Bouquet.objects.get(id=id)
    return render(
        request,
        template_name='card.html',
        context={
            'flower': flower
        }
    )