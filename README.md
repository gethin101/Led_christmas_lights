# 🎄 Gethin's Voice-Controlled Christmas Lights v1

This repository contains all files for my **HackClub Blueprint Custom Project**.  
The project is designed to combine **voice recognition**, **LED strip lights**, and **christmas music playback** for a cool interactive christmas setup that controls lights & plays songs.

 

**It should feature:**

-Raspberry Pi Pico 2 WH

-LD3320 voice recoginition module

-WS2812B LED strip lights

-DFPlayer Mini & microSD storage

-PAM8403 amplifier & BF 37 speakers

---

## 📸 My view for the project


-I want the Raspberry Pi Pico to listen for voice commands through the LD3320 voice recognition module.

-The user can use prompts to control the setup.

-Triggers colorful LED animations on the WS2812B strip lights & plays christmas songs through the DFPlayer Mini


## 🔌 Breadboard design

<img src="Images/breadboard.png" alt="breadboard png" width="500">

This is the layout of my components on a breadboard that I designed using Fritzing.

**Rough idea for connections:**

-WS2812B - Pico GP0 -> LED DI

-DFPlayer - Pico GP8 -> DFPlayer RX, GP9 (RX) -> DFPlayer TX

-LD3320 (SPIO):
   GP2 -> SCK
   GP3 -> MOSI
   GP4 -> MISO
   GP5 -> CS
   GP6 -> RST
   #maybe GP7 -> IRQ (interupt)
   
-PAM8403 -> BF 37 speakers

-Shared 5V & GND rails

---

## Voice commands

I will add many voice commands that users can use to control the lights & sounds.

**A few will include:**

-"**red**" - **makes lights glow red and turn on and off**

-"**green**" - **makes lights glow green and turn on and off**

-"**random song**" - **the DFPlayer will select & play a random christmas song**

-"**song1**" - **DFPlayer will play first song in album**

-"**song2**" - **DFPlayer will play second song in album**

-"**dark**" - **lights will turn off**

-"**stop**" - **DFPlayer will stop playback & wait for another command**

-"**turn off**" - **Pico will stop music, lights & voice recoginiton - essentially neutral mode**



## 📦 Bill of Materials (BOM)
List of all parts used in my project:

| Part | Quantity | Description |
|------|----------|-------------|
| Raspberry Pi Pico 2 WH | 1 | Microcontroller |
| WS2812B LED strip (5m) | 1 | Addressable RGB LEDs |
| LD3320 Voice Recognition Module | 1 | Offline voice recognition |
| DFPlayer Mini | 1 | MP3 player module |
| MicroSD card (8GB) | 1 | Stores Christmas songs |
| BF 37 speaker | 1–2 | Plays music |
| PAM8403 amplifier | 1 | Boosts audio output |
| Breadboard | 1 | For prototyping |
| Jumper wires | 1 set | For connections |

**Should come out to no more than £70**
---

## 🚀 Next Steps

- Once my project is approved, I will use the grant to purchase the components
- I will build the breadboard prototype with all modules connected
- I will test the LED animations and confirm that the DFPlayer plays music correctly
- I will train the LD3320 with my voice commands
- I will update this README & my project on Blueprints with photos & videos of the setup fully functional

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
This project is open-source under the MIT License and created by @Gethin101
