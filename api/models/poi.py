from simple_history.models import HistoricalRecords
from django.db import models
from .utils import TimestampMixin


##Point of interest table 
class PoI(TimestampMixin):
    poi_id = models.CharField(max_length=100, verbose_name='poi external id')
    poi_name = models.CharField(max_length=255)
    poi_category = models.CharField(max_length=100)
    poi_latitude = models.FloatField()
    poi_longitude = models.FloatField()
    poi_ratings = models.JSONField()
    
    def __str__(self):
        return self.poi_name
    
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = "POI"
        verbose_name_plural = "POIs"
    
    