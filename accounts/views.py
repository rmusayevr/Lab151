from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, View
from django.contrib.auth import get_user_model,  authenticate, login as django_login, logout as django_logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from accounts.tasks import send_confirmation_mail
from django.contrib.sites.shortcuts import get_current_site
from .forms import LoginForm, RegistrationForm
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from accounts.tokens import account_activation_token
from products.models import ProductCategory

User = get_user_model()

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(parent__isnull=True)
        return context

    def form_invalid(self, form):
        messages.error(self.request, 'Yanlış email və ya şifrə')
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(parent__isnull=True)
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        send_confirmation_mail(user=self.object, current_site=get_current_site(self.request))
        messages.success(self.request, 'Please confirm your email address to complete the registration')
        messages.success(self.request, 'Zəhmət olmasa qeydiyyatı tamamlamaq üçün email ünvanınızı təsdiqləyin')
        return result
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)


class ActiveAccountView(View):

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(self.request, messages.SUCCESS,('Hesabınız aktivlaşdirilmişdir.'))
            return redirect(reverse_lazy('login_page'))
        else:
            messages.warning(request, 'Yanlış bir şey baş verdi!')
            return redirect(reverse_lazy('login_page'))