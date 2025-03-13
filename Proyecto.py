import requests
import datetime
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def es_bisiesto(anio):
    """Devuelve True si el año es bisiesto, False si no lo es."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def ajustar_fecha_bisiesta(fecha, anios_atras):
    """Ajusta la fecha si el año de destino no es bisiesto y el día es 29 de febrero."""
    fecha_original = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    anio_destino = fecha_original.year - anios_atras

    # Si la fecha original es 29 de febrero y el año de destino no es bisiesto, ajustamos a 28 de febrero
    if fecha_original.month == 2 and fecha_original.day == 29 and not es_bisiesto(anio_destino):
        fecha_ajustada = datetime.date(anio_destino, 2, 28)
    else:
        fecha_ajustada = fecha_original.replace(year=anio_destino)

    return fecha_ajustada.strftime("%Y-%m-%d")

def obtener_clima(ciudad, fecha):
    """Obtiene el clima de una ciudad en una fecha específica usando Visual Crossing."""
    if not API_KEY or not BASE_URL:
        print(" Error: No se encontró la API Key o la BASE_URL. Verifica tu archivo .env")
        return None

    url = f"{BASE_URL}/{ciudad}/{fecha}?unitGroup=metric&key={API_KEY}&include=days&contentType=json"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si el código de estado es 4xx o 5xx
        datos = respuesta.json()
        if "days" in datos and datos["days"]:
            return datos["days"][0]  # Retorna solo la info del día solicitado
        else:
            print(f"⚠️ No hay datos disponibles para {fecha}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f" Error al obtener los datos: {e}")
        return None


def comparar_clima(ciudad, fecha, anios_atras):
    """Compara el clima de la fecha dada con la misma fecha en años anteriores, manejando años bisiestos."""
    clima_actual = obtener_clima(ciudad, fecha)
    fecha_pasada = ajustar_fecha_bisiesta(fecha, anios_atras)
    clima_pasado = obtener_clima(ciudad, fecha_pasada)

    if clima_actual and clima_pasado:
        print(f"\n Ciudad: {ciudad} |  Fecha: {fecha}")
        print(f" Temperatura actual ({fecha}): {clima_actual['temp']}°C | {clima_actual['conditions']}")
        print(f" Hace {anios_atras} años ({fecha_pasada}): {clima_pasado['temp']}°C | {clima_pasado['conditions']}")
        print(f" Diferencia de temperatura: {clima_actual['temp'] - clima_pasado['temp']}°C")
    else:
        print("⚠️ No se pudieron obtener los datos para la comparación.")

# --- Ejecución ---
if __name__ == "__main__":
    ciudad = input(" Ingrese la ciudad: ") or "monesterio"
    fecha = input(" Ingrese la fecha (YYYY-MM-DD) o presione Enter para usar la de hoy: ") or datetime.date.today().strftime("%Y-%m-%d")
    anios_atras = input(" ¿Cuántos años atrás quieres comparar? (Por defecto 1 año): ") or "1"

    try:
        anios_atras = int(anios_atras)
        comparar_clima(ciudad, fecha, anios_atras)
    except ValueError:
        print(" Error: La cantidad de años debe ser un número entero.")
