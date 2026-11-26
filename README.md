# NEXUS - AI Assistant Pet Robot

Academic capstone starter implementation for SR University, Warangal (2026-2027).

This repository contains runnable starter code for the five project workstreams:
1. AI Brain & Voice
2. Vision AI
3. TFT Display & Emotion UI
4. Mobile Dashboard
5. Memory & Meeting AI

**Important:** This is a working foundation, not a claim that every advanced feature is complete. Face detection is not face recognition. Emotion labels are simple UI states, not reliable emotion inference. The meeting summarizer is extractive/basic and does not use a trained language model.

## Architecture

Camera/microphone/dashboard -> Python services -> MQTT (optional) -> ESP32 display/motor controller.
SQLite stores notes, conversation turns, and meeting transcripts.

## Requirements
- Python 3.10+ recommended
- Windows, Linux, or macOS
- Webcam and microphone for live camera/voice features
- Optional MQTT broker (e.g. Mosquitto) for robot-to-dashboard/ESP32 messaging
- ESP32 board and compatible TFT wiring for the display firmware

## Setup

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows; on macOS/Linux use: cp .env.example .env
python -m memory_meeting_ai.init_db
```

## Run the modules

Open separate terminals (activate the same virtual environment in each):

**1. Vision AI**
```bash
python -m vision_ai.main
```
Press `q` in the camera window to quit. Uses OpenCV's built-in HOG person detector and Haar face detector. Camera index can be changed with `CAMERA_INDEX` in `.env`.

**2. AI Brain & Voice**
```bash
python -m ai_voice.assistant
```
Text mode works without a microphone. Set `VOICE_MODE=true` to attempt microphone input. Speech recognition may require an internet connection depending on the installed recognizer/service. TTS requires audio output.

**3. Mobile dashboard**
```bash
python -m mobile_dashboard.app
```
Open `http://127.0.0.1:5000`. This is a local development dashboard; do not expose it publicly without authentication and security hardening.

**4. Memory & Meeting AI**
```bash
python -m memory_meeting_ai.cli
```
Follow the menu to save notes, list recent notes, or create a basic meeting summary from a text transcript.

**5. ESP32 TFT UI**
Open `emotion_display/esp32_tft_ui/esp32_tft_ui.ino` in Arduino IDE. Install the TFT_eSPI library and configure its `User_Setup` for your exact display/controller/pins before uploading. The sketch shows simple eye expressions and accepts serial commands: `happy`, `neutral`, `sleep`, `alert`.

## MQTT (optional)
Set `MQTT_ENABLED=true` and configure `MQTT_HOST`, `MQTT_PORT`, and `MQTT_TOPIC` in `.env`. Install/run a broker separately. The Python helper publishes JSON events when MQTT is enabled.

## Safety
- Do not connect motor power or test movement with the robot lifted unsafely.
- Vision detections are advisory only. Never wire raw detections directly to motor commands.
- Add an independent obstacle-stop/safety controller before any autonomous movement.
- Do not commit Wi-Fi passwords, API keys, private recordings, or personal data.
- This repository does not implement autonomous navigation or verified safe follow-person behavior.

## Repository structure

```text
NEXUS-AI-Pet-Robot/
├── ai_voice/
├── vision_ai/
├── emotion_display/esp32_tft_ui/
├── mobile_dashboard/
├── memory_meeting_ai/
├── shared/
├── docs/
├── hardware/
├── images/
├── requirements.txt
└── .env.example
```

## Team
T. Hemanth | S. Raviteja | N. Sidhartha | G. Sathvik | M. Anshul Kumar

Guide: Dr. Suresh Kumar Mandala, Associate Professor
