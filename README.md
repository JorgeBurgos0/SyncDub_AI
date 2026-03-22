# 🎙️ Traductor IA (AI Video Dubbing)

Una aplicación que automatiza el proceso de traducción y doblaje de videos. Utiliza un backend asíncrono en FastAPI y un panel web para transcribir, traducir, generar voces y ensamblar el video final conservando la música de fondo original.

## Características

- **Integración con YouTube**: Descarga y procesa videos mediante `yt-dlp`.
- **Transcripción**: Reconocimiento de audio con `faster-whisper`.
- **Diarización de Hablantes**: Identifica y separa a los diferentes locutores con `pyannote.audio`.
- **Separación de Audio**: Aísla las voces de la música de fondo o SFX usando `demucs`.
- **Traducción Neuronal**: Traducción de textos utilizando el modelo `demonbyron/HY-MT1.5-7B` a través de Ollama.
- **Síntesis de Voz (TTS)**: Generación de voces en múltiples idiomas con `kokoro`.
- **Editor Interactivo**: Interfaz web para editar traducciones, cambiar voces y regenerar audios por segmento.
- **Ensamblaje de Video**: Mezcla de audio y sincronización híbrida (audio/video) usando FFmpeg.

## Tecnologías

- **Backend**: Python 3.12, FastAPI, Uvicorn
- **LLM Local**: Ollama
- **Audio y Machine Learning**: `faster-whisper`, `pyannote.audio`, `kokoro`, `demucs`, `torch`, `soundfile`
- **Procesamiento de Video**: FFmpeg
- **Frontend**: HTML5, Vanilla JavaScript, CSS3

## Instalación

⚠️ **Importante**: Es necesario tener instalada la versión completa de `ffmpeg` (con soporte para `libx264`), tener `ollama` instalado y el modelo de traducción en ejecución.

```bash
git clone https://github.com/YourUsername/traductor_IA.git
cd traductor_IA

# Crear y activar un entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt
```

### Dependencias del Sistema (FFmpeg)
**Fedora** (Requiere habilitar RPM Fusion):
```bash
sudo dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf swap ffmpeg-free ffmpeg --allowerasing
```

**Debian/Ubuntu**:
```bash
sudo apt-get install ffmpeg
```

## Uso

Para iniciar la aplicación, ejecuta el script de arranque incluido:
```bash
chmod +x start.sh
./start.sh
```

O levanta el servidor manualmente:
```bash
uvicorn app:app --reload
```
Una vez iniciado, abre tu navegador y dirígete a `http://localhost:8000`.

## Contribuciones

Las contribuciones son bienvenidas. Puedes abrir un *Issue* para reportar errores o errores de sincronización, o enviar un *Pull Request* si deseas proponer mejoras al código.

## Licencia

Este proyecto está bajo la licencia **GNU Affero General Public License v3.0 (AGPLv3)**. Consulta el archivo `LICENSE` para más detalles.

## Descargo de Responsabilidad

Este proyecto tiene fines estrictamente educativos. El autor no se hace responsable por el mal uso de la información, el código provisto, o las voces generadas. Úselo bajo su propio riesgo.
