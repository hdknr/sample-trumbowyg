from django.contrib import admin
from django.forms import ModelForm
from .models import Entry

# Register your models here.


class EntryAdminForm(ModelForm):

    class Meta:
        model = Entry
        exclude = []


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm


admin.site.register(Entry, EntryAdmin)
