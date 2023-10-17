from django.contrib import admin
from .models import Pertsona
from .models import Etxea
from .models import Alokairua

# Register your models here.
class PertsonaAdmin(admin.ModelAdmin):
    list_display = ['izena','emaila','nan']
    list_filter = ['izena','nan']
    search_fields = ['izena','emaila','nan']

admin.site.register(Pertsona,PertsonaAdmin)

class EtxeaAdmin(admin.ModelAdmin):
    list_display = ['izena','herria','pertsona_kop']
    list_filter = ['izena','herria','pertsona_kop']
    search_fields = ['izena','herria','pertsona_kop']

admin.site.register(Etxea,EtxeaAdmin)

class AlokairuaAdmin(admin.ModelAdmin):
    list_display = ['etxea','pertsona','alokatze_hasiera','alokatze_amaiera']
    list_filter = ['etxea','pertsona','alokatze_hasiera','alokatze_amaiera']
    search_fields = ['etxea','pertsona','alokatze_hasiera','alokatze_amaiera']

admin.site.register(Alokairua,AlokairuaAdmin)