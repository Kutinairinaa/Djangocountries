# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Root project views                                                   #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2023 Irina                                             #
#                                                                      #
########################################################################


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(render(request, 'index.html'))
