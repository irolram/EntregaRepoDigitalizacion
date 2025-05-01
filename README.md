# Comparador Histórico de Clima

This project is a Python-based tool that allows you to compare the current weather in a city with the weather recorded on the same date a certain number of years ago. It uses the Visual Crossing Weather API to retrieve accurate weather data from both the present and the past.

## Motivation
Climate change is one of the major concerns of our time, and many people — from everyday citizens to researchers — are interested in seeing how temperatures and weather conditions have evolved over the years. This project was created with the idea of offering a simple, educational, and useful tool that allows users to:

Analyze local climate trends: Is it really warmer today than it was five years ago in your city?

Spark scientific curiosity in students or weather enthusiasts.

Provide data for analysis or visualization projects, without the need to build a complex infrastructure.

Offer a lightweight and portable resource, easy to use in terminals, educational settings, or even as part of larger systems.

With this tool, you can easily check, for example, whether May 1st, 2025 in Madrid was warmer than May 1st, 2015, and how much the temperature and general weather conditions (cloudy, sunny, rainy, etc.) differed.

## Technologies Used
Python 3.7+

requests – For making HTTP requests to the Visual Crossing API.

python-dotenv – For securely managing environment variables.

Visual Crossing Weather API – The source for historical and current weather data.
---

## Instalación y configuración

### 1. Clone the repository:


git clone https://github.com/irolram/EntregaRepoDigitalizacion.git
cd comparador-clima

## 2. Instala las dependencias necesarias:
pip install -r requirements.txt

## 3. Ejecuta el script:

python clima.py

# USO

Al ejecutar el script, se solicitarán:
Ciudad (por ejemplo: Madrid, Buenos Aires, Monesterio)
Fecha en formato YYYY-MM-DD (puedes dejarlo en blanco para usar la fecha de hoy)
Cantidad de años atrás a comparar (por defecto es 1)

Ejemplo de ejecución:

Ingrese la ciudad: Buenos Aires
Ingrese la fecha (YYYY-MM-DD) o presione Enter para usar la de hoy: 2024-12-25
¿Cuántos años atrás quieres comparar? (Por defecto 1 año): 10

Ciudad: Buenos Aires | Fecha: 2024-12-25
Temperatura actual (2024-12-25): 32.1°C | Clear
Hace 10 años (2014-12-25): 29.8°C | Partly Cloudy
Diferencia de temperatura: 2.3°C


