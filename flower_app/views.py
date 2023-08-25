from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bouquet, DeliveryTimeSlot, Client, Order, BouquetOrder
from .forms import OrderForm

def index(request):
    flowers = Bouquet.objects.order_by('?')[:3]
    context = {
        'is_index_page': True,
        'flowers': flowers
    }
    return render(request, 'index.html', context)


def catalog_api(request):
    flower_list = Bouquet.objects.filter(assortment=True)
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
    flower = get_object_or_404(Bouquet, id=id)
    return render(
        request,
        template_name='card.html',
        context={
            'flower': flower
        }
    )


def order(request, id):
    flower = get_object_or_404(Bouquet, id=id)

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['fname']
            phone = form.cleaned_data['tel']
            address = form.cleaned_data['adres']

            # Создаем запись клиента
            client, created = Client.objects.get_or_create(phone=phone, defaults={'name': name, 'address': address})

            # Создаем заказ
            order = form.save(commit=False)
            order.client = client
            order.delivery_time_slot = form.cleaned_data['orderTime']
            client.name = name
            client.address = address
            client.save()
            order.save()

            # Создаем заказ букета
            bouquet_order = BouquetOrder(bouquet=flower, order=order, quantity=1)
            bouquet_order.save()

            # Перенаправляем на страницу подтверждения или на другую страницу
            return redirect('order_result', id=order.id)

    else:
        form = OrderForm()

    context = {
        'form': form,
        'flower': flower,
    }

    return render(request, 'order.html', context)


def order_result(request, id):
    order = get_object_or_404(Order, id=id)
    bouquet_order = BouquetOrder.objects.get(order=order)
    flower = bouquet_order.bouquet
    return render(
        request,
        template_name='order_result.html',
        context={
            'order': order,
            'flower': flower,
        }
    )