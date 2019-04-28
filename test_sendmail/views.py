from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings

from .forms import EmailForm


def send_email(request):
    if request.method != 'POST':
        form = EmailForm()
        return render(request, 'test_sendmail/index2.html', {'email_form': form})

    form = EmailForm(request.POST, request.FILES)
    # to_email = form.cleaned_data['to_email']

    if form.is_valid():
        from_email = form.cleaned_data['from_email']
        to_email = form.cleaned_data['to_email'].replace(' ', '').split(',')
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        print(to_email)
        try:
            attach = request.FILES['attach']
        except:
            attach = None

        try:
            mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to_email,
                                headers={'From': from_email, 'Reply-to': from_email})

            if attach is not None:
                mail.attach(attach.name, attach.read(), attach.content_type)

            mail.content_subtype = 'html'
            mail.send()

            return render(request, 'test_sendmail/index2.html', {'message': 'Sent email to %s' % to_email})

        except (ValueError, TypeError, AttributeError, KeyError):
            print('Ошибка1')

        except:
            print('Ошибка2')
            # return render(request, 'admin/Error.html', {'message': 'Either the attachment is too  big or corrupt'})

    return render(request, 'test_sendmail/index2.html', {'message': 'Unable to send email. Please try again later'})
