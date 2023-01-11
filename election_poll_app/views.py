from django.shortcuts import render
from .models import Announced_Pu_Results
# Create your views here.
def homepage(request):
    if request.method == "GET":
        polling_unit = Announced_Pu_Results.objects.get(result_id = 114)
    return render(request, 'home.html', context={"polling_unit": polling_unit})


