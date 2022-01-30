from django import forms
from .models import Post
#linking the cat Model to out add post M

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','title_tag','author','body','pic')

        widgets={
            'title': forms.TextInput(attrs={'class':'inputForm','placeholder':' Post Title'}),
            'title_tag': forms.TextInput(attrs={'class':'inputForm tag','type':'hidden'}),
            'author': forms.TextInput(attrs={'class':' userId','value':'','type':'hidden'}),
            'body': forms.Textarea(attrs={'class':'bodyText','placeholder':' Write your Article here'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','body','pic')

        widgets={
            'title': forms.TextInput(attrs={'class':'inputForm'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'input your article here'}),
        }