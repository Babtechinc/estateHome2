from django.shortcuts import render,get_object_or_404
from agent.models import agent
from listing.models import listi_ng
from homeland.option import price,sq_ft,baths,beds,property_type,location
# Create your views here.
def agent_list(renderobj):
    agentlist = agent.objects.order_by('name')
    list_agent =  {'agentdict' : agentlist ,'price': price,
            'sq_ft': sq_ft,
            'baths': baths,
            'beds': beds,
            'location':location,
            'property_type':property_type}
    return render(renderobj,'agent.html',context=list_agent)
def agent_full(renderobj,agent_pid):
    agent_profile = get_object_or_404(agent,id=agent_pid)
    list_dict = listi_ng.objects.filter(agent_id=agent_pid)
    all_list = {'key':list_dict,'profile':agent_profile,'price': price,
            'sq_ft': sq_ft,
            'baths': baths,
            'beds': beds,
            'location':location,
            'property_type':property_type}
    return render(renderobj, 'single_agent.html',context=all_list )