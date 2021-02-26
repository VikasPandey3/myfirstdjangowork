from django.conf.urls import url
from django.contrib.auth import views
from . import views as site_view
from django.contrib.auth.views import \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView

urlpatterns = [

    url(r'^main/$', site_view.main, name="main"),

    url(r'^Login', site_view.login_form, name="Login"),
    url(r'^login/$', site_view.auth_user, name="login"),

    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),

    # url(r'^Signup', site_view.signup_form, name="signup"),
    url(r'^register', site_view.register, name="register"),

    url(r'^retrieve/(?P<pk>\w+)/$', site_view.api_data, name="retrieve"),
    url(r'^update/(?P<pk>\w+)/$', site_view.update, name="update"),

    url(r'^reset/password/$', PasswordResetView.as_view(), name="PasswordRestView"),

    url(r'^password/reset/done/$', PasswordResetDoneView.as_view(), name="password_reset_done"),

    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"),

    url(r'^password/reset/complete/$', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
