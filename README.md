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


---

## 📦 Bill of Materials (BOM)
List of all parts used in my project with likely sources:

| Part | Quantity | Description | Source |
|------|----------|-------------|--------|
| Raspberry Pi Pico 2 WH | 1 | Microcontroller | [PiHut Link](https://thepihut.com/products/raspberry-pi-pico-2-w?srsltid=AfmBOorHI_1q1DjVMA1ssCuGda-ervPT9WyUxXOJEcrdkc06SStn7pyK&scrlybrkr=fb02283f) + headers |
| WS2812B LED strip (5m) | 1 | Addressable RGB LEDs | [OnBuy Link](https://www.onbuy.com/gb/p/5m-ws2812b-led-strip-5v-144-pixel-ledsm-individually-addressable~p131223890/?exta=gshp&extac=gshpfa&scrlybrkr=fb02283f) |
| LD3320 Voice Recognition Module | 1 | Offline voice recognition | [Amazon link](https://www.amazon.co.uk/Recognition-Intelligent-Control-Development-Language-SPI-Port/dp/B0FND3DBT7?th=1) |
| DFPlayer Mini | 1 | MP3 player module | [Aliexpress link](https://s.click.aliexpress.com/deep_link.htm?dl_target_url=https%3A%2F%2Fwww.aliexpress.com%2Fitem%2F1005006584742737.html&src=google&aff_short_key=irey5Th&aff_platform=true&isdl=y) |
| MicroSD card (8GB) | 1 | Stores Christmas songs | [Amazon link](https://www.amazon.co.uk/SanDisk-MicroSDHC-Card-Label-Change/dp/B001C0DJL4?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1JF5HKJHGDUB9) |
| BF 37 speaker | 1–2 | Plays music | [ImpactAudio link](https://impactaudio.co.uk/products/visaton-bf-37-8-ohm) |
| PAM8403 amplifier | 1 | Boosts audio output | [Amazon link](https://www.amazon.co.uk/DollaTek-PAM8403-amplifier-module-audio/dp/B07DK7CYV5?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A3SCFTIO8CSK1X) |
| Breadboard | 1 | For prototyping | [Amazon link](https://www.amazon.co.uk/MMOBIEL-Solderless-Breadboard-Prototype-Circuit/dp/B0CPJPXDNX/ref=sr_1_2_sspa?crid=1BD5FWY3FPH08&dib=eyJ2IjoiMSJ9.3WtQephyJ_tMR9x7YadsvLyJBGm7673XLXePsMcovJWOwZCb1YAJn3JyNWvs1Qdc08yfJqsaOrM0oWmxyhtO3TpbtX6MdKeeVOSt9c4uXUL848-bxlkgCK2Nx8ARALdWHmPqkMGE3RRuJ068yAAqa_yHRETcLlNNs29gV2PwBw_Pc_ReOge6gukZF_UXkgpr3Ne4GgMZLwYgT-FP4lzA7imKe_MhKpb4l_Gn1vKxrBLCK8B0Y_ODkBdNpjwNBOnD_gpcwtU34gloA-w08L7K9TBNf3T0pQyYsDiXY3hkvlA.-93MR4NVNlsL1b3gFpehP-eqiGoe-CHjwZW5mjnPpGQ&dib_tag=se&keywords=breadboard+830&qid=1765229518&sprefix=breadboard+830%2Caps%2C88&sr=8-2-spons&aref=nCiSVGHNu3&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)|
| Jumper wires | Mixed set | For connections | [PiHut link](https://thepihut.com/products/thepihuts-jumper-bumper-pack-120pcs-dupont-wire?variant=13530244284478&country=GB&currency=GBP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&srsltid=AfmBOop0rdxrF5YBBWYAFB62J5QFmalpuACcezCw8UvOHM4R557Trwv-u2I) |

**Should come out to no more than £80**

voice recog https://www.aliexpress.com/item/1005007144572665.html?gatewayAdapt=usa2glo4itemAdapt

dfplayer mini https://www.aliexpress.com/item/1005006166800318.html?spm=a2g0o.productlist.main.1.764a21Fc21FcMB&algo_pvid=bc4a30aa-3f83-437a-9627-fddc84290746&algo_exp_id=bc4a30aa-3f83-437a-9627-fddc84290746-0&pdp_ext_f=%7B%22order%22%3A%22576%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%211.14%210.76%21%21%2110.43%216.95%21%40211b819117652667080666710e5ece%2112000037327793485%21sea%21UK%216897923402%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ae5f61ebb%3Bm03_new_user%3A-29895%3BpisId%3A5000000187461875&curPageLogUid=mRzHM7pNTvL9&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006166800318%7C_p_origin_prod%3A + STC11S

pico - <img width="1442" height="672" alt="image" src="https://github.com/user-attachments/assets/dbd78b96-bab4-4b8e-8d83-7d081e4fe417" />

need this? - <img width="366" height="579" alt="image" src="https://github.com/user-attachments/assets/0f91be5f-d994-4747-a58d-1c13bcea8030" />


| Component                | Description / Notes                                      |
|--------------------------|----------------------------------------------------------|
| Raspberry Pi Pico        | Main controller (normal Pico is fine, Pico 2 WH optional)|
| LD3320 Voice Module      | Offline voice recognition, with microphone               |
| WS2812B LED Strip        | 2 m length, 30 LEDs/m (≈60 LEDs total)                   |
| 330–470 Ω Resistor       | Series resistor on LED data line                         |
| 1000 µF Capacitor        | Across LED 5V/GND for stability                          |
| DFPlayer Mini            | MP3 playback from microSD card                           |
| MicroSD Card (8–32 GB)   | FAT32 formatted, tracks named 001.mp3, 002.mp3, etc.     |
| PAM8403 Amplifier Board  | Stereo 5 V amp, version with volume knob recommended     |
| BF‑37 Speakers (pair)    | Small drivers, ideally mounted in enclosures             |
| 5 V 3 A Wall Adapter     | Power supply for Pico, LEDs, audio                       |
| Breadboard               | For prototyping and module connections                   |
| Jumper Wires             | Male–male and male–female, assorted lengths              |
| Speaker Wire (20–22 AWG) | Twisted pairs, ~1–2 m runs to boxed speakers             |
| Thicker Wire (18–20 AWG) | For LED power injection if extending beyond 2 m          |
| Mounting Clips/Tape      | To secure LED strip to wall or shelf                     |
t
try get most stuff except from power from aliexrpess

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
