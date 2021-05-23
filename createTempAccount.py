import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://flashbox.5july.org/') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            text = html[2898:2994]
            start = text.find(">")
            stop = text.find("<")
            ac = text[start+1:stop]
            print('your temp account 'ac)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
