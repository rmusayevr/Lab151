from django.urls import path
from accounts.views import ActiveAccountView, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login_page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('activate/<str:uidb64>/<str:token>/', ActiveAccountView.as_view(), name="activate"),
]