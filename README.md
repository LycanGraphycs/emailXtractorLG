📧 emailXtractorLG
![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
emailXtractorLG es una herramienta en Python para extraer y consolidar información de archivos de correo electrónico en formato `.eml`. Procesa una carpeta completa de correos, extrae la fecha, el asunto y el cuerpo de cada mensaje, y genera un archivo Excel listo para analizar.
---
🚀 ¿Qué hace?
📂 Escanea automáticamente una carpeta en busca de archivos `.eml`
📋 Extrae los campos: Fecha, Asunto y Cuerpo de cada correo
🧹 Limpia caracteres inválidos (saltos de línea, espacios sobrantes, etc.)
📊 Consolida toda la información en un archivo Excel (`correos_eml.xlsx`)
✅ Soporta correos en formato `text/plain` y `multipart`
---
📋 Requisitos
Python 3.7 o superior
Las siguientes librerías:
```
pandas
openpyxl
```
---
⚙️ Instalación
Clona el repositorio:
```bash
git clone https://github.com/LycanGraphycs/emailXtractorLG.git
cd emailXtractorLG
```
Instala las dependencias:
```bash
pip install pandas openpyxl
```
---
▶️ Uso
Coloca todos tus archivos `.eml` en la misma carpeta donde se encuentra el script `xtractorLg.py`.
Ejecuta el script:
```bash
python xtractorLg.py
```
Al finalizar, encontrarás el archivo `correos_eml.xlsx` en la misma carpeta con toda la información extraída.
---
📁 Estructura del proyecto
```
emailXtractorLG/
│
├── xtractorLg.py        # Script principal
├── correos_eml.xlsx     # Archivo de salida generado (se crea al ejecutar)
└── README.md
```
---
📊 Ejemplo de salida
Fecha	Asunto	Cuerpo
Mon, 10 Apr 2024 08:30:00	Reunión de equipo	Buenos días, les recuerdo que...
Tue, 11 Apr 2024 14:15:00	Informe mensual	Adjunto el informe del mes de...
---
🛠️ Tecnologías utilizadas
Librería	Uso
`email` / `BytesParser`	Parseo de archivos `.eml`
`re`	Limpieza de campos con expresiones regulares
`os`	Recorrido del sistema de archivos
`pandas`	Construcción y exportación del DataFrame
`openpyxl`	Escritura del archivo Excel
---
⚠️ Notas
El script procesa los correos desde el directorio actual (`./`). Puedes modificar la variable `eml_folder` dentro del script para apuntar a otra ruta.
Si un correo es `multipart`, se extrae únicamente la parte `text/plain`.
Los campos vacíos o nulos en el remitente se reemplazan por `"Remitente desconocido"`.
---
📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
---
👤 Autor
Andres Mauricio M. Garavito  
🐺 LycanGraphycs
---
🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto:
Haz un fork del repositorio
Crea una rama con tu feature: `git checkout -b feature/mi-mejora`
Haz commit de tus cambios: `git commit -m 'Agrego mi mejora'`
Haz push a la rama: `git push origin feature/mi-mejora`
Abre un Pull Request
---
Hecho con ❤️ en Colombia 🇨🇴
