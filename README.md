# 🎙️ Doblador IA (AI Video Dubbing App)

Una potente aplicación web de código abierto para la traducción y el doblaje automático de videos.

Diseñada con un backend asíncrono en **FastAPI** y una elegante interfaz de usuario "Dashboard" (HTML/CSS Vanilla con Glassmorphism), esta herramienta permite: descargar videos de YouTube o subir tus propios archivos locales, transcribirlos al vuelo, traducirlos, generar clones vocales ultra-realistas aislados por locutor, y ensamblarlos magistralmente de vuelta en un archivo de video final sin perder la música de fondo.

---

## ✨ Características Principales

*   🚀 **Integración Directa con YouTube:** Pega el link de cualquier video y el sistema extraerá automáticamente la mejor calidad visual y auditiva sincronizada (mediante `yt-dlp`). Cuenta con un ingenioso sistema de caché local.
*   🎤 **Transcripción Inteligente:** Emplea `faster-whisper` nativo para reconocer con enorme precisión el audio original del video.
*   👥 **Diarización de Hablantes:** Capacidad de aislar matemáticamente y separar automáticamente quién está hablando gracias a `Pyannote.audio` para asignarle voces distintas de manera inteligente.
*   🎸 **Aislamiento Acústico (Demucs):** Separa los diálogos humanos de la música de fondo y los efectos de sonido, manteniendo la banda sonora original totalmente intacta para el video doblado final.
*   🌍 **Traducción Neural Avanzada (Hunyuan MT):** Integra el prestigioso y galardonado modelo de Machine Translation de Tencent (`demonbyron/HY-MT1.5-7B`) vía **Ollama**, aplicando las directrices técnicas oficiales para un doblaje corto, idiomático y programado para **no traducir marcas ni nombres propios**.
*   🗣️ **Catálogo Multi-Idioma Kokoro TTS:** Clonación y síntesis de voz líder en la industria con [Kokoro v1.0]. Más de 30 voces oficiales incluidas en múltiples idiomas (Español, Inglés, Japonés, Francés, Mandarín, etc.) calculadas de manera ultrarrápida por GPU.
*   🛠️ **Editor de Segmentos Interactivo ("Timeline Visual"):** Interfaz de navegador moderna que incluye un flujo de trabajo granular donde puedes:
    *   Editar el texto original y la traducción de cada línea individualmente en la tabla.
    *   Cambiar la voz de un personaje al vuelo desde el menú de opciones (Ej. asignar a "Santa" el rol del orador principal).
    *   **Regenerar y reproducir audios** de forma suelta (por bloque de texto) a merced, sin tener que renderizar el video entero.
    *   Visualizar la duración y ubicación de cada locutor en una **línea de tiempo tipo "CapCut"** interactiva.
*   🎬 **Mix & Ensamble Inteligente (FFmpeg):** Fusión precisa milisegundo a milisegundo entre la pista musical original (`no_vocals`) y las nuevas voces. Incorpora un avanzado sistema de **Sincronía Híbrida** de múltiples capas: acelera levemente audios extensos de forma dinámica y, si es necesario, aplica un *time-stretching* adaptativo a los segmentos de video para lograr un ajuste de tiempos perfecto sin cortar las líneas de voz.

---

## ⚙️ Tecnologías Utilizadas

- **Servidor Local LLM**: Ollama (`demonbyron/HY-MT1.5-7B`)
- **Backend core**: Python 3.12, FastAPI, Uvicorn, BackgroundTasks
- **Machine Learning & Audio**: `faster-whisper`, `pyannote.audio`, `kokoro`, `demucs`, `torch`, `soundfile`
- **Renderizado Video**: FFmpeg, subprocess
- **Frontend App**: HTML5, Vanilla JavaScript, CSS3 (Con utilidades Asíncronas)

---

## 🚀 Instalación y Uso Rápido

### 1. Clonar el repositorio
```bash
git clone https://github.com/YourUsername/traductor_IA.git
cd traductor_IA
```

### 2. Dependencias de Sistema
Asegúrate de contar con la versión **completa** de `ffmpeg` instalada globalmente (con soporte para codificadores propietarios como `libx264`). Versiones limitadas como `ffmpeg-free` causarán errores en la sincronía híbrida de video.

```bash
# GNU/Linux (Fedora) - ¡Requiere habilitar RPM Fusion primero!
sudo dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf swap ffmpeg-free ffmpeg --allowerasing

# Debian/Ubuntu (Generalmente ya incluye los codecs necesarios)
sudo apt-get install ffmpeg
```
*(Nota: Necesitarás tener `ollama` instalado y el modelo de lenguaje de traducción corriendo activamente en el puerto 11434).*

### 3. Entorno de Python
Ejecuta el script de inicio o crea un entorno aislado manualmente:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Lanzar la Aplicación
Corre el script rápido incluido en la raíz de tu proyecto:
```bash
chmod +x start.sh
./start.sh
```
O levanta el servidor uvicorn manualmente:
```bash
uvicorn app:app --reload
```

Una vez que leas *Application startup complete*, visita **`http://localhost:8000`** en tu navegador para empezar a crear magia.

---

## 🤝 Contribuciones
¡Las *Pull Requests* son totalmente bienvenidas! Siéntete libre de reportar *Issues* si encuentras algún bug, comportamiento anómalo en la regeneración de audios, o si tienes una idea genial para seguir mejorando esta herramienta.

## 📄 Licencia
Este proyecto es distribuido como código abierto. Consulta el archivo de licencia para más detalles sobre garantías y responsabilidades operativas.
