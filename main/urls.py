from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("auction/", views.AuctionView, name="auction"),
	path("account/", views.AccountView, name="account"),
	path("checkout/", views.CheckOutView, name="checkout"),

]