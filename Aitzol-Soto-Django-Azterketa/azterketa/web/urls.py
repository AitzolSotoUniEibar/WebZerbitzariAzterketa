from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),

    path('addetxea/',views.addetxea,name='addetxea'),
    path('addetxea/gehituetxea/',views.etxeagehitu,name='gehituetxea'),
    path('updateetxea/<int:etxea_id>/',views.updateetxea,name='updateetxea'),
    path('updateetxea/<int:etxea_id>/aldatuetxea/',views.aldatuetxea,name='aldatuetxea'),
    path('deleteetxea/<int:etxea_id>',views.deleteetxea,name='deleteetxea'),

    path('addpertsona/',views.addpertsona,name='addpertsona'),
    path('addpertsona/gehitupertsona/',views.pertsonagehitu,name='pertsonagehitu'),
    path('updatepertsona/<int:pertsona_id>/',views.updatepertsona,name='updatepertsona'),
    path('updatepertsona/<int:pertsona_id>/aldatupertsona/',views.aldatupertsona,name='aldatuepertsona'),
    path('deletepertsona/<int:pertsona_id>',views.deletepertsona,name='deletepertsona'),

    path('alokatu/',views.alokatu,name='alokatu'),
    path('alokatu/alokatuetxea/',views.alokatuetxea,name='alokatuetxea')
]
