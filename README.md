# Equilíbrio Térmico - Fenômenos de Transporte

### Comandos

 - Criando Ambiente Virtual: ```python -m venv venv```
 - Iniciando Ambiente Virtual (Linux): ```. venv/bin/activate```
 - Iniciando Ambiente Virtual (Windows PowerShell): ```.\venv\Scripts\Activate.ps1```
 - Iniciando Ambiente Virtual (Windows CMD): ```.\venv\Scripts\activate.bat```
 - Instalando Django: ```pip install django```
 - Armazenando bibliotecas: ```pip freeze > requirements.txt```
 - Instalando bibliotecas: ```pip install -r requirements.txt```
 - Criando projeto: ```django-admin startproject equilibrio_termico .```
 - Makemigrations e Migrate: ```python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py runserver --noreload```
 - Importar dados: ```python manage.py loaddata fixtures/fixtures.json```
 - Criando Superuser: ```python manage.py createsuperuser```
 - Criando app home: ```python manage.py startapp home```
 - Coleta todos os arquivos estáticos em STATICFILES_DIRS e os coloca no diretório STATIC_ROOT, de onde o servidor web pode servir esses arquivos: ```python manage.py collectstatic```
 - Iniciar servidor: ```python manage.py runserver --noreload```
 - Executando testes: ```python manage.py test```
 - Executando testes com coverage: ```coverage run --source='.' manage.py test```
 - Executando testes com coverage: ```coverage report -m```
 - Medir consumo de resiquições: ```locust```

### Postgres

 - Conentando no Postgres: ```psql -U postgres -h localhost```
 - Criando banco de dados: ```create database equilibrio_termico;```
 - Restaurar dados: ```pg_restore -h localhost -p 5432 -U postgres -d equilibrio_termico_backup /caminho/para/o/backup.sql```

### Outros

 - Criando arquivo txt com árvore do projeto: ```tree /f > tree.txt```
 - Iniciando Ngrok: ```ngrok http http://127.0.0.1:8000/```