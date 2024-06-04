from playwright.sync_api import sync_playwright

url = 'https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=forno%20pizza'

def scraping_com_playwright():
    # Inicializa o Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        browser = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko")
        page = browser.new_page()

        # Navega até a página alvo
        page.goto(url)

        # Navega até o final da pagina
        page.evaluate('window.scrollTo(0, document.body.scrollHeight)')

        # Espera um pouco para o scroll ser executado
        page.wait_for_timeout(3000)
        page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        page.wait_for_timeout(3000)

        # Extrai os títulos dos artigos
        titles = page.query_selector_all('.olx-ad-card__title')
        for title in titles:
            print(title.inner_text())
        
        page.locator('.olx-button__content-wrapper').click()
        titles = page.query_selector_all('.olx-ad-card__title')
        for title in titles:
            print(title.inner_text())

        browser.close()

if __name__ == "__main__":
    scraping_com_playwright()
