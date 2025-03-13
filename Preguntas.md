## 1️ ¿Cómo se gestionan los datos desde su generación hasta su eliminación?

- **Generación:** Los datos climáticos se obtienen desde la API de Visual Crossing en formato JSON.
- **Procesamiento:** Se extrae la información relevante (temperatura y condiciones climáticas).
- **Almacenamiento temporal:** Los datos solo existen en memoria durante la ejecución; no se almacenan de manera persistente.
- **Eliminación:** Al no usar una base de datos, los datos desaparecen una vez que el programa finaliza.

## 2️ ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?

- **Validaciones previas:** Se verifica la existencia de `API_KEY` y `BASE_URL` antes de hacer peticiones.
- **Manejo de errores:** Se usa `try-except` para capturar errores en la solicitud HTTP.
- **Ajuste de fechas bisiestas:** Se corrige la fecha en caso de años no bisiestos para evitar errores.

## 3️ Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?

- **Persistencia:** Agregar una base de datos como PostgreSQL para almacenar datos históricos.

# ☁️ Seguridad y Almacenamiento en la Nube

## 4 Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?

- **Autenticación y autorización:** Uso de credenciales seguras (`API_KEY`) almacenadas en variables de entorno (`.env`).
- **Copias de seguridad:** Implementación de backups automáticos en servicios como Google Cloud Storage.
- **Redundancia y escalabilidad:** Implementación de servidores distribuidos para evitar pérdida de datos ante fallos.

## 5 ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?

La alternativa que usaria seria por ejemplo una base de datos como PosgreSQL ya que es una SQL potente y confiable, el contra es la mayor complejidad de configuración.
Otra alternativa seria con MongoDB que es flexible y escalable, el contra es que no es ideal para datos relacionales

## 6 Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?

Para una integración en la nube en versiones futuras, podría:  
- **Almacenar datos históricos del clima** en una base de datos en AWS RDS o Firebase Firestore.  
- **Automatizar backups** en Google Cloud Storage o AWS S3.  


## 7 ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?

- Uso de **variables de entorno** (`.env`) para ocultar la `API_KEY` y la `BASE_URL`, evitando que sean expuestas en el código.
- **Manejo de excepciones** con `try-except` en las solicitudes HTTP para evitar que errores inesperados afecten la ejecución.
- La API utilizada (Visual Crossing) **requiere conexiones seguras (HTTPS)** para evitar interceptación de datos en tránsito.



## 8 ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?

El código actual no implementa autenticación de usuarios ni almacenamiento de datos sensibles, por lo que no está afectado por normativas como GDPR. Sin embargo, si en el futuro se gestionan datos personales, habría que añadir medidas de seguridad adicionales como cifrado, autenticación y control de acceso.

## 9 Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?

**Exposición de credenciales** en el código , para solucionarlas usaria `.env` (ya está implementado), gestionar secretos con AWS Secrets Manager o Vault. |
**Intercepción de datos en tránsito** lo arreglaria manteniendo el uso de HTTPS 

## 1️0 ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?

- **Agricultura:** Permite comparar condiciones climáticas pasadas y actuales, ayudando en la planificación de cultivos.  
- **Construcción:** Mejora la planificación de obras al prever condiciones climáticas adversas.  
- **Logística y transporte:** Facilita la toma de decisiones para reducir riesgos climáticos en rutas de distribución.  

## 11 ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?

**Análisis predictivo:** Comparar temperaturas pasadas con las actuales ayuda a prever tendencias climáticas.  
**Reducción de riesgos:** Sectores como la aviación o logística pueden evitar condiciones adversas con información histórica.  

## 12 Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?

**Cambio climático:** Investigadores podrían usarlo para estudiar variaciones de temperatura a lo largo de los años.  

## 1️3 ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

El software podría servir como un **puente entre IT (Tecnología de la Información) y OT (Tecnología Operacional)** en industrias que dependen de datos meteorológicos, permitiendo que sistemas operativos tomen decisiones basadas en información en tiempo real.  

- **Optimización de mantenimiento:** Usar patrones climáticos históricos para programar **mantenimiento preventivo** en maquinaria expuesta a condiciones extremas.  
- **Gestión de energía:** Ajustar el uso de **energías renovables** en función de la previsión del clima.  

## 14 ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?

**Agricultura de precisión:** Ajustar riego y fertilización según variaciones climáticas.  
**Logística y transporte:** Optimizar rutas considerando condiciones climáticas pasadas y futuras.  

## 15 Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

Si bien el software no está diseñado específicamente para IT/OT, podría integrarse con:
- **Sistemas ERP** para mejorar la toma de decisiones basada en el clima.  
- **Machine Learning**, entrenando modelos con datos climáticos históricos para predicciones más precisas.  

## 1️6 ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

**Computación en la Nube** Uso de API meteorológica (Visual Crossing) para obtener datos climáticos. |
**IoT (Internet de las Cosas)** Integración con sensores meteorológicos para datos en tiempo real. |
**Ciberseguridad** | Protección de credenciales con `.env`, uso de HTTPS para API segura. |

## 17 ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?

**Mayor precisión:** Machine Learning podría predecir tendencias climáticas con mayor exactitud.  
**Automatización:** Integración con IoT para recopilar datos en tiempo real sin intervención manual.  

## 18 Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?

Si bien el software es básico, se podrían implementar **THD** como:
- **Machine Learning** para predecir variaciones climáticas futuras.  
- **IoT** con estaciones meteorológicas conectadas para recopilar datos en tiempo real.  
- **Big Data** para analizar patrones climáticos en múltiples ciudades y mejorar la toma de decisiones.  

