# My Django imports
from django import forms

# My app imports
from CST_cms.models import Post, Category

class PostForm(forms.ModelForm):
    title = forms.CharField(required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'autofocus':'',
        }
    ))

    # body = forms.CharField(required=True,help_text='Content of the tutorial', widget=forms.Textarea(
    #     attrs={
    #         'class':'form-control',
    #     }
    # ))

    image = forms.ImageField(required=False, widget=forms.FileInput(
                attrs={
                    'class':'form-control',
                    'type':'file',
                    'accept':'image/png, image/jpeg'
                }
            ))

    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=1, required=True,
        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        ))

    class Meta:
        model = Post
        exclude = ['slug', 'approval']