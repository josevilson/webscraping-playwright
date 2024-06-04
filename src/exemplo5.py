from playwright.sync_api import sync_playwright

def scrape_ecommerce():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko")
        page = context.new_page()
        

        url = 'https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=forno%20pizza'  # Substitua com a URL real

        # Lista para armazenar os dados dos produtos
        produtos = []

        # Loop para navegar pelas páginas
        while True:
            
            page.goto(url)
            print(f'Scraping {url}')

            # Scroll até o fim da página para carregar todos os produtos
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            page.wait_for_timeout(3000)  # Espera para carregar os itens após o scroll

            # Coletar dados dos produtos na página atual
            items = page.locator('.olx-ad-card__title').all()  # Ajuste o seletor conforme necessário
            for item in items:
                titulo = item.inner_text()
                print(titulo)
                produtos.append({'titulo': titulo})

            print(f'Quantidade de produtos na lista: {len(produtos)}')

            # Verificar se há um botão "Próxima página"
            next_button = page.locator('a.olx-button--link-button:has-text("Próxima página")')
            if next_button.count() > 0:
                # Pegar o href do botão "Próxima página"
                url = next_button.first.get_attribute('href')
                next_button.click()
                print(f'URL do próximo botão: {url}')
                page.wait_for_timeout(3000)
            else:
                break  # Saia do loop se não houver mais páginas

        browser.close()

        # Exibir os dados coletados
        for produto in produtos:
            print(produto)

# Executar a função de scraping
scrape_ecommerce()
