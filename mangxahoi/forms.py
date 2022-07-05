from dataclasses import field
from tkinter import Widget
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '(Lưu ý: Bạn có thể định dạng văn bản của mình với html hoặc css)'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '(Lưu ý: Bạn có thể định dạng văn bản của mình với html hoặc css)'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            #'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }