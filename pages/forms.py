from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        })
    )
    subject = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject"
        })
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Message"
        })
    )

class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    website = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control"
        })
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control"
        })
    )

