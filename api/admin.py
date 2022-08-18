from django.contrib import admin
from .models import PoI

##Custom admin table for POI's filtering and search
@admin.register(PoI)
class PoIAdmin(admin.ModelAdmin):
    search_fields = ['id', 'poi_id', 'poi_name']
    list_display = ('get_id', 'poi_id', 'poi_name', 'poi_category','get_average_rating')
    list_filter = ['poi_category']

    def get_average_rating(self, obj):
        if obj.poi_ratings:
            return sum(obj.poi_ratings) / len(obj.poi_ratings)
        return None
    
    def get_id(self, obj):
        return obj.id
    
    get_average_rating.short_description = 'Average Rating'
    get_id.short_description = 'POI internal ID'