from django.http import JsonResponse
from django.shortcuts import render
from .models import Passenger
from django.db.models import Count, Q

# Create your views here.
def ticket_class_view(request):
    dataset = Passenger.objects.values('ticket').annotate(survived_count = Count('ticket', filter=Q(survived=True)),not_survived_count = Count('ticket', filter=Q(survived=False))).order_by('ticket')
    return render(request, 'ticket_class.html', {'dataset': dataset})    


def json_example(request):
    return render(request, 'jsonexample.html')

def chart_data(request):
    dataset = Passenger.objects.values('embarked').exclude(embarked='').annotate(total=Count('embarked')).order_by('embarked')

    port_display_name = dict()
    for port_tuple in Passenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }    

    return JsonResponse(chart)