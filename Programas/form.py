from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
import time



def menu():
    print("Menu de Opções:\n")
    print("1 - Emissão Automática (Planilha)")
    print("2 - Programa Semi-Automático (Terminal)")
    print("3 - Cadastro de Tomador Automático\n")

    resp = int(input("Digite a opção que você deseja: "))

    while resp < 1 or resp >3:
        print("Opção não disponível.") 
        resp = int(input("Tente Novamente: "))
        
    return resp




def localForms(navegador):
    WebDriverWait(navegador, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Emissor/Consulta"))).click()
    
    navegador.find_element(By.XPATH, '//*[@id="B3672601040293666174"]').click()
    

    #navegador.find_element(By.XPATH, '//*[@id="dialog"]/a').click()

    #Preencher Primeiro Campo
    navegador.find_element(By.XPATH, '//*[@id="P27_ATIV_ID"]/option[5]').click()

    original_window = navegador.current_window_handle

    return original_window

def Login():
    
    navegador = webdriver.Chrome()
    navegador.get("https://nfseembudasartes.obaratec.com.br/ords/embu01/f?p=936:1:17237546898536:::::")

    #Localiza os campos do login 
    navegador.find_element(By.XPATH, '//*[@id="P101_USERNAME"]').send_keys("SEU_USUARIO")
    navegador.find_element(By.XPATH, '//*[@id="P101_PASSWORD"]').send_keys("SUA SENHA")

    #Aperta o botão de entrar
    navegador.find_element(By.XPATH, '//*[@id="P101_LOGIN"]').click()

    return navegador


def localPrest(navegador):
    navegador.find_element(By.XPATH, '//*[@id="P27_LOCAL_PRESTACAO"]').click()
    navegador.find_element(By.XPATH, '//*[@id="P27_LOCAL_PRESTACAO"]/option[2]').click()
    WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, './/*[@id="P27_LIVR_SERV_NOM_UF"]/option[27]'))
    ).click()
    navegador.find_element(By.XPATH, '//*[@id="P27_LIVR_SERV_NOM_CIDADE"]')
    WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, './/*[@id="P27_LIVR_SERV_NOM_CIDADE"]/option[565]'))
        ).click()
    

def camposSendKeys(respdesc = "a", navegador ='',desc = "",valor = ""):
    
    if respdesc == 'a':
    #Descrição dos serviços
        navegador.find_element(By.XPATH, '//*[@id="P27_LIVR_DES_OBS"]').send_keys(desc)
                
    #Valor dos serviços:
    navegador.find_element(By.XPATH, '//*[@id="P27_LIVR_VLR_NF"]').send_keys(valor)

    
def selTomador(navegador,original_window,cnpj):

    #Alternar Aba selecionar tomador
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="lista_tomador"]'))
        ).click()

    for window_handle in navegador.window_handles:

        if window_handle != original_window:
   
            
            navegador.switch_to.window(window_handle)

            
            navegador.find_element(By.XPATH, '//*[@id="R3291304139423876545_search_field"]').send_keys(cnpj)
        
            WebDriverWait(navegador, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="R3291304139423876545_search_button"]'))
                    ).click()


            WebDriverWait(navegador, 20).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, f"CNPJ({cnpj})"))
                    ).click()

            break

    navegador.switch_to.window(original_window)

def concluirEmissão (navegador):
    resp = input("Confirma emissão ? s/n")
    if resp in ('s','S','sim','SIM','Sim'):

        #Clicar em emitir
        navegador.find_element(By.XPATH, '//*[@id="B3672605734338668498"]').click()

        time.sleep(5)

        WebDriverWait(navegador, 10)

        navegador.close()

    return resp

def concluirEmissãoManual (navegador):
    concluirEmissão(navegador)

    respfim = input("Deseja continuar emitindo novas notas ? s/n")

    if respfim in ('s','S','sim','SIM',"Sim"):
        aut = True
    else:
        aut = False

    return aut

def cadastroAuto():
    navegador = Login()
    #Botao cadastro
    #WebDriverWait(navegador, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Tomador/Prestador"))).click()
    navegador.find_element(By.PARTIAL_LINK_TEXT, 'Tomador/Prestador').click()

    #Botao Criar
    navegador.find_element(By.XPATH, '//*[@id="B3671938022945989178"]').click()

    navegador.find_element(By.XPATH, '//*[@id="P87_TIPO"]').click()

    time.sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="P87_TIPO"]/option[3]').click()
    
   
    time.sleep(2)
    
    resp = input("Qual tipo de cadastro deseja realizar (cpf ou cnpj) ? ")
    if resp == 'cnpj':
        #Seleciona o 2.1
        navegador.find_element(By.XPATH, '//*[@id="P87_TIPO2"]/option[2]').click()

        razaoSocial = input("Digite a Razão Social/Nome: ")
        cnpj = input("Digite o CNPJ:")
        cep = input("Digite o CEP: ")
        num = input("Digite o Número: ")
    

        navegador.find_element(By.XPATH, '//*[@id="P87_COCL_NOM_RAZAO"]').send_keys(razaoSocial)
        time.sleep(3)
        navegador.find_element(By.XPATH, '//*[@id="P87_COCL_NUM_CNPJ"]').click()
        ActionChains(navegador).key_down(Keys.CLEAR)
        navegador.find_element(By.XPATH, '//*[@id="P87_COCL_NUM_CNPJ"]').send_keys(cnpj)
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="P87_COCL_NUM_CEP"]').send_keys(cep)
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="P87_COCL_NUM_ENDERECO"]').send_keys(num)

        resp = input("Confirma o cadastro ?")
        if resp in ('s','S','sim','SIM','Sim'):
             navegador.find_element(By.XPATH, '//*[@id="B8721303721493203105"]').click()

             time.sleep(2)
             navegador.close()


        navegador.close()