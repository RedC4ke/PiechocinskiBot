docker context use piecho-bot
docker stop piecho-bot
docker rm piecho-bot
docker run --name piecho-bot --restart on-failure  --env-file src/.env -m 2G redc4ke/piechocinski-bot:production
Read-Host -Prompt "Press Enter to exit"