import csv
import ast
import json
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from api.models import PoI
from bs4 import BeautifulSoup
import threading
import os
from django.core.serializers import serialize
class Command(BaseCommand):
    help = 'Import PoI data from CSV, JSON, and XML files'
    def add_arguments(self, parser):
        parser.add_argument('files', nargs='+', type=str)
    def handle(self, *args, **kwargs):
        for file_path in kwargs['files']:
            if file_path.endswith('.json'):
                self.import_json(file_path)
            elif file_path.endswith('.xml'):
                self.import_xml(file_path)
            elif file_path.endswith('.csv'):
                 self.import_csv(file_path)
            else:
                self.stdout.write(self.style.ERROR(f'Unsupported file format: {file_path}'))
    def import_csv(self, file_path):
        with open(file_path, 'r') as f:
            count=0
            reader = csv.reader(f)
            header_row = next(reader)  # Read header row
            # Skip header row if present
            if header_row[0] == 'poi_id':
                next(reader)  # Skip header row
            for row in reader:
                if count == 100:
                    break
  
                # Extract data from each row
                poi_id = row[0]
                poi_name = row[1]
                poi_category = row[2]
                poi_latitude = float(row[3])
                poi_longitude = float(row[4])
                poi_ratings_string = row[5]  # Store ratings string initially
                poi_ratings = [float(x) for x in poi_ratings_string.strip('{}').split(',')]
                # Calculate average rating (adapt if needed for different calculations)
    
                # Create or update POI object (replace with your saving logic)
                poi = PoI.objects.create(
                    poi_id=poi_id,
                    poi_name=poi_name,
                    poi_category=poi_category,
                    poi_latitude=poi_latitude,
                    poi_longitude=poi_longitude,
                    poi_ratings=poi_ratings,  # Store the calculated average rating
                )
                count+=1
    def import_json(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            for entry in data:
                PoI.objects.create(
                    poi_id=entry['id'],
                    poi_name=entry['name'],
                    poi_category=entry['category'],
                    poi_latitude=entry['coordinates']['latitude'],
                    poi_longitude=entry['coordinates']['longitude'],
                    poi_ratings=entry['ratings']
                )
    def import_xml(self, file_path):
            with open(file_path, "r") as f:
                data = f.read()
            soup = BeautifulSoup(data, "xml")
            records = soup.find_all("DATA_RECORD")  # Assuming "DATA_RECORD" is the parent element
            for record in records:
                    poi_id = record.find("pid").text.strip()
                    poi_name = record.find("pname").text.strip()
                    poi_category = record.find("pcategory").text.strip()
                    poi_latitude = float(record.find("platitude").text.strip())
                    poi_longitude = float(record.find("plongitude").text.strip())
                    poi_ratings_string = record.find("pratings").text.strip()
                    # Process `poi_ratings_string` based on your requirements (e.g., split, convert to numbers)
                    poi_ratings = [float(rating) for rating in poi_ratings_string.split(",")]
                    # Use your data to create or update POI and ratings (replace placeholders)
                    poi = PoI.objects.create(
                        poi_id=poi_id,
                        poi_name=poi_name,
                        poi_category=poi_category,
                        poi_latitude=poi_latitude,
                        poi_longitude=poi_longitude,
                        poi_ratings=poi_ratings,  # Store the list of ratings
                    )