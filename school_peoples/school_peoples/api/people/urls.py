from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'alumns', AlumnViewSet, basename='alumns')
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'classrooms', ClassRoomViewSet, basename='classrooms')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'materials', MaterialsViewSet, basename='materials')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'
    ))
]