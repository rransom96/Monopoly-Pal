from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from monopolyprobability.forms import OwnedForm, TradeForm, OwnedOtherForm
from monopolyprobability.models import Property, Owned


def property(request):
    property = Property.objects.all()
    property = sorted(property, key=lambda x: x.value())
    for square in property:
        if square.owned_set.count() >= 1:
            property.remove(square)
    return render(request, 'monopolyprobability/property_list.html', {'property':property})


def delete(request):
    Owned.objects.all().delete()
    return HttpResponseRedirect(reverse('list_properties'))


def create_owned(request):
    if request.method == 'POST':
        form = OwnedForm(request.POST)
        if form.is_valid():
            owned = form.save()
            owned.save()
            return HttpResponseRedirect(reverse('list_properties'))
    else:
        form = OwnedForm()

    return render_to_response('monopolyprobability/owned_create.html',
                              {"owned_form": form},
                              context_instance=RequestContext(request))


def trade(request):
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            owned = form.save()
            owned.save()
            return HttpResponseRedirect(reverse('list_properties'))
    else:
        form = TradeForm()

    return render_to_response('monopolyprobability/owned_trade.html',
                              {"owned_form": form},
                              context_instance=RequestContext(request))


def create_owned_other(request):
    if request.method == 'POST':
        form = OwnedOtherForm(request.POST)
        if form.is_valid():
            owned = form.save()
            owned.save()
            return HttpResponseRedirect(reverse('list_properties'))
    else:
        form = OwnedOtherForm()

    return render_to_response('monopolyprobability/owned_other_create.html',
                              {"owned_form": form},
                              context_instance=RequestContext(request))


def other_owned(request):
    property = Property.objects.filter(owner=2)
    property = sorted(property, key=lambda x: x.value())
    return render(request, 'monopolyprobability/property_list.html', {'property':property})


def owned(request):
    property = Property.objects.filter(owner=1)
    property = sorted(property, key=lambda x: x.value())
    return render(request, 'monopolyprobability/property_list.html', {'property':property})