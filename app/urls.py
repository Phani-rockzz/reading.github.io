from django.urls import path, include, reverse_lazy
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('reading/', views.reading, name='reading'),
    path('list/', views.datareading, name='list'),
    path('search/', views.datefilter, name='search'),
    url(r'^detail/(?P<pk>\d+)$', views.datadetails, name='detail'),
    url(r'^edit/(?P<pk>\d+)$', views.reading_update, name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.reading_delete, name='delete'),
    path('contact/', views.contact, name='contact'),
    # password reset
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='app/password_reset_form.html',
             subject_template_name='app/password_reset_subject.txt',
             email_template_name='app/password_reset_email.html',
             success_url=reverse_lazy('app:password_reset_done')
         ),
         name='password_reset'),


    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'
                                                                            ), name='password_reset_done'),


    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('app:password_reset_complete')),
        name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='app/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='app/password_change.html',
            success_url='app/password_change_done.html'
        ),
        name='change_password'
    ),
]
