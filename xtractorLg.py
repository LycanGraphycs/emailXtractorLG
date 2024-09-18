import os
import re
import email
import pandas as pd
from email import policy
from email.parser import BytesParser

# Ruta de la carpeta donde están los archivos EML
eml_folder = './'

# Lista para almacenar los datos de los correos
correos = []


# Función para limpiar campos que contengan saltos de línea o caracteres inválidos
def limpiar_campo(campo):
    if campo:
        # Elimina saltos de línea y retornos de carro
        campo_limpio = re.sub(r'[\r\n]', '', campo)
        return campo_limpio.strip()  # Elimina espacios al inicio y al final
    return "Remitente desconocido"  # Si el campo es None o vacío


# Itera sobre cada archivo EML en la carpeta
for eml_file in os.listdir(eml_folder):
    if eml_file.endswith(".eml"):
        # Abre el archivo EML
        with open(os.path.join(eml_folder, eml_file), 'rb') as f:
            # Analiza el archivo EML
            msg = BytesParser(policy=policy.default).parse(f)

            # Inicializa un diccionario para almacenar los datos del correo
            correo_data = {}

            # Extrae la fecha, asunto y remitente (usando msg['raw'] para evitar el procesamiento de los encabezados)
            correo_data['Fecha'] = msg.get('Date')
            correo_data['Asunto'] = msg.get('Subject')



            # Extrae el cuerpo del correo (texto plano o HTML si no hay texto plano)
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        correo_data['Cuerpo'] = part.get_payload(decode=True).decode('utf-8', errors='replace')
                        break
            else:
                correo_data['Cuerpo'] = msg.get_payload(decode=True).decode('utf-8', errors='replace')

            # Agrega los datos del correo a la lista
            correos.append(correo_data)

# Convierte la lista de diccionarios a un DataFrame de pandas
df = pd.DataFrame(correos)

# Guarda el DataFrame en un archivo Excel
df.to_excel('correos_eml.xlsx', index=False)

print("Los correos han sido guardados en 'correos_eml.xlsx'")
