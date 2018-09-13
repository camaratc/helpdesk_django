# Instalação: #

1 - Executar: ```docker-compose up -d --force-recreate --build --remove-orphans```

2 - Entrar no bash do app e fazer as migrações do Django

3 - Modificar a variável _USE\_TZ_ para **True** no _settings.py_

## Opcional: ##
- Executar, se houver necessidade dos arquivos estáticos: ```python manage.py collectstatic```
