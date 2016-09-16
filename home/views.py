# django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout


# models
from django.contrib.auth.models import User 


class HomeView(View):
	template = 'base.html'
	context = {}
	
	def get(self,request):
		return render(request,self.template,self.context)
	