from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf=8') as cvsfile:
        reader = csv.DictReader(cvsfile)
        bus_stations_list = list(reader)

    paginator = Paginator(bus_stations_list, 50)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)

    context = {
        'bus_stations': pages.object_list,
        'paginator': paginator,
        'page': pages,
    }
    return render(request, 'stations/index.html', context)

