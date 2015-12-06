from django.contrib import admin
from monopolyprobability.models import Color, Property, Owned


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color',)


@admin.register(Owned)
class OwnedAdmin(admin.ModelAdmin):
    list_display = ('user', 'property')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price', 'probability', 'rent', 'value')
