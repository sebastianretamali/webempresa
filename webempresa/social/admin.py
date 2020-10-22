from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personl").exists():
            return ('key', 'name')
        else:
            return('creted', 'updated')

admin.site.register(Link, LinkAdmin)