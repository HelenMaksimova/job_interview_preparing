import asyncio
import aiohttp
from urllib.parse import urljoin

from bs4 import BeautifulSoup as BS


async def get_urls_list(base_url):
    session = aiohttp.ClientSession()
    async with session.get(base_url) as response:
        soup = BS(await response.text(), features="html.parser")
        elements = soup.find('div', {'class': 'list-group'}).findAll('a')
        urls = [urljoin(base_url, element['href']) for element in elements]
    await session.close()
    return urls


async def get_data(url):
    session = aiohttp.ClientSession()
    async with session.get(url) as response:
        soup = BS(await response.text(), features="html.parser")
        elements = soup.find('tbody').findAll('tr')
        data = [list(map(lambda x: x.text, element.findAll('td'))) for element in elements]
    await session.close()
    return data


async def main():
    urls_list = await get_urls_list('http://127.0.0.1:8000/')
    result, pending = await asyncio.wait([get_data(url) for url in urls_list])
    print(*(item.result() for item in result), sep='\n')

asyncio.run(main())
