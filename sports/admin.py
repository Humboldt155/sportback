from django.contrib import admin

# Register your models here.
from .models import SportGroup, SportSubGroup, Sport, SportType

admin.site.register(SportGroup)
# admin.site.register(SportSubGroup)
#admin.site.register(Sport)
admin.site.register(SportType)


class SubGroupInline(admin.TabularInline):
    model = SportSubGroup.sports.through

@admin.register(SportSubGroup)
class SportSubGroupAdmin(admin.ModelAdmin):
    inlines = (SubGroupInline,)
    exclude = ('sports',) # Excluding field to hide unnecessary field, as mentioned in the docs


class SportInline(admin.TabularInline):
    model = Sport.sport_sub_groups.through

@admin.register(Sport)
class SportSubGroupAdmin(admin.ModelAdmin):
    inlines = (SportInline,)
    #exclude = ('sports',) # Excluding field to hide unnecessary field, as mentioned in the docs
