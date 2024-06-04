import asyncio
import httpx
from selectolax.parser import HTMLParser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

async def fetch_and_parse(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        tree = HTMLParser(response.text)
        elements = tree.css('.olx-ad-card__title')
        titles = [element.text() for element in elements]
        return titles

# Exemplo de execução assíncrona
url = 'https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=forno%20pizza'
title = asyncio.run(fetch_and_parse(url))
print(f'Title: {title}')
print(f'Tamanho: {len(title)}')
