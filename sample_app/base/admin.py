from django.contrib import admin
from base import models


@admin.register(models.Dog)
class DogAdmin(admin.ModelAdmin):
    class FriendsInline(admin.StackedInline):
        model = models.Dog.dog_friends.through
        verbose_name = 'friend'
        verbose_name_plural = 'friends'
        autocomplete_fields = ['to_dog']
        fk_name = 'from_dog'
        extra = 0
    class VaccinesInline(admin.StackedInline):
        model = models.Dog.vaccines.through
        verbose_name = 'vaccine'
        verbose_name_plural = 'vaccines'
        autocomplete_fields = ['vaccine']
        extra = 0

    inlines = [FriendsInline, VaccinesInline]
    search_fields = ['name']
    fields = ['name', 'age', 'owner']
    list_display = ['name', 'age', 'owner']


@admin.register(models.Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    class FriendsInline(admin.StackedInline):
        model = models.Vaccine.covered_diseases.through
        verbose_name = 'covered disease'
        verbose_name_plural = 'covered diseases'
        autocomplete_fields = ['disease']
        extra = 0

    inlines = [FriendsInline]
    search_fields = ['name']
    fields = ['name']
    list_display = ['name']


@admin.register(models.Disease)
class DiseaseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    fields = ['name']
    list_display = ['name']