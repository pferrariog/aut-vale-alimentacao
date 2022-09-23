from datetime import date
from os import getenv
from time import sleep

from dotenv import find_dotenv, load_dotenv
from pandas import read_excel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def web_browser_connect(*options: str) -> webdriver.Chrome:
    """Função p/ configurar o driver corretamente com a versão do browser"""
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(argument=option)

    chrome_service = Service(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser


def get_date():
    """Função para retornar a data corretamente conforme o campo"""
    today = date.today()
    tomorrow = today.day + 1
    current_month = today.month
    current_year = today.year
    date_today = today.strftime(f"{tomorrow}/0{current_month}/{current_year}")
    return date_today


def main_execution(chrome, user: str, password: str, df):
    """Execução principal da automação"""
    chrome.get('https://wss.upbrasil.com/portalup/login.aspx')
    chrome.find_element(By.NAME, value='txtUsuarioEmpresa').send_keys(user)
    chrome.find_element(By.NAME, value='txtSenha').send_keys(password)
    chrome.find_element(By.NAME, value='form_up_entrar').click()
    chrome.get('https://wss.upbrasil.com/SGP/CadastroPedidoOnline.aspx')
    chrome.find_element(By.ID, value='txtDataEntrega').send_keys(order_date)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_ddlPlanoVenda > option:nth-child(2)').click()
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnSalvar').click()
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_ddlProduto > option:nth-child(2)').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnPesquisaUsuario').click()
    sleep(2)

    # setar valores por pessoa
    for index in df['ID']:
        chrome.find_element(By.NAME,
                            value=f'ctl00$ContentPlaceHolder1$gvwCartoes$ctl0{index}$chkUsuariosSelecionados').click()
        sleep(1)
        chrome.find_element(By.CSS_SELECTOR, value=f'#ContentPlaceHolder1_gvwCartoes_txtValorCarga_{index-2}').send_keys(
            df['Valor recebido'][index])
        sleep(1)

    # inclusão de usuários
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnIncluirUsuarios').click()
    sleep(4)

    chrome.switch_to.alert.accept()
    sleep(2)

    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnGerarPdfIncluidos').click()
    sleep(1)

    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnProximo').click()
    sleep(4)

    chrome.switch_to.alert.accept()
    sleep(2)

    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnEnviarPedido').click()
    sleep(4)

    chrome.switch_to.alert.accept()
    sleep(10)

    chrome.switch_to.alert.accept()
    sleep(120)

    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnBoleto').click()
    sleep(1)

    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwBoletos_imgImprimirBoleto_0').click()

    sleep(100)
    chrome.quit()


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    login = getenv("UP_LOGIN")
    senha = getenv("UP_SENHA")
    df_func = read_excel(r'.\input\Dadosfunc.xlsx')
    order_date = get_date()
    browser_options = 'user-data-dir=Perfil'
    chrome_browser = web_browser_connect()
    main_execution(chrome_browser, login, senha, df_func)
