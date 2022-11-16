from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt

from main.ray_bns import GetAddress, GetPrice



#from .forms import UserForm


def IndexView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/index.html", context )


def AuctionView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/auction.html", context )


def AccountView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/account.html", context )

def CheckOutView(request):

	if request.method == "POST":
		pass

	else:

		context = {}
		return render(request, "main/checkout.html", context )




def FindView(request):

	if request.method == "POST":
		domain_name = request.POST.get("domain_name")

		return HttpResponseRedirect(reverse("main:result", args=[domain_name,]))

	else:

		context = {}
		return render(request, "main/find.html", context )



def ResultView(request, domain_name):

	if request.method == "POST":
		pass

	else:
		name_address = GetAddress(domain_name)

		if name_address == "0x0000000000000000000000000000000000000000":
			available = True
		else:
			available = False
		
		name_price = GetPrice(domain_name)

		context = {"domain_name": domain_name, "available": available, "name_price": name_price}
		return render(request, "main/result.html", context )



def BuyView(request, domain_name):

	if request.method == "POST":
		pass

	else:

		context = {"domain_name": domain_name}
		return render(request, "main/buy.html", context )

