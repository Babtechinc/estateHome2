from django.core.paginator import Paginator
from django.shortcuts import render,reverse,get_object_or_404
from listing.models import listi_ng
from homeland.option import price,sq_ft,baths,beds,property_type,location
# Create your views here.
def property(reponse):
    listing1= listi_ng.objects.all()
    paginator = Paginator(listing1, 6) # Show 25 contacts per page.
    page_number = reponse.GET.get('page')
    key = paginator.get_page(page_number)
    listdict = {'key':key,'price': price,
            'sq_ft': sq_ft,
            'baths': baths,
            'beds': beds,
            'location':location,
            'property_type':property_type}
    return render(reponse,'property.html',context=listdict)
def property_full(request,list_item):
    property_full_detail = get_object_or_404(listi_ng,pk=list_item)
    listdict = {'key': property_full_detail,'price': price,
            'sq_ft': sq_ft,
            'baths': baths,
            'beds': beds,
            'location':location,
            'property_type':property_type}
    return render(request, 'single_page.html',context=listdict)