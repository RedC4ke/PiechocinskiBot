docker context use default
docker build . --rm -t redc4ke/piechocinski-bot:production
docker image prune
Read-Host -Prompt "Press Enter to exit"