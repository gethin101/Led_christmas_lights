# 🎄 Gethin's Voice-Controlled Christmas Lights v1

This repository contains all design files for my **HackClub Blueprint Custom LED Project**.  
My project is designed to combine **voice recognition**, **LED strip lights**, and **christmas music playback** for a cool interactive christmas setup that controls LED strip lights & plays songs via a DFPlayer mini MP3 player.

 

**It should feature:**

-Raspberry Pi Pico

-LD3320 voice recoginition module

-WS2812B LED strip lights (30 led/m - 2m)

-DFPlayer Mini & 8gb microSD storage

-PAM8403 amplifier & BF 37 speakers

-5V 3A wall power adapter

-Breaboard & jumper wires

-Speaker extension wire (if needed)

---

## Rough layout

<img alt="image" src="Images/led_lights_layout.png" />


## 📸 My view for the project


-I want the Raspberry Pi Pico to listen for voice commands through the LD3320 voice recognition module.

-The user can use prompts to control the setup.

-Triggers colorful LED animations on the WS2812B strip lights & plays christmas songs through the DFPlayer Mini

## Firmware Summary

The firmware is written in CircuitPython and split into small modules that handle LEDs, audio, and voice input seperately and then are referenced in the difference codes.
Main.py ties everything together by listening for voice triggers, running LED effects, and playing songs from the DFPlayer.
I will easily change the code later by editing the individual helper codes.

## Audio Summary

Music is stored on the DFPlayer Mini’s microSD card and are numbered as 0001.mp3.
The Pico sends simple commands to play tracks, while a PAM8403 amp and BF-37 speakers provide the audio output and play the christmas songs when commanded.

## 🔌 Breadboard design

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


---

voice recog https://www.aliexpress.com/item/1005007144572665.html?gatewayAdapt=usa2glo4itemAdapt

dfplayer mini https://www.aliexpress.com/item/1005006166800318.html?spm=a2g0o.productlist.main.1.764a21Fc21FcMB&algo_pvid=bc4a30aa-3f83-437a-9627-fddc84290746&algo_exp_id=bc4a30aa-3f83-437a-9627-fddc84290746-0&pdp_ext_f=%7B%22order%22%3A%22576%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%211.14%210.76%21%21%2110.43%216.95%21%40211b819117652667080666710e5ece%2112000037327793485%21sea%21UK%216897923402%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ae5f61ebb%3Bm03_new_user%3A-29895%3BpisId%3A5000000187461875&curPageLogUid=mRzHM7pNTvL9&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006166800318%7C_p_origin_prod%3A + STC11S

pico - <img width="1442" height="672" alt="image" src="https://github.com/user-attachments/assets/dbd78b96-bab4-4b8e-8d83-7d081e4fe417" />

need this? - <img width="366" height="579" alt="image" src="https://github.com/user-attachments/assets/0f91be5f-d994-4747-a58d-1c13bcea8030" />


## Bill of Materials (BOM)

| Component                | Notes                                                       | Links |
|--------------------------|-------------------------------------------------------------| |
| Raspberry Pi Pico        | Normal Pico (~£3–£5)                                        | |
| LD3320 Voice Module      | Offline voice recognition (~£5–£8)                          | |
| WS2812B LED Strip        | 2 m, 30 LEDs/m (~£12–£18)                                   | |
| DFPlayer Mini            | MP3 playback (~£1–£2)                                       | |
| MicroSD Card (8–16 GB)   | FAT32 formatted (~£3–£5)                                    | |
| PAM8403 Amplifier Board  | Stereo 5 V amp, version with knob (~£1–£2)                  | |
| BF‑37 Speakers (pair)    | Small drivers, clone versions (~£8–£12)                     | |
| 5 V 3 A Wall Adapter     | Power supply (~£5–£7, safer to buy locally if possible)     | |
| Breadboard               | For prototyping (~£3–£6, often bundled with jumper wires)   | |
| Jumper Wires             | Male–male/female, assorted lengths (~£2–£3 in kits)         | |
| #Speaker Wire (20–22 AWG)| Twisted pairs, ~1–2 m runs (~£2–£3)                        | prob dont need |

source most from aliexpress



---

## 🚀 Next Steps

- Once my project is approved, I will use the grant to purchase the components from the links in my BOM
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
