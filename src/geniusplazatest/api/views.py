import django_filters.rest_framework
from rest_framework import generics, mixins
from geniusplazatest.models import Recipe
from .serializers import UserSerializer
#from django.db.models import Q


class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field			= 'pk'
	serializer_class 		= UserSerializer

	
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def get_queryset(self):
		queryset = Recipe.objects.all()
		user = self.request.GET.get("user")
		if user is not None:
			queryset = queryset.filter(user=user)
		return queryset
		#name = self.kwargs['name']
		#return Recipe.objects.filter(recipe__name=name)

class UserRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field			= 'pk'
	serializer_class 		= UserSerializer

	def get_queryset(self):
		return Recipe.objects.all()




	

