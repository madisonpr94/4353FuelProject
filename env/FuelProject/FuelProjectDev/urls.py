from django.urls import path
from django.conf.urls import url
from . import views

# Index / Landing page
urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('index', views.index_page, name='index_page')
]

# Profile page
urlpatterns += [
    path('profile', views.profile_page, name='profile_page')
]

# Login page
urlpatterns += [
    path('login', views.login_page, name='login_page'),
    path('login', views.login_page, name='login_page',
         kwargs={'redirect_not_logged_in': True})
]

# Pricing page
urlpatterns += [
    path('quote_request', views.quote_page, name="quote_page"),
    path('price_module', views.price_module, name='price_module'),
    path('checkout', views.checkout_page, name="checkout_page")
]

# Quote History page
urlpatterns += [
    path('quote_history', views.history_page, name='history_page')
]
