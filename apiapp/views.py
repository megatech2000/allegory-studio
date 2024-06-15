from django.shortcuts import render
from rest_framework import viewsets
from .models import Work,Featured,GearItem,GearCategory
from .serializer import WorkSerializer,FeatureSerializer,GearCategorySerializer,GearItemSerializer

# Create your views here.

class WorkViewset(viewsets.ModelViewSet):
    queryset = Work.objects.all().order_by('-date_created')
    serializer_class= WorkSerializer

class featureViewset(viewsets.ModelViewSet):
    queryset = Featured.objects.all()
    serializer_class = FeatureSerializer

class gearCategoryViewset(viewsets.ModelViewSet):
    queryset = GearCategory.objects.all()
    serializer_class = GearCategorySerializer

class gearItemViewset(viewsets.ModelViewSet):
    queryset = GearItem.objects.all()
    serializer_class = GearItemSerializer


