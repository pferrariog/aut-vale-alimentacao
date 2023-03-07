from datetime import date
from datetime import timedelta
from time import sleep

from keyboard import press_and_release
from keyboard import write
from pandas import read_excel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from yaml import safe_load

from sender import mail_sender


def web_browser_connect(*options: str) -> webdriver.Chrome:
    """Função p/ configurar o driver corretamente com a versão do browser"""
    # browser_options = "user-data-dir=Perfil"

    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(argument=option)
    chrome_service = Service(executable_path="chromedriver.exe")
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.maximize_window()
    return browser


def get_date() -> str:
    """Função para retornar a data corretamente conforme o campo"""
    tomorrow = date.today() + timedelta(days=1)
    date_today = tomorrow.strftime("%d/%m/%Y")
    return date_today


def login_up(webdriver: webdriver, user: str, password: str) -> None:
    """Login into portal"""
    webdriver.get("https://wss.upbrasil.com/portalup/login.aspx")
    webdriver.find_element(By.NAME, "txtUsuarioEmpresa").send_keys(user)
    webdriver.find_element(By.NAME, "txtSenha").send_keys(password)
    webdriver.find_element(By.NAME, "form_up_entrar").click()


def order_openning(webdriver: webdriver, order_date: str) -> None:
    """Get to the order screen"""
    webdriver.get("https://wss.upbrasil.com/SGP/CadastroPedidoOnline.aspx")
    webdriver.find_element(By.ID, value="txtDataEntrega").send_keys(order_date)
    webdriver.find_element(By.CSS_SELECTOR, value="#ContentPlaceHolder1_ddlPlanoVenda > option:nth-child(2)").click()
    webdriver.find_element(By.CSS_SELECTOR, value="#ContentPlaceHolder1_btnSalvar").click()
    webdriver.find_element(By.CSS_SELECTOR, value="#ContentPlaceHolder1_ddlProduto > option:nth-child(2)").click()
    sleep(1)
    webdriver.find_element(By.CSS_SELECTOR, value="#ContentPlaceHolder1_btnPesquisaUsuario").click()
    sleep(2)


def fill_employee_form(webdriver: webdriver, employee_data: dict) -> None:
    """Fill the form with employee data from input file"""
    checkbox = "/html/body/form/div[3]/div[2]/div[3]/div[2]/div[1]/div[20]/div/div[7]/div/div[2]/div/table/tbody"
    for index in employee_data["ID"].index:
        valor = employee_data["Conta"].loc[index]  # TODO null value validation
        webdriver.find_element(By.XPATH, f'{checkbox}/tr[{employee_data.loc[index, "ID"]}]/td[1]/input').click()
        sleep(1)
        webdriver.find_element(
            By.XPATH, f'//*[@id="ContentPlaceHolder1_gvwCartoes_txtValorCarga_{employee_data.loc[index, "ID"] - 2}"]'
        ).send_keys(f"{float(valor):.2f}")
        sleep(1)


def browse_to_output_report(webdriver: webdriver) -> None:
    """Browse the website until generate output report screen"""
    webdriver.find_element(By.CSS_SELECTOR, value="#ContentPlaceHolder1_btnIncluirUsuarios").click()
    sleep(3)
    webdriver.switch_to.alert.accept()
    sleep(2)

    # Generate PDF w/ employees included
    webdriver.find_element(By.CSS_SELECTOR, value="#ContentPlaceHolder1_btnGerarPdfIncluidos").click()
    sleep(1)

    webdriver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_btnProximo").click()
    sleep(3)
    webdriver.switch_to.alert.accept()
    sleep(2)
    webdriver.find_element(By.CSS_SELECTOR, value="#ContentPlaceHolder1_btnEnviarPedido").click()
    sleep(5)
    webdriver.switch_to.alert.accept()
    sleep(5)
    webdriver.switch_to.alert.accept()

    # Waiting the report generation
    sleep(120)


def save_report(webdriver: webdriver) -> None:
    """Download the PDF report"""
    webdriver.find_element(By.XPATH, "//input[@value='Imprimir Boleto'][@type='submit']").click()
    sleep(1)
    webdriver.find_element(By.XPATH, "//input[@title='Gerar boleto'][@type='image']").click()
    sleep(5)

    # Switch to PDF popup screen
    window_popup = webdriver.window_handles[1]
    webdriver.switch_to.window(window_popup)
    sleep(3)

    # Save and rename file
    press_and_release("ctrl+s")
    sleep(1)
    write(f"Boleto Ticket Alimentação - {date.today()}.pdf")
    sleep(1)
    press_and_release("enter")

    sleep(1)
    webdriver.close()


def main_execution(credentials: dict) -> None:
    """Execução principal da automação"""
    current_webdriver = web_browser_connect()
    employee_data = read_excel(r".\input\Dadosfunc.xlsx", dtype={"Conta": str})
    order_date = get_date()
    login_up(current_webdriver, credentials["login"], credentials["senha"])
    order_openning(current_webdriver, order_date)
    fill_employee_form(current_webdriver, employee_data)
    browse_to_output_report(current_webdriver)
    save_report(current_webdriver)
    mail_sender(credentials["username"], credentials["password"], "", order_date, credentials["to"])


if __name__ == "__main__":
    with open("./input/up.yaml") as file:
        process_dict = safe_load(file)
    main_execution(process_dict)
