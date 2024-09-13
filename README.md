INSTALAÇÃO DE PACOTES EM pip.ini via diretory Petrobras == pip config set global.trusted-host "nexus.petrobras.com.br"
```
PASTA PROJETO
python -m pip install --upgrade pip
pip install pip setuptools wheel --upgrade > OK
python -m pip install pip setuptools wheel --upgrade > retirar o warning
python -m venv venv

PASTA VENV 
.\venv\Scripts\activate
pip install django
python -m pip install pip setuptools wheel --upgrade > retirar o warning
code .

NA PASTA DO PROJETO
git config --global user.name viniciusdantasdc
git config --global user.email viniemmovimento@gmail.com
git config --global init.defaultBranch main
git init
ssh-keygen > gerar chave da maq para o git SSH
git config --global push.autoSetupRemote true
git remote add origin git@github.com:viniciusdantasdc/fleet-naval-control-CNF-.git
git remote add origin https://github.com/viniciusdantasdc/fleet-naval-control-CNF-.git
git remote -v > confere se conectou
```
```
VSCODE
pip install pytest
python -m pip install mypy
python -m install -U flake8
python -m pip install -U autopep8


EXTENSÕES
> django = troca linguagem de HTML p/ DJANGO HTML
> icon materials thema
```
```
django-admin --help
django-admin startproject nomeProjeto .
python manage.py runserver
config DEBUG.json
>> rotas da urls.py

django-admin startapp
>>migrar urls.py para views
>> 
>>font awesome https://cdnjs.com/libraries/font-awesome/6.5.2
>>icon awesome https://fontawesome.com/search?q=ship&o=r
>>pasta pages em templates/nameSpace/pages
>>pasta partials em templates/nameSpace/head.html
>>use include para arquivos na pasta partials
>google fonts https://fonts.google.com/selection/embed
```

