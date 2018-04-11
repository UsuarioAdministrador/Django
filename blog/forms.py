from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ContactForm(forms.Form):
    emissor = forms.EmailField(required=True)
    assunto = forms.CharField(required=True)
    mensagem = forms.CharField(widget=forms.Textarea)