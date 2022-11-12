# Este modulo nos permite hacer uso de la libreria de Import_Export
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

# ------- 9
# Importamos nuestro modelo Posts

from .models import Posts

# Register your models here.

# -------- 10
# Registramos Nuestro modelo para añadirlo al panel de administracion

@admin.register(Posts)
class PostAdmin(ImportExportModelAdmin):
    list_display = ('fecha','titulo','categoria',)
    list_display_links = ('titulo',)
    search_fields = ('categoria',)

