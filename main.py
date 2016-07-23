from selenium import webdriver
from selenium.webdriver.support.ui import Select
from os import listdir
from time import sleep
import simplejson as json


LOGIN_USR_ID = "sid"
LOGIN_PSW_ID = "PIN"
career = "040013-Ingenieria Civil"
delay = 2
data = None
ready = False
per_sel = False

if 'config.json' in listdir():
    print("Configuraciones encontradas, cargando ...")
    with open('config.json') as json_file:
        data = json.load(json_file)
else:
    print("Corre configUC.py antes para ingresar tus configuraciones.")
    exit()


# Generate semester dropdown text
def gen_sem(semester):
    data_str = ""
    year, sem = semester.split('-')
    data_str += year + ' '
    data_str += ("Primer" if sem == 1 else "Segundo") + " Semestre"
    return data_str


# LOGIN PAGE - Enters username and password into login site
def login_page(site_driver):
    # Obtain username and password fields
    usr_field = site_driver.find_element_by_name(LOGIN_USR_ID)
    psw_field = site_driver.find_element_by_name(LOGIN_PSW_ID)
    # Send user and pass to fields
    usr_field.send_keys(user_cred)
    psw_field.send_keys(pass_cred)
    # Create a list with all input elements and another with previous fields
    inputs = site_driver.find_elements_by_tag_name('input')
    fields = [usr_field, psw_field]
    # Subtract sets generated by previous lists and pop to obtain submit button
    sub_btn = (set(inputs) - set(fields)).pop()
    # Click on submit button to access system
    sub_btn.click()


# ADD CLASSES - Clicks Agregar o Eliminar Clases link
def add_classes(site_driver):
    add_btn = site_driver.find_element_by_link_text("Agregar o Eliminar Clases")
    add_btn.click()


# INSCRIPTION PERIOD - Reselect period and verify
def select_period(site_driver, semest, dela):
    global per_sel
    if not per_sel:
        prd_drop = Select(site_driver.find_element_by_id('term_id'))
        prd_drop.select_by_visible_text(semest)
        sub_btn = site_driver.find_element_by_xpath("//input[@value='Enviar']")
        sub_btn.click()
        per_sel = True
    if site_driver.title != 'Seleccionar Planes de Estudio':
        ret_btn = site_driver.find_element_by_id('ssbbackurl')
        ret_btn.click()
        sleep(dela)
        return False
    return True


# STUDIES SELECTION - Reselect period and proceed
def select_career(site_driver, carr):
    prd_drop = Select(site_driver.find_element_by_id('st_path_id'))
    prd_drop.select_by_visible_text(carr)
    sub_btn = site_driver.find_element_by_xpath("//input[@value='Enviar']")
    sub_btn.click()


# CLASSES INPUT - Inputs NRC codes and submits
def input_classes(site_driver, nrc_codes):
    while nrc_codes:
        # Find 3 NRC input fields and clear them
        nrc_fields = [site_driver.find_element_by_id('crn_id{}'.format(n)) for n in range(1, 4)]
        [nrc_field.clear() for nrc_field in nrc_fields]
        # Find send button
        snd_btn = site_driver.find_element_by_xpath("//input[@value='Enviar Cambios']")
        # Fill in NRC codes in order
        try:
            [nrc_field.send_keys(nrc_codes.pop(0)) for nrc_field in nrc_fields]
        except IndexError:
            pass
        # Send NRC. Rinse and repeat
        snd_btn.click()


user_cred = data['username']
pass_cred = data['password']
semestre = gen_sem(data['semestre'])
cods_nrc = data['nrc_code']

# Create driver and navigate to login
driver = webdriver.Firefox()
driver.get("https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin")

login_page(driver)
while not ready:
    add_classes(driver)
    ready = select_period(driver, semestre, delay)
select_career(driver, career)
input_classes(driver, cods_nrc)