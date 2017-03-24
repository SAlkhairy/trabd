from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from models import Position, Nomination
from forms import NominationForm

#from forms import NominationForm

# Create your views here.


def show_index(request):
    return HttpResponse(render(request, 'accounts/home.html'))


login_required
def add_nominee(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    instance = Nomination(position=position)
    if request.method == 'POST':
        form = NominationForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save(request.user)
            context = {'form': form}
        return HttpResponse(render(request,'voting/add_nominee.html', context))

    elif request.method == 'GET':
        form = NominationForm(request.GET, instance=instance)
        context = {'form': form}
        return HttpResponse(render(request,'voting/add_nominee.html', context))



