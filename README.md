# DjangoProject

Olá,

Eu sou Guilherme Picoli dos Santos, e desenvolvi em Python, utilizando o framework Django (v2.2.22), o Projeto DjangoProject, assim como seu APP AlunoApp, de maneira rápida para visualizarmos a estruturação básica de um CRUD relacional.

Para testar o programa, será necessário baixá-lo em uma máquina com Python e  Django instalados (comando cmd: "pip install django==2.2.22", ou a versão de sua escolha). 
Eu decidi não utilizar o PostgreSql, que rotineiramente uso, visando a simplicidade e fácil portabilidade do mesmo, assim sendo, o sistema está no seu sql embarcado, não sendo necessárias configurações de DB para visualizar este CRUD.

Após baixar o sistema e colocá-lo na pasta de sua escolha, abra o CMD, vá até o diretório escolhido, entre na pasta projeto (primeira DjangoProject), e insira os seguintes comandos:
python manage.py makemigrations AlunoApp
python manage.py migrate AlunoApp

Após sucesso, favor verificar a instalação das seguintes packages via pip, para evitar falta de imports (comando cmd: "pip freeze"), garantindo que você possui os mesmos módulos que esta imagem do meu pip freeze:

asgiref==3.5.1
bleach==5.0.0
Django==2.2.22
django-cpf==0.1.0
django-crispy-forms==1.14.0
django-simple-history==3.0.0
django-summernote==0.8.20.0
pytz==2022.1
six==1.16.0
sqlparse==0.4.2
tzdata==2022.1
webencodings==0.5.1

Caso algum esteja faltando, instale-o. Eu instalei manualmente os seguintes:

pip install Django==2.2.22
pip install django-cpf==0.1.0
pip install django-crispy-forms==1.14.0
pip install django-simple-history==3.0.0
pip install django-summernote==0.8.20.0

E então, ainda no CMD, rode o comando como exemplificado abaixo, para abrir o server:
X:\PastaSelecionadaPorVoce\DjangoProject> python manage.py runserver

Se a seguinte mensagem: 'Starting development server at http://127.0.0.1:8000/' aparecer, copie este link e cole no seu navegador, e então, você terá acesso ao APP.

O sistema está simples, não implementei a classe usuário(user/perfis/auth_perms), extends, css/js estáticos ou a admin session. 

Qualquer dúvida, entrar em contato via gpsantos1999@gmail.com

Boa noite. Divirta-se :D








