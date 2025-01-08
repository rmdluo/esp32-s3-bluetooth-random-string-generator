import aioble
import asyncio
import bluetooth
import struct

from character_generator import generate_random_character

_RANDOM_CHAR_SERVICE_UUID = bluetooth.UUID(0xF8CD)
_RANDOM_CHAR_CHAR_UUID = bluetooth.UUID(0x902D)
_APPEARANCE = const(0)

_ADV_INTERVAL_US = const(250000)

MAX_LEN = const(128)

# Define BLE Service and Characteristic
random_char_generator_service = aioble.Service(_RANDOM_CHAR_SERVICE_UUID)
random_char_generator_char = aioble.Characteristic(random_char_generator_service, _RANDOM_CHAR_CHAR_UUID, read=True, notify=True)

aioble.register_services(random_char_generator_service)

async def heartbeat_task():
    random_str = "".join([generate_random_character() for _ in range(MAX_LEN)])
    while True:
        random_str = random_str[1:] + generate_random_character()
        random_char_generator_char.write(random_str.encode('utf-8'))
        await asyncio.sleep(1)  # Every 1 seconds

async def main():
    # Start notifying data
    asyncio.create_task(heartbeat_task())

    print("Waiting for connection...")
    while True:
        try:
            connection = await aioble.advertise(
                _ADV_INTERVAL_US,
                name="esp32s3",
                services=[_RANDOM_CHAR_SERVICE_UUID],
                appearance=_APPEARANCE,
                manufacturer=(0xabcd, b"1234"),
            )
            print("Connected to", connection.device)
            
            await connection.disconnected()  # Wait for disconnection
            print("Disconnected")
        except Exception as e:
            print("Error:", e)

asyncio.run(main())
