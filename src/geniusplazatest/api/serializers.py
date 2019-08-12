from rest_framework import serializers
from geniusplazatest.models import Recipe

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = [
			'pk',
			'name',
			'user',
					
			
		]