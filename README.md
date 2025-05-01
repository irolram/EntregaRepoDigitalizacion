# Comparador Histórico de Clima

Este proyecto es una herramienta en Python que permite comparar el clima actual de una ciudad con el clima registrado en la misma fecha hace una cierta cantidad de años. Se basa en la API de [Visual Crossing Weather](https://www.visualcrossing.com/) para obtener datos meteorológicos precisos tanto del presente como del pasado.

---

## Motivación

El cambio climático es una de las principales preocupaciones de nuestro tiempo, y muchas personas —desde ciudadanos comunes hasta investigadores— están interesadas en observar cómo han cambiado las temperaturas y las condiciones meteorológicas a lo largo de los años. Este proyecto nace con la idea de ofrecer una herramienta simple, educativa y útil que permita:

- **Analizar tendencias climáticas locales**: ¿Está realmente haciendo más calor hoy que hace cinco años en tu ciudad?
- **Despertar la curiosidad científica** en estudiantes o aficionados a la meteorología.
- **Ofrecer datos para proyectos de análisis o visualización**, sin necesidad de construir una infraestructura compleja.
- **Proveer un recurso ligero y portable**, fácil de usar en terminales, entornos educativos o incluso como parte de otros sistemas más grandes.

Con esta herramienta puedes comprobar, por ejemplo, si el 1 de mayo de 2025 en Madrid ha sido más cálido que el 1 de mayo de 2015, y cuánta diferencia hay en temperatura y condiciones generales (nublado, soleado, lluvioso, etc.).

---

## Tecnologías utilizadas

- **Python 3.7+**
- **requests** – Para realizar solicitudes HTTP a la API de Visual Crossing.
- **python-dotenv** – Para gestionar variables de entorno de forma segura.
- **Visual Crossing Weather API** – Fuente de los datos meteorológicos históricos y actuales.

---

## Instalación y configuración

### 1. Clona el repositorio:

bash
git clone https://github.com/tuusuario/comparador-clima.git
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


