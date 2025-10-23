<h1>Automação de Emissão de NFSe - Embu das Artes</h1>

<p>Este projeto consiste em um script Python que utiliza a biblioteca Selenium para automatizar o processo de emissão de Notas Fiscais de Serviço Eletrônica (NFSe) no portal da prefeitura de Embu das Artes - SP.</p>

<p>O script oferece dois modos de operação: um modo totalmente automático que lê os dados de uma planilha Excel e um modo semi-automático que solicita os dados interativamente pelo terminal.</p>

<h2>Portal Alvo</h2>

<p>O script foi desenvolvido para interagir com o seguinte portal:<br>
<code>https://nfseembudasartes.obaratec.com.br</code></p>

<h2>Funcionalidades</h2>

<ul>
    <li><strong>Login Automático:</strong> O script realiza o login no portal NFSe.</li>
    <li><strong>Dois Modos de Operação:</strong>
        <ul>
            <li><strong>Modo <code>auto</code>:</strong> Lê os dados de uma planilha Excel (<code>notas.xlsx</code>) para emitir múltiplas notas em lote.</li>
            <li><strong>Modo <code>semi</code>:</strong> Permite a emissão de notas uma a uma, solicitando os dados (CNPJ, descrição, valor) diretamente no terminal.</li>
        </ul>
    </li>
    <li><strong>Navegação Automatizada:</strong> Preenche os campos do formulário, lida com a seleção do tomador de serviço (incluindo a troca para a janela pop-up) e preenche os detalhes da prestação de serviço.</li>
    <li><strong>Confirmação Final:</strong> Antes de emitir cada nota, o script solicita uma confirmação manual no terminal.</li>
</ul>

<h2>Pré-requisitos</h2>

<p>Para executar este projeto, você precisará de:</p>

<ul>
    <li>Python 3.x</li>
    <li>O navegador Google Chrome</li>
    <li>ChromeDriver compatível com a sua versão do Google Chrome. (O Selenium precisa dele para controlar o navegador).</li>
    <li>As seguintes bibliotecas Python:
        <ul>
            <li><code>selenium</code></li>
            <li><code>pandas</code></li>
        </ul>
    </li>
</ul>

<p>Você pode instalar as bibliotecas necessárias usando o pip:</p>

<pre><code>pip install selenium pandas openpyxl</code></pre>

<h2>Configuração Obrigatória</h2>

<p>Antes de executar o script, você <strong>DEVE</strong> configurar suas credenciais e preparar o ambiente:</p>

<h3>1. Credenciais de Acesso</h3>

<p>Abra o arquivo <code>form.py</code> e localize a função <code>Login()</code>. Você precisa inserir seu usuário e senha de acesso ao portal nos locais indicados:</p>

<pre><code># Em form.py

def Login():
    
    navegador = webdriver.Chrome()
    navegador.get("https://nfseembudasartes.obaratec.com.br/ords/embu01/f?p=936:1:17237546898536:::::")

    # Localiza os campos do login 
    navegador.find_element(By.XPATH, '//*[@id="P101_USERNAME"]').send_keys("COLOQUE_SEU_USUÁRIO_AQUI")
    navegador.find_element(By.XPATH, '//*[@id="P101_PASSWORD"]').send_keys("COLOQUE_SUA_SENHA_AQUI")

    # Aperta o botão de entrar
    navegador.find_element(By.XPATH, '//*[@id="P101_LOGIN"]').click()

    return navegador</code></pre>

<h3>2. ChromeDriver</h3>

<p>Certifique-se de que o executável <code>chromedriver</code> esteja no <code>PATH</code> do seu sistema ou localizado na mesma pasta que os scripts Python.</p>

<h3>3. Planilha (Para Modo <code>auto</code>)</h3>

<p>Se você planeja usar o modo <code>auto</code>, siga esta estrutura:</p>

<ol>
    <li>Crie uma pasta chamada <code>arquivos</code> no mesmo diretório onde o <code>ProgramaAuto.py</code> está.</li>
    <li>Dentro da pasta <code>arquivos</code>, crie um arquivo Excel chamado <code>notas.xlsx</code>.</li>
    <li>A planilha <strong>deve</strong> conter as seguintes colunas, exatamente como nomeadas:
        <ul>
            <li><code>CNPJ</code></li>
            <li><code>DESCRIÇÃO</code></li>
            <li><code>VALOR(R$)</code></li>
            <li><code>INSS</code> (Observação: este campo é lido pelo script, mas não é usado nas funções de preenchimento atuais).</li>
        </ul>
    </li>
</ol>

<h2>Como Usar</h2>

<ol>
    <li>Certifique-se de ter concluído todas as etapas de <strong>Configuração Obrigatória</strong>.</li>
    <li>Abra seu terminal ou prompt de comando.</li>
    <li>Navegue até o diretório do projeto.</li>
    <li>Execute o script principal:
        <pre><code>python ProgramaAuto.py</code></pre>
    </li>
    <li>O script perguntará qual modo deseja executar:
        <pre><code>Qual tipo de programa deseja executar ? (auto/semi)</code></pre>
    </li>
    <li><strong>Se escolher <code>auto</code>:</strong>
        <ul>
            <li>O script começará a ler o arquivo <code>arquivos/notas.xlsx</code>.</li>
            <li>Ele abrirá o navegador, fará o login e começará a preencher as notas, uma por linha da planilha.</li>
            <li>A cada nota, ele perguntará no terminal: <code>Confirma emissão ? s/n</code>.</li>
            <li>Digite <code>s</code> para emitir e continuar para a próxima, ou qualquer outra tecla para interromper o loop.</li>
        </ul>
    </li>
    <li><strong>Se escolher <code>semi</code>:</strong>
        <ul>
            <li>O script solicitará os dados da nota no terminal (CNPJ, Descrição, Valor, etc.).</li>
            <li>Ele perguntará se deseja prosseguir com a emissão (<code>s/n</code>).</li>
            <li>Se <code>s</code>, ele fará o login e preencherá a nota.</li>
            <li>Ele solicitará a confirmação final: <code>Confirma emissão ? s/n</code>.</li>
            <li>Após a emissão (ou cancelamento), ele perguntará: <code>Deseja continuar emitindo novas notas ? s/n</code>.</li>
            <li>Digite <code>s</code> para emitir outra nota ou <code>n</code> para encerrar o programa.</li>
        </ul>
    </li>
</ol>

<h2>Estrutura dos Arquivos</h2>

<pre><code>.
├── ProgramaAuto.py     # Script principal que controla o fluxo
├── form.py             # Módulo com as funções de automação (Login, preenchimento, etc.)
└── arquivos/
    └── notas.xlsx      # (Opcional, necessário apenas para o modo 'auto')
</code></pre>

<h2>Aviso</h2>

<p>Este é um script de automação que lida com a emissão de documentos fiscais. O uso deste script é de sua inteira responsabilidade.</p>

<ul>
    <li><strong>Teste exaustivamente:</strong> Antes de usar para emissões reais, teste em um ambiente de homologação (se disponível) ou com dados de teste.</li>
    <li><strong>Verifique as notas:</strong> Sempre confira as notas emitidas pela automação.</li>
    <li><strong>Manutenção:</strong> Os seletores (XPaths, IDs) do site podem mudar a qualquer momento, o que pode quebrar o script. Mantenha os seletores no arquivo <code>form.py</code> atualizados.</li>
</ul>
