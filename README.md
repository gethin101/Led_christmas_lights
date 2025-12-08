# 🎄 Voice-Controlled Christmas Lights v1

This repository contains all files for my **HackClub Blueprint Custom Project**.  
The project is designed to combine **voice recognition**, **LED strip lights**, and **christmas music playback** for a cool interactive christmas setup.

It should feature:
-Raspberry Pi Pico 2 WH
-LD3320 voice recoginition module
-WS2812B LED strip lights
-DFPlayer Mini & microSD storage

---

## 📸 Project Overview

This is the overview of my Christmas lights + music system assembled in Fusion 360 / breadboard prototype.  
It shows how the Pico, LED strip, DFPlayer, and LD3320 module are connected together.

<img src="Images/project-overview.png" alt="Christmas Project Screenshot" width="600">

---

## 🔌 Schematic
![Schematic Screenshot](Images/schematic.png)

This schematic shows how each component is wired:
- Pico GPIO → WS2812B data line
- Pico UART → DFPlayer Mini RX/TX
- Pico SPI → LD3320 voice recognition module
- DFPlayer Mini → Speaker (direct or via PAM8403 amplifier)
- Power rails: 5V shared across LEDs, DFPlayer, and LD3320

---

## 🖥️ PCB / Breadboard Layout
This layout shows the component placement and wiring for prototyping.  
Later, this can be turned into a custom PCB for a permanent build.

<img src="Images/breadboard-layout.png" alt="Breadboard Screenshot" width="500">

---

## 🧩 Case Design

<img src="Images/case_base.png" alt="Case base fusion" width="500">
<img src="Images/case_cover.png" alt="Case cover fusion" width="500">
<img src="Images/case_assembled.png" alt="Case assembled fusion" width="500">

I designed a simple enclosure in Fusion 360 to hold the Pico, DFPlayer, and speaker.  
The LED strip can be mounted externally around a tree or window.

---

## 📦 Bill of Materials (BOM)
List of all parts used in my project:

| Part | Quantity | Description |
|------|----------|-------------|
| Raspberry Pi Pico 2 WH | 1 | Microcontroller |
| WS2812B LED strip (5m) | 1 | Addressable RGB LEDs |
| LD3320 Voice Recognition Module | 1 | Offline voice recognition |
| DFPlayer Mini | 1 | MP3 player module |
| MicroSD card (8GB) | 1 | Stores Christmas songs |
| Speaker (5W–10W, 4–8Ω) | 1–2 | Plays music |
| PAM8403 amplifier (optional) | 1 | Boosts audio output |
| Breadboard | 1 | For prototyping |
| Jumper wires | 1 set | For connections |

---

## Firmware Instructions

1. Flash the Raspberry Pi Pico 2 WH with MicroPython firmware.  
2. Connect via USB and upload `main.py`.  
3. Install required libraries:
   - `neopixel` for WS2812B LED control
   - UART driver for DFPlayer Mini
   - LD3320 driver (custom integration)
4. Train LD3320 with chosen voice commands (e.g., "lights on", "play music").  
5. Test LEDs and music playback.

---

## 📝 License
This project is open-source under the MIT License and created by @YourUsername
