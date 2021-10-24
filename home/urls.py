from django.urls import path
from django.contrib.auth.decorators import login_required
from. import views

urlpatterns = [
		path("", views.login_request, name="login"),
    #path('homepage', views.homepage, name="homepage"),
		path('homepage', login_required(views.homepage), name="homepage"),
		path("logout", login_required(views.logout_request), name= "logout"),
    ]