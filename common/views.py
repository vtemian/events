from django.shortcuts import render_to_response, render
from django.template.context import RequestContext

def home(request):
    if request.user.is_authenticated():
        context = {}
        return render_to_response('login.html', context, context_instance=RequestContext(request))
    else:
        return render(request, 'home.html')