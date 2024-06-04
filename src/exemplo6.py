from playwright.async_api import async_playwright
import asyncio
import csv

async def scrape_ecommerce():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko")
        page = await context.new_page()
        
        url = 'https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=forno%20pizza'  # Substitua com a URL real

        # Lista para armazenar os dados dos produtos
        arquivo_csv = 'dados.csv'

# Ler e imprimir o conteúdo atual do CSV (opcional)


        # Loop para navegar pelas páginas
        while True:
            produtos = []
            items = []
            page = await context.new_page()
            await page.goto(url)
            print(f'Scraping {url}')

            # Scroll até o fim da página para carregar todos os produtos
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            await page.wait_for_timeout(3000)  # Espera para carregar os itens após o scroll

            # Coletar dados dos produtos na página atual
            items = await page.locator('.olx-ad-card__title').all()  # Ajuste o seletor conforme necessário
            for item in items:
                titulo = await item.inner_text()
                with open(arquivo_csv,sep=';', mode='a', newline='\n') as file:
                    writer = csv.writer(file)
                    # Adicionar a nova linha
                    writer.writerow(titulo)
                
                

            print(f'Quantidade de produtos na lista: {len(produtos)}')

            # Verificar se há um botão "Próxima página"
            next_button = page.locator('a.olx-button--link-button:has-text("Próxima página")')
            if await next_button.count() > 0:
                # Pegar o href do botão "Próxima página"
                url = await next_button.first.get_attribute('href')
                await next_button.click()
                print(f'URL do próximo botão: {url}')
                await page.wait_for_timeout(3000)
            else:
                break  # Saia do loop se não houver mais páginas

        await browser.close()

        # Exibir os dados coletados
        for produto in produtos:
            print(produto)

# Executar a função de scraping
asyncio.run(scrape_ecommerce())
