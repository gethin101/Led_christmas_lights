# 🎄 Voice-Controlled Christmas Lights & Music

## Overview
This project creates a festive **Christmas decoration system** powered by a Raspberry Pi Pico 2 WH.  
It combines **voice recognition**, **addressable LED lights**, and **music playback** to deliver an interactive holiday experience.  
Users can speak commands like *"lights on"* or *"play music"* to trigger colorful LED patterns and Christmas songs.

---

## Goals
- 🎤 **Voice Control**: Use the LD3320 module to recognize simple spoken commands.
- 🌈 **LED Effects**: Drive WS2812B LED strips with custom animations (red/green waves, rainbow chase, synced flashing).
- 🎶 **Music Playback**: Play MP3 Christmas songs stored on a microSD card via DFPlayer Mini.
- 🛠️ **DIY Friendly**: Built with affordable, widely available parts and documented for replication.

---

## Bill of Materials
| Item | Qty | Approx. Price (UK) | Notes |
|------|-----|--------------------|-------|
| Raspberry Pi Pico 2 WH | 1 | £10–£15 | Main controller |
| WS2812B LED strip (5m) | 1 | £12–£25 | Addressable RGB LEDs |
| LD3320 Voice Recognition Module | 1 | £7–£9 | Offline voice commands |
| DFPlayer Mini MP3 module | 1 | £4–£7 | Plays MP3s from microSD |
| MicroSD card (8GB) | 1 | £5–£10 | Stores songs |
| Speaker (5W–10W, 4–8Ω) | 1–2 | £10–£15 | For room-filling sound |
| PAM8403 amplifier (optional) | 1 | £3–£6 | Boosts audio output |
| Breadboard | 1 | £5 | For prototyping |
| Jumper wires kit | 1 | £5–£10 | Connections |

**Estimated total cost:** £65–£90 depending on speaker/LED choice.

---

## Wiring Diagram
- **Pico → WS2812B**: GPIO pin (e.g., GP0) → LED data line  
- **Pico → LD3320**: SPI/parallel pins → LD3320 interface  
- **Pico → DFPlayer Mini**: UART TX/RX → DFPlayer RX/TX  
- **DFPlayer Mini → Speaker**: Direct connection or via PAM8403 amplifier  
- **Power**: 5V supply for LEDs, DFPlayer, and speaker; Pico powered via USB or 5V rail

*(Include a diagram image here once drawn)*

---

## Voice Commands
- `"lights on"` → LEDs turn festive colors  
- `"red"` → LEDs glow red  
- `"green"` → LEDs glow green  
- `"play music"` → DFPlayer plays Christmas song  
- `"stop music"` → DFPlayer stops playback  

---

## Software
- Written in **MicroPython** for Pico 2 WH.  
- Libraries used:
  - `neopixel` for WS2812B control
  - UART commands for DFPlayer Mini
  - LD3320 driver (custom integration)

---

## Next Steps
- Build prototype on breadboard.  
- Test LED patterns and music playback.  
- Train LD3320 with chosen voice commands.  
- Document with photos and demo video.  

---

## License
MIT License — free to use, modify, and share.
