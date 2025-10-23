from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import form

tipoPrograma = form.menu()

if tipoPrograma == 1:

    tabela = pd.read_excel(r"Arquivos\ExemplosNotas.xlsx")

    #Looping para percorrer o xlsx
    for i,cnpj in enumerate(tabela["CNPJ"]):
        desc =tabela.loc[i,"DESCRIÇÃO"]
        valor =tabela.loc[i,"VALOR(R$)"]
        inss =tabela.loc[i,"INSS"]
        nome =tabela.loc[i,"NOME"]


        time.sleep(2)
        
        #Acessa o site das notas
        navegador = form.Login()

        original_window = form.localForms(navegador)

        form.selTomador(navegador,original_window,cnpj)

    #Local prestação
        form.localPrest(navegador)
        
        respdesc = "a"
        form.camposSendKeys(respdesc,navegador,desc,valor)

        resp = form.concluirEmissão(navegador)

        if resp not in ('s','S','Sim','SIM','sim'):
            break

elif tipoPrograma == 2:
    #Variável de controle


    #Looping de preenchimeento
    while(True):

            #Campos a serem preenchidos:
            cnpj = input("Digite o CNPJ: ")
            respdesc = input("Deseja preencher a descrição automático ou manual ? a/m")

            if respdesc == 'a':
                    desc = input("Digite a Descrição: ")

            valor = input("Digite o Valor: ")
            inss = input("Digite o valor do INSS: ")


            resp = input("Deseja prosseguir com a emissão s/n ? ")

            if resp in ('s','S','Sim','SIM','sim'):
                    time.sleep(2)

                    #Faz login
                    navegador = form.Login()

                    #Varivel janela original
                    original_window = form.localForms(navegador)

                    #Alternar Aba selecionar tomador
                    form.selTomador(navegador,original_window,cnpj)
                    
                    #Local prestação
                    form.localPrest(navegador)
                    
                    #Responde Campos ctrl C ctrl V
                    form.camposSendKeys(respdesc,navegador,desc,valor)

           
                    aut = form.concluirEmissãoManual(navegador)

            else:
                  break

elif tipoPrograma == 3:
      form.cadastroAuto()
                    
            
            
    











