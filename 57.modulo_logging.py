import logging

"""
  DEBUG      → Información detallada para desarrolladores
  INFO       → Información general del programa
  WARNING    → Algo inesperado pero no crítico
  ERROR      → Error que afecta una parte del sistema
  CRITICAL   → Error grave que puede detener el sistema
"""

"""
  %(asctime)s
  %(levelname)s
  %(message)s
  %(filename)s
  %(lineno)d
"""

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s - %(name)s ")

logging.info("La aplicación inició")
logging.error("Error al conectar a la base de datos")