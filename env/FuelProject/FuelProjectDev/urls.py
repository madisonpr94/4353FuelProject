from django.urls import path, re_path
from django.conf.urls import url
from . import views

# Index / Landing page
urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('index', views.index_page, name='index_page'),
    url(r'^login/index', views.index_page, name='index_page'),
]

# Profile page
urlpatterns += [
    path('profile', views.profile_page, name='profile_page')
]

# Login page
urlpatterns += [
    url('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
]

# Pricing page
urlpatterns += [
    path('quote_request', views.quote_page, name="quote_page"),
    path('price_module', views.price_module, name='price_module')
]

# Quote History page
urlpatterns += [
    url('quote_history', views.history_page, name='history_page')
]
