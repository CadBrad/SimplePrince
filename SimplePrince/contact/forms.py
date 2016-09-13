from django import forms

from django.utils.translation import ugettext_lazy as _

from .models import Registration

# our new form
'''
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Let us know about your project"
'''
class ContactForm(forms.ModelForm):
    remember = forms.BooleanField(
    required=False, initial=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )


    class Meta:
        model = Registration
        fields = ('contact_name', 'contact_email')
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Project details"
        self.fields['remember'].label = "Email me updates on the Infinity-Box!"
            