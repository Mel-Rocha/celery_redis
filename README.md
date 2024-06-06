## Dependências do projeto
### Ambiente virtual
Criar um ambiente virtual na raiz do projeto com o comando

```bash
python -m venv venv
```

### Instalar as dependências necessárias
Executar o comando para instalar as dependencias que estão em requirements.txt
```bash
pip install -r requirements.txt
```

---

## Rodar o projeto
### FastAPI
Executar o comando para iniciar a aplicação FastAPI

```bash
uvicorn main --reload
```

### Docker e Redis
Executar os comandos para rodar o celery apartir de um container

Obetenha a imagem oficial do redis diretamente do Docker Hub
```bash
docker pull redis
```

Inicie o container redis
```bash
docker run -d -p 6379:6379 --name my-redis redis
```

Agora, o Redis deve estar em execução em um contêiner Docker e ouvindo na porta 6379, verifique
```bash
docker ps
```

Verifique se o redis está funcionando corretamente dentro no container, se tudo estiver certo o retorno será PONG.
```bash
docker exec -it my-redis redis-cli ping
```

### Celery
Inicie o worker do celery
```bash
celery -A tasks worker --loglevel=info --without-gossip --without-mingle --without-heartbeat -Ofair
```
