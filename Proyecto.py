import requests
import datetime
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def ajustar_fecha_bisiesta(fecha, anios_atras):
    fecha_original = datetime.datetime.strptime(fecha, "%Y-%m-%d")
    anio_destino = fecha_original.year - anios_atras
    if fecha_original.month == 2 and fecha_original.day == 29 and not es_bisiesto(anio_destino):
        return datetime.date(anio_destino, 2, 28).strftime("%Y-%m-%d")
    return fecha_original.replace(year=anio_destino).strftime("%Y-%m-%d")

def obtener_clima(ciudad, fecha):
    if not API_KEY:
        return "❌ Falta la API_KEY"
    url = f"{BASE_URL}/{ciudad}/{fecha}?unitGroup=metric&key={API_KEY}&include=days&contentType=json"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        datos = resp.json()
        return datos["days"][0] if "days" in datos else None
    except:
        return None

def comparar_clima(ciudad, fecha, anios):
    try:
        anios = int(anios)
    except ValueError:
        return "❌ El número de años debe ser un valor entero."

    try:
        clima_actual = obtener_clima(ciudad, fecha)
        fecha_pasada = ajustar_fecha_bisiesta(fecha, anios)
        clima_pasado = obtener_clima(ciudad, fecha_pasada)

        if clima_actual and clima_pasado:
            diferencia = clima_actual['temp'] - clima_pasado['temp']
            return (
                f"🌍 Ciudad: {ciudad}\n"
                f"📅 Fecha actual: {fecha} — {clima_actual['temp']}°C | {clima_actual['conditions']}\n"
                f"📅 Hace {anios} años ({fecha_pasada}): {clima_pasado['temp']}°C | {clima_pasado['conditions']}\n"
                f"🔺 Diferencia: {diferencia:.1f}°C"
            )
        else:
            return "⚠️ No se pudo obtener la información meteorológica. Verifica la ciudad o la fecha."
    except Exception as e:
        return f"❗ Error inesperado: {str(e)}"


# Si se está ejecutando en un entorno Gradio, lanzamos la interfaz web
try:
    import gradio as gr

    # Interfaz con Gradio
    def gradio_interface(ciudad, fecha, anios_atras):
        return comparar_clima(ciudad, fecha, anios_atras)

    demo = gr.Interface(
        fn=gradio_interface,
        inputs=[
            gr.Textbox(label="Ciudad", placeholder="Ej: Madrid"),
            gr.Textbox(label="Fecha (YYYY-MM-DD)", value=datetime.date.today().strftime("%Y-%m-%d")),
            gr.Textbox(label="Años atrás", value="1"),
        ],
        outputs="text",
        title="🌤️ Comparador de Clima Histórico",
        description="Compara el clima actual con el de la misma fecha hace X años usando Visual Crossing API.",
    )

    if __name__ == "__main__":
        demo.launch()

except ImportError:
    # Si no está usando Gradio, ejecutamos en la terminal
    if __name__ == "__main__":
        ciudad = input("Ingrese la ciudad: ")
        fecha = input("Ingrese la fecha (YYYY-MM-DD) o presione Enter para usar la de hoy: ") or datetime.date.today().strftime("%Y-%m-%d")
        anios_atras = input("¿Cuántos años atrás quieres comparar? (Por defecto 1 año): ") or "1"
        print(comparar_clima(ciudad, fecha, anios_atras))
