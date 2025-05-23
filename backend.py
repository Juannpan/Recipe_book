import csv
import os
import random
import math

class recipe:
    def __init__(self, id_receta, recipe_name, recipe_degrees):
        self.id = id_receta
        self.name = recipe_name
        self.time = self.generate_cooking_time() 
        self.degrees = recipe_degrees
        self.fdegrees = self.fahrenheit_converter()
        
    def generate_cooking_time(self):
        return random.randint(15, 90)
    
    def fahrenheit_converter(self):
        fahrenheit = self.degrees * 1.8 + 32
        return math.floor(fahrenheit) if fahrenheit - math.floor(fahrenheit) < 0.5 else math.ceil(fahrenheit)
    
    def to_row(self):
        return [self.id, self.name, self.time, self.degrees, self.fdegrees]

class recipe_manager:
    def __init__(self, filename):
        self.filename = filename
        self._initialize_file()
    
    def _initialize_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', 'Nombre', 'Tiempo (min)', 'Temp. (C)', 'Temp. (F)'])
    
    def get_last_id(self):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)[1:]  
                return int(rows[-1][0]) if rows else 0
        except (FileNotFoundError, IndexError, ValueError):
            return 0
    
    def save_recipe(self, receta):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(receta.to_row())
    
    def get_recipe_by_id(self, recipe_id):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == str(recipe_id):
                    return row
        return None
    
    def get_all_recipes(self):
        if not os.path.exists(self.filename):
            return []
        
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            return list(reader)[1:] 