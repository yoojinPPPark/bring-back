from fileinput import filename
import os 

from tracemalloc import get_object_traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import json

import config
from . import models
from . import serializers
from config import settings

# Create your views here.
class Capsule(APIView):
    def get(self, request, format=None):
        capsule = models.Capsule.objects.all()
        serializer = serializers.CapsuleSerializer(capsule, many=True)
        
        return Response(serializer.data)
        


#개별적으로 보여주는 건 /<int:id> 이런식으로 api(url)만 구현