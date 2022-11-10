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


