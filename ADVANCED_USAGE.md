# ⚙️ Advanced Usage & Configuration

This guide provides advanced users with instructions on how to modify internal code parameters to adjust the app's behavior, optimize performance, or tweak machine learning models to fit their specific needs.

## 1. Changing the Transcription Model (Whisper)

By default, the application is set up to provide the best balance between accuracy and performance. If you want to change the Whisper model size (e.g., from `large-v3` to `medium` or `small` to save RAM/VRAM), you need to modify the `traductor.py` file.

Open `traductor.py` and locate the `transcribe_audio` method (around line 115). Change the model name in both the `cuda` and `cpu` fallback blocks:

```python
model = WhisperModel(
    "medium", # Change this string to "small", "medium", or "large-v3"
    device="cuda", 
    compute_type="int8_float16",
    cpu_threads=4,
    num_workers=1
)
```

**Recommended Models:**
- `small` / `medium`: Excellent for English and Spanish, very fast.
- `large-v3`: Highly recommended for Asian languages (e.g., Chinese, Japanese) or fast-paced audio to prevent transcription hallucinations.

## 2. Adjusting Whisper Parameters

If you notice the AI getting stuck repeating phrases (hallucinations) during extremely fast speech or silent periods, ensure the following parameters are set inside the `.transcribe()` call in `traductor.py`:

```python
segments, _ = model.transcribe(
    self.audio_track_orig,
    beam_size=10, # Increase to 10 for better accuracy (default usually 5)
    vad_filter=True, # Keeps silence out of the transcription
    language=self.source_language,
    condition_on_previous_text=False, # CRITICAL: Set to False to prevent repeating loops
    temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0] # Variable fallback temperatures
)
```

## 3. Changing the Translation LLM

The project uses Ollama with the `demonbyron/HY-MT1.5-7B` model by default. To change this to another local model (e.g., `llama3` or `qwen`), locate the `translate_text` method in `traductor.py` (around line 242) and update the payload model name:

```python
payload = {
    "model": "your_new_model_name", # Update here
    "prompt": prompt,
    "stream": False,
    # ...
```

*Note on Translations:* Translating from English or Chinese to Spanish yields great results due to the model's training. Trying complex bidirectional translations (like Spanish to Chinese) hasn't been as extensively tested in this pipeline and may require prompt tweaking to enforce correct output formatting without metadata.

## 4. Troubleshooting & Known Limitations

- **VRAM Limitations:** The system includes internal try/except blocks that automatically flush VRAM (`self.clear_vram()`) and switch to CPU processing if your GPU runs out of memory (`torch.cuda.OutOfMemoryError`). This means generation might suddenly become slower for a specific segment, but it won't crash the entire app. You can monitor this in your terminal logs.
- **Pyannote Tokens:** To detect multiple speakers, `pyannote.audio` requires an active HuggingFace token. Ensure your `HF_TOKEN` environment variable is correctly set in your terminal or `.env` file before executing `start.sh`.
