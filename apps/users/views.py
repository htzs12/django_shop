from django.shortcuts import render
from rest_framework import views
from rest_framework.throttling import BaseThrottle
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.viewsets import ModelViewSet
from django.views.generic import View