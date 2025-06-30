# 🆘 Gemma Emergency Assistant

An offline AI-powered emergency assistant built with the Gemma 3n model running locally via Ollama. Created for the **Google - Gemma 3n Impact Challenge 2025**.

## 🚀 Project Goal

To provide offline, instant, and intelligent assistance during natural disasters like floods, earthquakes, and power/internet outages — using only a local laptop and open-source AI tools.

## 🧠 How It Works

- **CLI Interface:** Runs in the Command Prompt or terminal
- **Gemma 3n via Ollama:** Uses the `gemma:2b` model to answer emergency-related questions
- **Offline Execution:** Works without internet after setup
- **Python-based:** Simple and lightweight, runs on most laptops

## 🧰 Features

- 📦 Suggests emergency survival kits
- 🌊 Gives flood safety guidance
- 🆘 Shares tips for power outages and communication failures
- 🧠 Answers general emergency questions intelligently

## 🛠️ Technologies Used

- **Python 3**
- **Ollama** (local model runner)
- **Gemma 3n (2B)** model
- `transformers`, `torch`, `sentencepiece`, `accelerate`

## 💻 How to Run the App

1. Install Ollama: [https://ollama.com](https://ollama.com)  
2. Download the Gemma 2B model:
Gemma Emergency Assistant (CLI)
|
Python (main.py)
|
Ollama API (Localhost)
|
Gemma 2B model (downloaded via Ollama)

---

## 🔧 Requirements

Install dependencies via `requirements.txt`, then run:

ollama run gemma:2b
python main.py

---

## 📦 How to Install

1. Install [Ollama](https://ollama.com) on your system.
2. Open terminal and run:
ollama pull gemma:2b
3. Clone this repo and run the app:
python main.py

---

## 🚀 Demo

A full 3-minute demo video is included in the [Kaggle Writeup Submission](https://www.kaggle.com/competitions/google-gemma-de-hackathon).

---

## 👩‍💻 Created By

**Amna Hanif**  
Solo Developer – Kaggle Gemma 3n Impact Challenge 2025

---
