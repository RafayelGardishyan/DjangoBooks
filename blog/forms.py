from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    active = forms.BooleanField(required=False) # required=False makes the field optional
    created_on = forms.DateTimeField()
    last_logged_in = forms.DateTimeField()