from django.shortcuts import render, redirect, get_object_or_404
from random import choice
from datetime import datetime
from string import ascii_letters, digits
from .forms import LinkForm
from .models import Link

SIZE = 7  # > 78 млрд уникальных ссылок
AVAILABLE_CHARS = ascii_letters + digits  # использую буквы и цифры


def gen_link(ascii_uppercase=AVAILABLE_CHARS, size=SIZE):
    glink = ''.join(choice(ascii_uppercase) for i in range(size))
    return glink


def input_link(request):
    form = LinkForm()
    if request.method == 'POST':
        in_link = LinkForm(request.POST)
        if in_link.is_valid():
            link = request.POST.get('input_link')
            if Link.objects.filter(input_link=link).exists():
                true_link = link_in_database(link)
            else:
                true_link = short_link_in_database(gen_link())
                li = Link(input_link=link, output_link=true_link, clicks=1, date_last_click=datetime.now())
                li.save()
            return render(request, 'link_shorter_1.html', {'in_link': in_link , 'links': request.build_absolute_uri('/') + true_link})
        else:
            return render(request, 'link_shorter.html', {'error': 'Data is not valid'})
    else:
        return render(request, 'link_shorter.html', {'form': form, })



def short_link_in_database(link):
    if Link.objects.filter(output_link=link).exists():
        return gen_link()
    else:
        return link


def link_in_database(link):
    link_old = Link.objects.get(input_link=link)
    link_old.clicks = link_old.clicks + 1
    link_old.date_last_click = datetime.now()
    link_old.save()
    return link_old.output_link


def relink(request, data):
    if Link.objects.filter(output_link=data).exists():
        obj = Link.objects.get(output_link=data)
        link = obj.input_link
        obj.clicks = obj.clicks + 1
        obj.date_last_click = datetime.now()
        obj.save()
        return redirect(link)

