from django.shortcuts import render, redirect
from .models import Show

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
    print("Network", request.POST['network'])
    show_id = request.POST['show_id']
    show_to_edit = Show.objects.get(id=show_id)
    if  len(request.POST['title']) > 0:
        title = request.POST['title']
        show_to_edit.title = title
        show_to_edit.save()
    if len(request.POST['network']) > 0:
        network = request.POST['network']
        show_to_edit.network = network
        show_to_edit.save()
    if len(request.POST['release_date']) > 0:
        release_date = request.POST['release_date']
        show_to_edit.release_date = release_date
    if len(request.POST['description']) > 0:
        description = request.POST['description']
        show_to_edit.description = description
        show_to_edit.save()
    return redirect(f'/shows/{show_id}')