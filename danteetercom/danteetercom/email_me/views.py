from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .forms import emailForm
from django.views.decorators.csrf import csrf_protect

# SEND EMAIL TO DANTEETERWEBSITE@GMAIL.COM
@csrf_protect
def email_me(request):
    title = ""
    sub_title = 'Please complete and send:'
    form = emailForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        topic = form.cleaned_data['topic']
        comment = form.cleaned_data['comment']
        email_sender = form.cleaned_data['email_sender']
        subject = '%s %s' %('Message from ', name)
        message = '%s // %s (%s)' %(topic, comment, email_sender)
        from_email = form.cleaned_data['email_sender']
        to_email = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_email, fail_silently=True)
        title = 'Success!'
        sub_title = "Your message has been sent."
        confirm_message = "I will try to respond shortly.  Thanks :)"
        form = None

    context = {'title':title, 'sub_title': sub_title, 'form':form, 'confirm_message':confirm_message}
    template ='email_me/email_me.html'
    return render(request, template, context)
