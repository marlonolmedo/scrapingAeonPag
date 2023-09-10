import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get('https://aeon.com.sv', ssl=False) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print(html)
            # print("Body:", html[:15], "...")

asyncio.run(main())