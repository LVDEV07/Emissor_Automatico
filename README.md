# Emissor Automatico

Este projeto consiste em um script Python que utiliza a biblioteca Selenium para automatizar o processo de emissão de Notas Fiscais de Serviço Eletrônica (NFSe) no portal da prefeitura de Embu das Artes - SP.

O script oferece dois modos de operação: um modo totalmente automático que lê os dados de uma planilha Excel e um modo semi-automático que solicita os dados interativamente pelo terminal.

#Portal Alvo
O script foi desenvolvido para interagir com o seguinte portal: https://nfseembudasartes.obaratec.com.br

#Funcionalidades
<b> Login Automático: <\b> O script realiza o login no portal NFSe.

##Dois Modos de Operação:

Modo auto: Lê os dados de uma planilha Excel (notas.xlsx) para emitir múltiplas notas em lote.

Modo semi: Permite a emissão de notas uma a uma, solicitando os dados (CNPJ, descrição, valor) diretamente no terminal.

Navegação Automatizada: Preenche os campos do formulário, lida com a seleção do tomador de serviço (incluindo a troca para a janela pop-up) e preenche os detalhes da prestação de serviço.

Confirmação Final: Antes de emitir cada nota, o script solicita uma confirmação manual no terminal.

Pré-requisitos
Para executar este projeto, você precisará de:

Python 3.x

O navegador Google Chrome

ChromeDriver compatível com a sua versão do Google Chrome. (O Selenium precisa dele para controlar o navegador).

As seguintes bibliotecas Python:

selenium

pandas

Você pode instalar as bibliotecas necessárias usando o pip:

Bash

pip install selenium pandas openpyxl
Configuração Obrigatória
Antes de executar o script, você DEVE configurar suas credenciais e preparar o ambiente:

1. Credenciais de Acesso
Abra o arquivo form.py e localize a função Login(). Você precisa inserir seu usuário e senha de acesso ao portal nos locais indicados:

Python

# Em form.py

def Login():
    
    navegador = webdriver.Chrome()
    navegador.get("https://nfseembudasartes.obaratec.com.br/ords/embu01/f?p=936:1:17237546898536:::::")

    # Localiza os campos do login 
    navegador.find_element(By.XPATH, '//*[@id="P101_USERNAME"]').send_keys("COLOQUE_SEU_USUÁRIO_AQUI")
    navegador.find_element(By.XPATH, '//*[@id="P101_PASSWORD"]').send_keys("COLOQUE_SUA_SENHA_AQUI")

    # Aperta o botão de entrar
    navegador.find_element(By.XPATH, '//*[@id="P101_LOGIN"]').click()

    return navegador
    
2. ChromeDriver
Certifique-se de que o executável chromedriver esteja no PATH do seu sistema ou localizado na mesma pasta que os scripts Python.

3. Planilha (Para Modo auto)
Se você planeja usar o modo auto, siga esta estrutura:

Crie uma pasta chamada arquivos no mesmo diretório onde o ProgramaAuto.py está.

Dentro da pasta arquivos, crie um arquivo Excel chamado notas.xlsx.

A planilha deve conter as seguintes colunas, exatamente como nomeadas:

CNPJ

DESCRIÇÃO

VALOR(R$)

INSS (Observação: este campo é lido pelo script, mas não é usado nas funções de preenchimento atuais).

Como Usar
Certifique-se de ter concluído todas as etapas de Configuração Obrigatória.

Abra seu terminal ou prompt de comando.

Navegue até o diretório do projeto.

Execute o script principal:

Bash

python ProgramaAuto.py
O script perguntará qual modo deseja executar:

Qual tipo de programa deseja executar ? (auto/semi)
Se escolher auto:

O script começará a ler o arquivo arquivos/notas.xlsx.

Ele abrirá o navegador, fará o login e começará a preencher as notas, uma por linha da planilha.

A cada nota, ele perguntará no terminal: Confirma emissão ? s/n.

Digite s para emitir e continuar para a próxima, ou qualquer outra tecla para interromper o loop.

Se escolher semi:

O script solicitará os dados da nota no terminal (CNPJ, Descrição, Valor, etc.).

Ele perguntará se deseja prosseguir com a emissão (s/n).

Se s, ele fará o login e preencherá a nota.

Ele solicitará a confirmação final: Confirma emissão ? s/n.

Após a emissão (ou cancelamento), ele perguntará: Deseja continuar emitindo novas notas ? s/n.

Digite s para emitir outra nota ou n para encerrar o programa.

Estrutura dos Arquivos
.
├── ProgramaAuto.py     # Script principal que controla o fluxo
├── form.py             # Módulo com as funções de automação (Login, preenchimento, etc.)
└── arquivos/
    └── notas.xlsx      # (Opcional, necessário apenas para o modo 'auto')
Aviso
Este é um script de automação que lida com a emissão de documentos fiscais. O uso deste script é de sua inteira responsabilidade.

Teste exaustivamente: Antes de usar para emissões reais, teste em um ambiente de homologação (se disponível) ou com dados de teste.

Verifique as notas: Sempre confira as notas emitidas pela automação.

Manutenção: Os seletores (XPaths, IDs) do site podem mudar a qualquer momento, o que pode quebrar o script. Mantenha os seletores no arquivo form.py atualizados.

