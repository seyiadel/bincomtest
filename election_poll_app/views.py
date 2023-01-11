from django.shortcuts import render
from .models import Announced_Pu_Results, Polling_Unit, Lga
# Create your views here.
def homepage(request):
    if request.method == "POST":
        get_polling_result_id = request.POST.get("search")
        polling_unit = Announced_Pu_Results.objects.get(result_id = get_polling_result_id)
        return render(request, 'home.html', {"polling_unit": polling_unit})
    return render(request, 'home.html')

def get_poll_result(request):
    request.method == "GET"
    lga = Lga.objects.get(lga_name="Aniocha North").lga_id
    poll = Polling_Unit.objects.filter(lga_id_id=lga)
    for i in poll:
        verifyFromAPR = Announced_Pu_Results.objects.filter(polling_unit_uniqueid_id=i.polling_unit_id)
        polling_number = verifyFromAPR.party_score
            
        # polling_unit_result = party_score.count()
        return render(request, 'get_poll.html', context={"polling_unit_result":polling_number})
    return render(request, 'get_poll.html',)

