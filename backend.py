import csv
import os
import random

archive = 'recetas.csv'

class recipe:
    def __init__(self, id_receta, cooking_time, recipe_name, recipe_degrees):
        self.id = id_receta
        self.time = cooking_time
        self.name = recipe_name
        self.degrees = recipe_degrees 
        self.fdegrees = self.fahrenheit_converter() 
        
    def fahrenheit_converter(self):
        return round(self.degrees * 1.8 + 32)
    
    def row_converter(self):
        return [self.id, self.name, self.time, self.degrees, self.fdegrees]

class recipe_manager:
    def __init__(self, archive):
        self.archive = archive
        self._initialize_csv()
    
    def _initialize_csv(self):
        if not os.path.exists(self.archive):
            with open(self.archive, 'w', newline='') as f:
                csv.writer(f).writerow(['ID', 'Nombre', 'Tiempo (min)', 'Temp. (C)', 'Temp. (F)'])
    
    def get_last_id(self):
        try:
            with open(self.archive, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)
                return int(rows[-1][0]) if len(rows) > 1 else 0
        except (FileNotFoundError, IndexError, ValueError):
            return 0
        
    def save_recipe(self, recipe):
        with open(self.archive, 'a', newline='') as f:
            csv.writer(f).writerow(recipe.row_converter())
        
    def id_by_recipe(self, id_buscado):
        with open(self.archive, 'r') as f:
            for row in csv.reader(f):
                if row and row[0] == str(id_buscado):
                    return row
        return None
    
    def all_recipes(self):
        if not os.path.exists(self.archive):
            return []
        with open(self.archive, 'r') as f:
            return list(csv.reader(f))[1:]
    
    def make_recipe(self, name):
        return recipe(
            id_receta=self.get_last_id() + 1,
            cooking_time=random.randint(15, 90),
            recipe_name=name,
            recipe_degrees=random.randint(120, 220))