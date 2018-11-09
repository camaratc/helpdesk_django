# Instalação: #

1 - Executar: ```sudo docker-compose up -d --build --remove-orphans``` e aguardar a inicialização do banco de dados;

2 - Entrar no bash do app, fazer as migrações e criar superuser do Django:

- ```sudo docker-compose exec app bash```
- ```python manage.py makemigrations```
- ```python manage.py migrate```
- ```python manage.py createsuperuser```

3 - Sair do bash e reiniciar o container: ```sudo docker-compose restart app```


## Opcional: ##
- Executar, se houver necessidade dos arquivos estáticos: ```python manage.py collectstatic```
- Para realizar o proxy reverso copiar o arquivo _src/config/helpdesk.conf_ para a pasta de configuração do Nginx _/etc/nginx/conf.d/_
