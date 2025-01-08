import asyncio
from bleak import BleakScanner
from bleak import BleakClient

async def main():
    print("Scanning...")
    devices = await BleakScanner.discover()
    address = None
    for d in devices:
        if d.name == "esp32s3":
            print("Found", d)
            address = d.address
    if address is None:
        print("esp32s3 not found")
        return

    print("Connecting...")
    async with BleakClient(address) as client:
        print("Connected!")

        while True:
            print("Reading characteristic 0x902D")
            random_str = await client.read_gatt_char("0000902d-0000-1000-8000-00805f9b34fb")
            print("Random String:", random_str.decode("utf-8"))

            await asyncio.sleep(1)

asyncio.run(main())
