from django.shortcuts import render, redirect
from django.http import Http404
from glossary.models import Acronym
from .forms import AcronymForm

from django.http import HttpResponse


def index(request):
    acronyms = Acronym.objects.all()
    return render(request, 'glossary/index.html', {
        'acronyms': acronyms,
    })


def acronym_detail(request, id):
    try:
        acronym = Acronym.objects.get(id=id)
    except Acronym.DoesNotExist:
        raise Http404('This Acronym does not exist')
    return render(request, 'glossary/acronym_detail.html', {
        'acronym': acronym
    })


def acronym_new(request):
    if request.method == "POST":
        form = AcronymForm(request.POST)
        if form.is_valid():
            acronym = form.save(commit=False)
            acronym.abbreviation = form.cleaned_data['abbreviation']
            acronym.word = form.cleaned_data['word']
            acronym.save()
            return redirect('acronym_detail', id=acronym.id)
    else:
        form = AcronymForm()
    return render(request, 'glossary/acronym_edit.html', {'form': form})
