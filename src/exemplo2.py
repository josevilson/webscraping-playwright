import asyncio
from pyppeteer import launch
import os 

PYPPETEER_CHROMIUM_REVISION = '1263111'
os.environ['PYPPETEER_CHROMIUM_REVISION'] = PYPPETEER_CHROMIUM_REVISION

async def main():
    # Lança o navegador
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    # Acessa a URL desejada
    url = 'https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=forno%20pizza'
    await page.goto(url)
    
    # Define a função de rolagem
    async def scroll_to_bottom():
        await page.evaluate('''
            async () => {
                const scrollHeight = document.body.scrollHeight;
                window.scrollTo(0, scrollHeight);
                await new Promise(resolve => setTimeout(resolve, 2000));
            }
        ''')
    
    last_height = await page.evaluate('document.body.scrollHeight')
    
    while True:
        await scroll_to_bottom()
        new_height = await page.evaluate('document.body.scrollHeight')
        
        if new_height == last_height:
            break
        last_height = new_height
    
    # Extrai o conteúdo desejado
    titles = await page.querySelectorAll('.olx-ad-card__title')
    for title in titles:
        text = await page.evaluate('(element) => element.textContent', title)
        print(text)
    
    # Fecha o navegador
    await browser.close()

# Executa a função assíncrona
asyncio.get_event_loop().run_until_complete(main())
