from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Comment
from django import forms


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',

            }),

            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',

            }),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')