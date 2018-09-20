# !/bin/bash

echo "===== Iniciando Helpdesk... ====="
cd /home/matheus/helpdesk_django && sudo docker-compose restart

echo "===== Iniciando Intranet... ====="
cd /home/matheus/intranet && sudo docker-compose restart