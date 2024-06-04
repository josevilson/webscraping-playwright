from playwright.sync_api import sync_playwright

def extrair_links(page):
    """Extrai todos os links de uma página."""
    links = page.query_selector_all('a')
    for link in links:
        href = link.get_attribute('href')
        print(f"Link encontrado: {href}")

def configurar_callbacks(page):
    """Configura callbacks para manipular elementos e eventos de rede."""
    page.on("request", lambda request: print(f"Solicitação: {request.url}"))
    page.on("response", lambda response: print(f"Resposta: {response.url}"))
    page.on("domcontentloaded", lambda _: extrair_links(page))

with sync_playwright() as p:
    # Iniciar o navegador
    browser = p.chromium.launch()
    
    # Criar um contexto de navegador
    context = browser.new_context()
    
    # Configurar callbacks para páginas existentes
    for page in context.pages:
        configurar_callbacks(page)
    
    # Adicionar um evento para capturar novas páginas e configurar callbacks
    context.on("page", configurar_callbacks)
    
    # Abrir uma página de exemplo
    page1 = context.new_page()
    page1.goto("https://www.olx.com.br/estado-sp/sao-paulo-e-regiao?q=forno%20pizza")
    
    # Esperar um pouco para capturar eventos (opcional)
    page1.wait_for_timeout(5000)
    
    # Fechar o navegador
    browser.close()
