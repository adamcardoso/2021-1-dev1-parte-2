<h1 align="center">Projeto Final</h1>

<h3 align="center">Instalações preliminares</h3>

<p>Executar as seguintes etapas:</p>

* Instalar Python3.9.
* Instalar o VSCode


<p>Instalar através do VSCode as Extensões a seguir:</p>

* Github
* ms-python
* Django Template
* Python for VSCode
* Djaneiro

<p>Instalar PostgreSQL de preferência a última versão (13). Coloque a senha padrão "123456" e usuário padrão "postgres"</p>
<p>Instalar o Miniconda para Python3.9 e reiniciar o computador.</p>


<h3 align="center">Miniconda</h3>

<p> Criar ambiente virtual de programação.</p>

* conda create -n nome_do_projeto_que_voce_escolher python=3.9

<p>Liste os ambientes criados. </p>

* conda env list

<p>Remover ambiente virtual de programação. </p>

* conda env remove -n nome_do_projeto_que_voce_escolher 

<p>Criar ambiente virtual de programação novamente (Defina um nome seguido pela palavra app, por exmeplo "lojaapp" ou "projetoapp"). </p>

* conda create -n nome_do_projeto_que_voce_escolher

<p>Ative o ambiente criado e verifique se ficou no início da linha de comandos o nome do projeto entre parênteses. </p>

* conda activate nome_do_projeto_que_voce_escolher

<p>Desative o ambiente. </p>

* conda deactivate

<p>Ative novamente o ambiente. </p>

* conda activate nome_do_projeto_que_voce_escolher

<h3 align="center">As etapas a seguir devem ser executadas dentro do ambiente virtual de desenvolvimento para cada projeto.</h3>

<h3 align="center">Instalação de bibliotecas Python e Django.</h3>

<p>Instalar o pip com o Miniconda para gerenciamento de pacotes padrão e usado para instalar e gerenciar pacotes de software escritos em Python (A regra para instalação de pacotes, bibliotecas e dependências, será sempre instalar com o MINICONDA e caso não tenha utilizar o PIP). </p>

* conda install pip

<p>Instalar o interpretador Python "bpython" para codificar em Python no windows será pelo PIP.  </p>

* pip install bpython

<p>Executado através do comando. </p>

* python -m bpython.cli

<p>Instalar o interpretador Python "bpython" para codificar em Python. </p>

* conda install bpython

<p>Instalar Biblioteca "python-decouple" para esconder informações importantes por segurança como as de banco de dados em um arquivo separado ".env" com essas informações. </p>

* pip install python-decouple

<p>Instalar Biblioteca do drive do banco de dados postgres "psycopg2-binary" para rodar no Framework Django. </p>

* pip install psycopg2-binary

<p>Instalar biblioteca "Pillow" para tratar e resolver imagens para campos (ImageFilds). </p>

* conda install Pillow

<p>Instalar Biblioteca "django-widget-tweaks" para renderizar de templates, ajuda a trabalhar com os forms de formas com tags especificas. </p>

* pip install django-widget-tweaks

<p>Instalar o Framework Django e explicar o que é um Framework de desenvolvimento. </p>

* conda install django

<h3 align="center">Bpython</h3>

<p>Digite no nome do interpretador python</p>

* bpython

<p>Sair do interpretador</p>

* exit(0)


<h3 align="center">Framework Django</h3>

<p>Explique o que é um framework de uma linguagem e para que serve. </p>

<p>Crie um projeto Django em um diretório de sua escolha onde ficaram todos os seus projetos (Defina com o mesmo nome do ambiente virtual por exmeplo "lojaapp" ou "projetoapp"). </p> 

* django-admin startproject nome_do_projeto_que_voce_escolher

<p>O comando criará a seguinte estrutura. </p>

  <p>(RAIZ)nome_do_projeto_que_voce_escolher</p>
      <p>.</p>   
      <p>├── manage.py</p>
          <p>└── nome_do_projeto_que_voce_escolher</p>
            <p> ├── __init__.py</p>
                <p>├── asgi.py</p>
                    <p>├── settings.py</p>
                        <p>├── urls.py</p>
                            <p>└── wsgi.py</p>
   

<p>Acesse o diretorio RAIZ do projeto criado, e através do terminal inicie o serviço do Django. Lembre que dependendo do sitema operacional o "manage.py" pode ser executado de forma diferente, por exemplo sem o "./" .</p>

* ./manage.py runserver

<p>Acessar um navegador de sua escolha e digitar e teste o serviço.</p>

* http://localhost:8000

<p>Parar o serviço</p>

* Ctrl + C 

<p>Inicie novamente o serviço utilizando outra porta por exemplo 8001.</p>

* ./manage.py runserver 8001


<h3 align="center">Conferência de instalação de Bibliotecas</h3>

<p>Digite o comando e indica na lista as bibliotecas solicitadas instaladas. </p>

* pip list

<p>Digite o comando e indica na lista as bibliotecas solicitadas instaladas. </p>

* conda list


