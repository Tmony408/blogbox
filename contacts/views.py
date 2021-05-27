from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages
from tmonyblog.settings import EMAIL_HOST_USER



# Create your views here.
def contact (request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone=request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        subjects= subject  ,   phone

        contact = Contact(name=name, email=email, message=message,subject=subjects)
        contact.save()
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            ['adetulatestimony@gmail.com'],
            fail_silently=False,
        ) 
        messages.success(request, 'Thanks for reaching out to us at Blogbox')
        return redirect('contact')
    else:
        content={

        }
        return render(request,'contact.html',content)