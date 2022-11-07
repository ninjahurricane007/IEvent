from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('fests', views.fests, name='fests'),
    path('addfest', views.addfest, name='addfest'),
    path('events/<uuid:id>', views.events, name='events'),
    path('getyourevents', views.getyourevents, name='getyourevents'),
    path('regevent/<uuid:id>', views.regevent, name='regevent'),
    path('checkout/<uuid:id>', views.checkout, name='checkout'),
    path('verify_payment', views.verify_payment, name='verify_payment'),
    path('cordinator', views.cordinator, name='coordinator'),
    path('unregister/<uuid:id>', views.unregister, name='unregister'),
    path('eventcreate/<uuid:id>', views.eventcreate, name='eventcreate'),
    path('festdelete/<uuid:id>', views.festdelete, name='festdelete'),
    path('eventdelete/<uuid:id>', views.eventdelete, name='eventdelete'),
    path('profile', views.profile, name='profile'),
    path('editprofile', views.editprofile, name='editprofile'),
]

