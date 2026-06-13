# SyncDub AI Case Study

## Overview

SyncDub AI is a local-first video translation and dubbing workflow. It takes a source video, extracts the audio, transcribes speech, detects speakers, translates each segment, generates synthetic voiceovers, and assembles a dubbed video while preserving background music.

The project was built as a practical AI automation tool rather than a simple model demo. The main goal is to give users control over every segment before final rendering.

## Problem

Manual video dubbing is slow and repetitive. A typical workflow requires transcription, translation, speaker review, voice recording, audio cleanup, timing adjustments, and final video assembly. Most AI demos automate only one piece of that process.

## Solution

SyncDub AI combines the full workflow in one dashboard:

- Upload a local video or import from YouTube.
- Extract and separate vocals/background audio.
- Transcribe speech with Whisper.
- Detect speakers with pyannote.
- Translate segment by segment through a local Ollama model.
- Edit translations before generating audio.
- Select or regenerate voices per segment.
- Assemble the final dubbed video with FFmpeg.

## Architecture

```txt
Video / YouTube URL
        |
        v
FastAPI backend
        |
        +--> FFmpeg audio extraction
        +--> Demucs vocal/background separation
        +--> faster-whisper transcription
        +--> pyannote speaker diarization
        +--> Ollama translation
        +--> Kokoro TTS generation
        +--> FFmpeg final video assembly
        |
        v
Web dashboard editor
```

## Technical Highlights

- Segment-level editor for translation review and audio regeneration.
- GPU memory fallback for long-running transcription and TTS tasks.
- Hybrid synchronization strategy that adjusts generated audio and video timing.
- Local-first architecture for privacy and lower API dependency.
- Simple FastAPI endpoints that expose each pipeline stage independently.

## Limitations

This is a local prototype intended for controlled use, demos, and portfolio review. Project state is stored in memory while the server is running, and heavy AI dependencies must be installed locally.

## Stack

Python, FastAPI, FFmpeg, faster-whisper, pyannote.audio, Demucs, Kokoro TTS, Ollama, HTML, CSS, and vanilla JavaScript.
