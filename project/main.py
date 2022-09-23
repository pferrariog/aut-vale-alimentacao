from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date
from os import getenv
from dotenv import load_dotenv, find_dotenv


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


def main_execution(chrome, user, password):
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

    # adelina
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl02$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_0').send_keys('6.50')
    sleep(1)

    # ademar
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl03$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_1').send_keys('548.76')
    sleep(1)

    # ageu
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl04$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_2').send_keys('548.76')
    sleep(1)

    # bruno
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl06$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_4').send_keys('548.76')
    sleep(1)

    # elias
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl10$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_8').send_keys('548.76')
    sleep(1)

    # filipe
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl14$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_12').send_keys('548.76')
    sleep(1)

    # jeorge
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl18$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_16').send_keys('548.76')
    sleep(1)

    # jó
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl19$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_17').send_keys('548.76')
    sleep(1)

    # josé
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl20$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_18').send_keys('548.76')
    sleep(1)

    # marcos
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl24$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_22').send_keys('548.76')
    sleep(1)

    # otávio
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl26$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_24').send_keys('548.76')
    sleep(1)

    # rafael
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl28$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_26').send_keys('548.76')
    sleep(1)

    # ronevon
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl32$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_30').send_keys('548.76')
    sleep(1)

    # sebastião
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl34$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_32').send_keys('548.76')
    sleep(1)

    # thiago
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl35$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_33').send_keys('548.76')
    sleep(1)

    # wanderson
    chrome.find_element(By.NAME, value='ctl00$ContentPlaceHolder1$gvwCartoes$ctl36$chkUsuariosSelecionados').click()
    sleep(1)
    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwCartoes_txtValorCarga_34').send_keys('548.76')
    sleep(4)

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
    sleep(180)

    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_btnBoleto').click()
    sleep(1)

    chrome.find_element(By.CSS_SELECTOR, value='#ContentPlaceHolder1_gvwBoletos_imgImprimirBoleto_0').click()

    sleep(100)
    chrome.quit()


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    login = getenv("UP_LOGIN")
    senha = getenv("UP_SENHA")
    order_date = get_date()
    browser_options = 'user-data-dir=Perfil'
    chrome_browser = web_browser_connect()
    main_execution(chrome_browser, login, senha)
