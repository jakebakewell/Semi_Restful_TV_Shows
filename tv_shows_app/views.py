from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, 'shows.html', context)

def shows_new(request):
    return render(request, 'shows_new.html')

def process_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        Show.objects.create(title=title, network=network, release_date=release_date, description=description)
        return redirect('/shows')

def specific_show(request, id_num):
    context = {
        "show": Show.objects.get(id=id_num)
    }
    return render(request, 'specific_show.html', context)

def delete(request, id_num):
    show_to_delete = Show.objects.get(id=id_num)
    show_to_delete.delete()
    return redirect('/shows')

def edit(request, id_num):
    context = {
        "show": Show.objects.get(id=id_num)
    }
    return render(request, 'edit.html', context)

def process_edit(request):
    show_id = request.POST['show_id']
    show_to_edit = Show.objects.get(id=show_id)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')

    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        show_to_edit.title = title
        show_to_edit.network = network
        show_to_edit.release_date = release_date
        show_to_edit.description = description
        show_to_edit.save()
    return redirect(f'/shows/{show_id}')