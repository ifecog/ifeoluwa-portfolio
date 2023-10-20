from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control px-3 py-4', 'placeholder': 'Your Name', 'style': 'color: white;'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control px-3 py-4', 'placeholder': 'Your Email', 'style': 'color: white;'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control px-3 py-4', 'placeholder': 'Write a Message', 'style': 'color: white;'})
    )
