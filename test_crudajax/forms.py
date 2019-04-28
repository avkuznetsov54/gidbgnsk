from datetime import datetime

from django import forms
from .models import Test1
from .models import Book


class FormTest1(forms.ModelForm):
    name = forms.CharField(label=None,
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя',
                                                         'class': 'form-control'}), )

    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control'}))

    class Meta:
        model = Test1
        fields = ('name', 'email')


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название',
                                                          'class': 'form-control'}), )
    publication_date = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                                     'value': datetime.strftime(datetime.now(), "%d.%m.%Y")
                                                                     }))

    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type',)
