from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import form


tipoPrograma = input("Qual tipo de programa deseja executar ? (auto/semi)")


if tipoPrograma == 'auto':

    tabela = pd.read_excel(r"arquivos\notas.xlsx")

    #Looping para percorrer o xlsx
    for i,cnpj in enumerate(tabela["CNPJ"]):
        desc =tabela.loc[i,"DESCRIÇÃO"]
        valor =tabela.loc[i,"VALOR(R$)"]
        inss =tabela.loc[i,"INSS"]

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

        if resp != 's' or 'S' or 'Sim':
            break

elif tipoPrograma == 'semi':
    #Variável de controle
    aut = True

    #Looping de preenchimeento
    while(aut):

            #Campos a serem preenchidos:
            cnpj = input("Digite o CNPJ: ")
            respdesc = input("Deseja preencher a descrição automático ou manual ? a/m")

            if respdesc == 'a':
                    desc = input("Digite a Descrição: ")

            valor = input("Digite o Valor: ")
            inss = input("Digite o valor do INSS: ")


            resp = input("Deseja prosseguir com a emissão s/n ? ")

            if resp == 's':
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

            #Conclui a emissão:
            aut = form.concluirEmissãoManual(navegador)
                    
            
            
    











