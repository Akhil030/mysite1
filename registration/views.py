from django.views.generic import View
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from .utils import generate_token
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.


def registration(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=name).exists():
            messages.info(request, 'Name exists')
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email exists ')
            return redirect('/')
        else:
            user = User.objects.create_user(username=name, password=password, email=email)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Active your Account'
            message = render_to_string('activate.html',
                                       {
                                           'user': user,
                                           'domain': current_site.domain,
                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                           'token': generate_token.make_token(user)
                                       }
                                       )

            email = EmailMessage(
                email_subject,
                message,
                'testakhil261@gmail.com',
                [email],
            )
            email.send(fail_silently=True)

            messages.info(request, 'user created')
            return redirect('/accounts/login')


    else:
        return redirect('/')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 'account activated successfully')
            return redirect('login')
        return render(request, 'activate_failed.html', status=401)


