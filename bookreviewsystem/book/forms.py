# from django import forms
# from book.models import Book


# class BookForm(forms.ModelForm):
#   class Meta:
#     model=Book
#     fields=['title','author','decription','genre','isbn','publication_date']

#     widgets={
#       'title':forms.TextInput(attrs={'class':'form-control','row':4,
#                                      'placeholder':'Enter book description'}),
#       'genre':forms.Select(attrs={
#         'class':'form-contrl'
#       }),
#       'isbn':forms.TextInput(attrs={
#         'class':'form-control',
#         'placeholder':'Enter ISBN'
#       }),
#       'publication_date':forms.DateInput(attrs={
#         'class':'form-control',
#         'type':'date'
#       })
#     }


from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'genre',
            'isbn',
            'publication_date',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_date': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
        }
