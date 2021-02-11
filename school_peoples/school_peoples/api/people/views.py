from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all().order_by('id')
    serializer_class = PeopleSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer

class AlumnViewSet(viewsets.ModelViewSet):
    queryset = Alumn.objects.all().order_by('id')
    serializer_class = AlumnSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all().order_by('id')
    serializer_class = ClassRoomSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer


class MaterialsViewSet(viewsets.ModelViewSet):
    queryset = Materials.objects.all().order_by('id')
    serializer_class = MaterialsSerializer
