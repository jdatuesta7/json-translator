import json
from googletrans import Translator

# leer el archivo JSON
with open('en_example.json') as f:
    data = json.load(f)

# crear un objeto traductor
translator = Translator()

# traducir los valores y actualizar el diccionario
count = 0
for key in data:
    translated = translator.translate(data[key], dest='pt').text
    data[key] = translated
    count += 1
    percent = (count / len(data)) * 100
    print(f"Progreso: {percent:.2f}%")

# escribir el nuevo archivo JSON en portugués
with open('pt.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
