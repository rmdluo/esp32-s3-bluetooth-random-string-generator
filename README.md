# esp32-s3-bluetooth-random-string-generator
Small toy project for testing ESP32-S3 DevKit-C bluetooth capabilities. Uses the ESP32-S3 as a GATT server which can be queried using GATT clients (see main.py and client.py respectively). The ESP32-S3 stores and random string and updates it by removing the first character and adding a new randomly selected character to the string. Clients can then retrieve the randomly generated string.

# Setup

1. Flash MicroPython onto the ESP32-S3 (https://micropython.org/download/?mcu=esp32s3)
2. Copy the files to the ESP32-S3 using something like ampy (pip library) or PyMakr (VSCode extension)
3. From another device with python, pip install `bleak` and run `python client.py`

## Sample output (client side)
```
Reading characteristic 0x902D
Random String: tyz]&)g#."!\4l0|([\)hp_pi`:=;a|:^}=#()w9_=34^q4;[!~3%b1ci9[/|r5!~@#4r`wxjnd.j_1^,;~m/g31$m26]2~tw3,|4]{|~3`k5e>]hx9k`e'[rm@|4tc{
```