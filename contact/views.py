from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            email = form.cleaned_data['email']
            try:
                send_mail(subject, message, email,
                          ['mphphotography.ni@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('email_success')

    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})


def email_success(request):

    return render(request, "contact/contact_success.html")
