# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def home(request):
    context = {'title': 'Welkom on our Mood Monitor'}
    return render(request, 'base.html', context)
