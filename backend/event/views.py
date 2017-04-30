# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse, Http404
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Event
from .serializer import EventSerializer

class ListEvent(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    paginate_by = 10
    paginate_by_param = 'page'
    max_paginate_by = 100

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return JsonResponse({
            "data" : serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse({ "data" : serializer.data})

# Create your views here.
