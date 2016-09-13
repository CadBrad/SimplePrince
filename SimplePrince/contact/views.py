from django.shortcuts import render

from SimplePrince.contact.forms import ContactForm
from django.contrib.messages import get_messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template import Context
from django.http import HttpResponseRedirect
from django.contrib import messages

# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            send_mail(
                "New contact form submission",
                content,
                contact_email,
                ['3DPrinceinfo@gmail.com'],
                fail_silently=False,
            )
            


            #Save email and name if requested
            form_remember = request.POST.get('remember', '')

            if form_remember == "on":
                form.save()

            messages.add_message(request, messages.SUCCESS, "Form submitted, we will get back to you soon!")    
            return HttpResponseRedirect('contact')
    return render(request, 'contact.html', {
        'form': form_class,
    })