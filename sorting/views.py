from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *

# Create your views here.`
@csrf_exempt
def SortingView(request):
	if request.method== 'POST':
		arr=(request.POST.getlist('d[]'))
		print(arr)
		sortedlist=quicksort(arr)
		print(sortedlist)
		return JsonResponse({'sorted':sortedlist})

	return render(request,'sorting/sort.html')


