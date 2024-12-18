from django.shortcuts import render, redirect
from .models import Tertulia



def tertulias_list(request):
    
    tertulias = Tertulia.objects.all().order_by('id')



    context = {
        'tertulias': tertulias,
}
    return render(request, 'tertulias/tertulias_list_copia.html', context)





