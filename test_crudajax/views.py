from django.shortcuts import render, get_object_or_404
from .forms import FormTest1
from .models import Book
from .forms import BookForm
from django.http import JsonResponse
from django.template.loader import render_to_string


def test1(request):
    form = FormTest1()
    if request.is_ajax():
        form = FormTest1(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {
                'message': 'form is saved'
            }
            return JsonResponse(data)
    context = {
        'form': form,
    }
    return render(request, 'test_crudajax/form.html', context)


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'test_crudajax/book_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['book_list'] = render_to_string('test_crudajax/book_list_2.html', {'books': books})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_all(request, form, 'test_crudajax/book_create.html')


def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_all(request, form, 'test_crudajax/book_update.html')


def book_delete(request, id):
    data = dict()
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        data['form_is_valid'] = True
        books = Book.objects.all()
        data['book_list'] = render_to_string('test_crudajax/book_list_2.html', {'books': books})
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('test_crudajax/book_delete.html', context, request=request)

    return JsonResponse(data)
