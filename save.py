import json
import os

class Saver:
    def __init__(self, file):
        self.file = file
        
    def save(self, data):
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)
   
    def read(self):
        # Vérifie si le fichier existe et n'est pas vide avant de le lire
        if not os.path.exists(self.file) or os.stat(self.file).st_size == 0:
            return []

        # Lit le contenu du fichier en utilisant directement json.load
        with open(self.file, "r") as file:
            return json.load(file)