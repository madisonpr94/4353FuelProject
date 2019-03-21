from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('index.html/', views.index_page, name='index_page'),
    path('login.html/', views.login_page, name='login_page'),
    #path('login.html/login.html', views.login_page, name='login_page'),
    path('profile.html/', views.profile_page, name='profile_page'),
    # path('login.html/index.html', views.index_page, name='index_page')
]

urlpatterns += [
    path('login.html', views.login_page, name='login_page',
         kwargs={'redirect_not_logged_in': True})
]

urlpatterns += [
    path('quote_request.html', views.quote_page, name="quote_page"),
    path('price_module', views.price_module, name='price_module')
]
