# TranslateAI

TranslateAI is a powerful real-time speech translation desktop application built using PyQt and Hugging Face models. It enables users to seamlessly convert spoken words into text and translate them into different languages.

<table style="width:100%; height:300px; border: none; border-collapse: collapse;">
  <tr>
    <td style="text-align:center; vertical-align:middle; border:none;">
      <img src="https://github.com/user-attachments/assets/f4f7ee85-79ee-4872-945f-caec6ed38f0d" height="50%">
    </td>
    <td style="text-align:center; vertical-align:middle; border:none;">
      <img src="https://github.com/user-attachments/assets/3d587358-ebb2-4e9b-b312-550997fa824b" height="50%">
    </td>
  </tr>
</table>

This app allows you to:

- Select your preferred input device, whether it's a microphone or system audio, ensuring flexibility in capturing speech.
- Speak or even play pre-recorded audio files, and the app will process and transcribe the speech into text in real time.
- Enjoy an automatic translation trigger, which activates after about 1 second of silence, making the experience smooth and natural.
- Translate between multiple languages, including Turkish 🇹🇷, English 🇬🇧, Spanish 🇪🇸, and French 🇫🇷, with the possibility of adding more in the future.


Designed with ease of use and efficiency in mind, TranslateAI brings a fluid translation experience for various use cases, whether you're learning a new language, working in multilingual environments, or simply looking for an intuitive speech-to-text tool.


## 📌 Contents

- 🚀 Features
- 📦 Installation
   - MacOS
   - Windows
   - Linux
- 🛠️ Usage
- 🧠 How It Works
   - Speech Detection
   - Translation Model
- ⚙️ Configuration
- 🤝 Contributing
- 📝 License

---

## 🚀 Features

- 🎙️ **Real-time Speech & Audio Translation**
- 🔊 **Visual Indicator for Sound Intensity**
- 🌐 **Multi-language Support: Turkish 🇹🇷, English 🇺🇸, Spanish 🇪🇸, French 🇫🇷 (More to come!)**
- 🤖 **Hugging Face Model Integration**
- ⚡ **Automatic Model Download Based on Selected Language**
- 🖥️ **User-Friendly PyQt GUI**

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/furkankarakuz/TranslateAI.git
cd TranslateAI
```

### 2. Set Up a Python Environment (Recommended)

It’s often best to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

> **Note**: If `requirements.txt` doesn’t exist or you prefer manual installation, make sure to install:
> - `PyQt5` or `PyQt6` (depending on your code)
> - `pyaudio` (or `sounddevice` / `pydub` if you adapt the code)
> - `torch`, `transformers`, `datasets` (for Hugging Face)

### MacOS

On **macOS**, you may need to install `portaudio` via Homebrew before installing `pyaudio`:

```bash
brew install portaudio
```

Then:

```bash
pip install pyaudio
```

### Windows

On **Windows**, you can directly install `pyaudio` from PyPI:

```bash
pip install pyaudio
```

If you encounter issues, you might need to install the appropriate **Microsoft Visual C++ Build Tools**.

### Linux

On **Linux** (Ubuntu/Debian-based), you may need:

```bash
sudo apt-get update
sudo apt-get install portaudio19-dev python3-pyaudio
```

Then install Python packages as usual:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage

1. **Run the Application**
   ```bash
   python app.py
   ```

2. **Select Your Audio Device**  
   - In the top section of the UI, choose your microphone or system audio input (e.g., “MacBook Air Microphone …”).

3. **Choose Language Pair**  
   - Select the **source** and **target** language. For example, `EN-TR` means you will speak English and get Turkish translations.

4. **Start Recording**  
   - Click **Start Record** to begin capturing audio.  
   - Watch the volume indicator to see if audio is being detected.  
   - After you **stop speaking for about 1 second**, the application will automatically **trigger the translation**.

5. **View Translations**  
   - The translated text will appear in the console.  

6. **Stop Recording**  
   - Click **Stop Record** when finished.  

---

## 🧠 How It Works

### Speech Detection

- **PyAudio** captures your microphone input (or chosen device).  
- A **volume level meter** is displayed to help you monitor input levels.  
- Once **silence** (below a certain threshold) is detected for ~1 second, the app processes the captured audio chunk and sends it for transcription & translation.

### Translation Model

- The application uses **Hugging Face** Transformers to download and run the appropriate translation model for the chosen language pair.  
- **Model caching**: Once a model is downloaded, it should be reused for subsequent translations to save time.  
- The translations are displayed in real-time, providing an **instant** feedback loop.

---

## ⚙️ Configuration

- **Silence Threshold & Delay**: Currently set to about 1 second. You can modify this value in the code if you want quicker or slower triggers.  
- **Language Support**: To add a new language pair, you need to:
  - Find a Hugging Face translation model that supports that pair.
  - Update the UI to include the new language option.
  - Adjust the code that downloads/loads the model.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- **Fork** this repository.
- **Create** a new branch.
- **Commit** your changes.
- Open a **Pull Request** describing the improvements or bug fixes you’ve made.

---

## 📝 License

This project is licensed under the Apache License 2.0
