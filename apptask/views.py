from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from django.contrib import messages
from django.db.models import ProtectedError

def base_view(request):
    return render(request, 'base.html')

#BOOKS
def list_books(request):
    books = models.Biblio.objects.select_related('genderid').all()
    return render(request, 'biblio/listbooks.html', {'books': books})

def create_book(request):
    genders = models.Genderbook.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genderid = request.POST.get('genderid')
        aquisition = request.POST.get('aquisition')
        editor = request.POST.get('editor')
        num_page = request.POST.get('num_page')

        book = models.Biblio(
            title=title,
            author=author,
            genderid=models.Genderbook.objects.get(id=genderid) if genderid else None,
            aquisition=aquisition,
            editor=editor,
            num_page=num_page if num_page else None
        )
        book.save()

        return redirect('list_books')  # You can change this to any success page

    return render(request, 'biblio/createbook.html', {'genders': genders})

def edit_book(request, book_id):
    book = get_object_or_404(models.Biblio, id=book_id)
    genders = models.Genderbook.objects.all()

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        genderid = request.POST.get('genderid')
        book.genderid = models.Genderbook.objects.get(id=genderid) if genderid else None
        book.aquisition = request.POST.get('aquisition')
        book.editor = request.POST.get('editor')
        book.num_page = request.POST.get('num_page') or None

        book.save()
        return redirect('list_books')  # or another success page

    return render(request, 'biblio/editbook.html', {'book': book, 'genders': genders})


def delete_book(request, book_id):
    book = get_object_or_404(models.Biblio, id=book_id)
    book.delete()
    return redirect('list_books')

#GENDERS
def list_gender(request):
    genders = models.Genderbook.objects.all()
    return render(request, 'genderbook/listgender.html', {'genders':genders})

def create_gender(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        genderbook = models.Genderbook(name=name)
        genderbook.save()

        return redirect('genders')

    return render(request, 'genderbook/creategender.html')

def edit_gender(request, gender_id):
    gender = models.Genderbook.objects.get(id=gender_id)

    if request.method == 'POST':
        new_name = request.POST.get('name')
        gender.name = new_name
        gender.save()
        return redirect('genders')

    return render(request, 'genderbook/editgender.html', {'gender': gender})

def delete_gender(request, gender_id):
    gender = models.Genderbook.objects.get(id=gender_id)
    if models.Biblio.objects.filter(genderid=gender).exists():
        messages.warning(request, 'Não é possível apagar este género porque está associado a um ou mais livros.')
        return redirect('genders')
    
    gender.delete()
    messages.success(request, 'Género apagado com sucesso.')
    return redirect('genders')