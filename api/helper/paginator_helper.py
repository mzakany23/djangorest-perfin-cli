# python 
import math

from django.contrib.contenttypes.models import ContentType

# django rest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# django
from django.core.paginator import Paginator

# serializer
from rest_framework import serializers


class APIGenericGenerator(APIView):

	def __init__(self,**kwargs):
		self.queryset = kwargs['queryset']
		self.serializer = kwargs['serializer']
		

	def list(self,**kwargs):
		serializer_class = self.serializer
		serialized_objects = self.serializer(self.queryset,many=True)
		return serialized_objects.data

	def list_paginated_results(self,request,**kwargs):
		try:
			page_num = int(request.GET['page'])
			if page_num < 1: page_num = 1
		except:
			page_num = 1

		try:
			results_per_page = int(request.GET['results'])
			if results_per_page < 1: results_per_page = 1
		except:
			results_per_page = 10

		paginator = Paginator(self.queryset, results_per_page)

		try:
			page = paginator.page(page_num)
		except:
			page = paginator.page(1)

		max_pages = int(math.ceil(float(paginator.object_list.count())/float(results_per_page)))

		
		pagination = {
			'description' : str(page),
			'pages' : str(results_per_page),
			'current_page' : str(page.number),
			'start_index' : str(page.start_index()),
			'end_index' : str(page.end_index()),
			'total_records' : str(paginator.object_list.count()),
			'has_next' : str(page.has_next()),
			'max_pages' : str(max_pages)
		}

		serializer_class = self.serializer 
		serialized_objects = self.serializer(page,many=True).data

		return {'results':serialized_objects,'pagination': pagination}


