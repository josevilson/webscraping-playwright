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
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')

        # Espera um pouco para o scroll ser executado
            page.wait_for_timeout(3000)
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            page.wait_for_timeout(3000)
            # Coletar dados dos produtos na página atual
            cards = page.locator('.olx-ad-card__title')
            items = cards.all()  # Substitua com o seletor real dos itens do produto
            for item in items:
                titulo = item.inner_text()
                print(titulo)
                len(produtos)
                
                produtos.append({
                    'titulo': titulo
                })
                tamannho_produtos = len(produtos)
                print(f'qtd de produtos na lista: {tamannho_produtos}')

            locator = page.locator('a.olx-button.olx-button--link-button.olx-button--small.olx-button--a')
            next_buttons = locator.all()
            # print(next_buttons)
            for button in next_buttons:
                # Verificar se o texto do botão corresponde ao texto desejado
                if 'Próxima página' in button.inner_text():
                    # Obter o valor do atributo href
                    url = button.get_attribute('href')
                    print('URL do próximo botão:', url)
                    page.wait_for_timeout(3000)

        browser.close()


            # button = page.get_by_text("Próxima página")
            # # Iterar sobre os botões encontrados
            # # for button in next_buttons:
            # #     # Verificar se o texto do botão corresponde ao texto desejado
            # if 'Próxima página' in button.inner_text():
            #     # Faça algo com o botão
            #     print('Botão encontrado:', button.inner_text())
            #     url = button.get_attribute('href')

            # # Verificar se há uma próxima página
            # next_button = page.query_selector('a.olx-button.olx-button--link-button.olx-button--small.olx-button--a')
            # texto_retornado = next_button.inner_text()
            # print(texto_retornado)  # Substitua com o seletor real do botão de próxima página
            # if next_button:
            #     for button in next_button:
            #         texto = button.inner_text()

            #         if 'Próxima página' in texto:
            #             print(texto)
        #     #             url = button.get_attribute('href')

        #     # else:
        #     #     break

        # browser.close()

        # # Exibir os dados coletados
        # for produto in produtos:
        #     print(produto)


# Executar a função de scraping
scrape_ecommerce()
