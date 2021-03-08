from django import forms
# from .models import Post


class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    phone = forms.IntegerField()
    city = forms.CharField(label="Город")
    vk = forms.URLField(label="Вк")
    last_name = forms.CharField(label="Фамилия")
    age = forms.IntegerField()
    inst = forms.URLField(label="Inst")
# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model = Post
#         fields = ('title', 'text',)
