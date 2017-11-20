from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
	objects = Restaurant.objects.all()
	context = {
	'objects': objects
	}

	return render(request, 'restaurant_list.html', context)

def restaurant_detail(request):
	x = Restaurant.object.get(id=restaurant_id)
	context = {
	'object': x
	}

	return render(request, 'restaurant_detail.html', context)
