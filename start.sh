#!/bin/bash
# Activar entorno virtual
source venv/bin/activate

# Instalar nuevas dependencias si faltan (FastAPI, uvicorn, etc)
pip install -r requirements.txt

# Iniciar el servidor
echo "Iniciando Servidor Web en http://localhost:8000"
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
