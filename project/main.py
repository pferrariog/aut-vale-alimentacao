from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date
from os import getenv
from dotenv import load_dotenv


def web_browser_connect(*options: str):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(argument=option)

    chrome_service = Service(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser


def get_date():
    today = date.today()
    tomorrow = today.day + 1
    current_month = today.month
    current_year = today.year
    date_today = today.strftime(f"{tomorrow}/0{current_month}/{current_year}")
    return date_today


if __name__ == '__main__':
    load_dotenv()
    order_date = get_date()
    browser_options = 'user-data-dir=Perfil'
    chrome = web_browser_connect()
    chrome.get('https://wss.upbrasil.com/portalup/login.aspx')
    chrome.find_element(By.NAME, value='txtUsuarioEmpresa').send_keys(getenv("UP_LOGIN"))
    chrome.find_element(By.NAME, value='txtSenha').send_keys("UP_SENHA")
    chrome.find_element(By.NAME, value='form_up_entrar').click()
    chrome.get('https://wss.upbrasil.com/SGP/CadastroPedidoOnline.aspx')
    chrome.find_element(By.ID, value='txtDataEntrega').send_keys(order_date)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_ddlPlanoVenda > option:nth-child(2)').click()
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnSalvar').click()
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_ddlProduto > option:nth-child(2)').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnPesquisaUsuario').click()

    # setar valores por pessoa
    sleep(2)
    # adelina
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl02$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_0').send_keys('548.76')
    sleep(1)
    # ademar
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl03$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_1').send_keys('548.76')

    sleep(10)
    chrome.quit()
