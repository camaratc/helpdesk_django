# Instalação: #

1 - Executar: ```docker-compose up -d --force-recreate --build --remove-orphans```

2 - Entrar no bash do app e fazer as migrações do Django

3 - Modificar a variável _USE\_TZ_ para **True** no _settings.py_

## Opcional: ##
- Executar, se houver necessidade dos arquivos estáticos: ```python manage.py collectstatic```
- Para realizar o proxy reverso copiar o arquivo _src/config/helpdesk.conf_ para a pasta de configuração do Nginx _/etc/nginx/conf.d/_