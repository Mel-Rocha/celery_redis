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
Executar o comando para iniciar a aplicação FastAPI

```bash
uvicorn main --reload
```

---

Executar o comando para iniciar o worker do Celery

```bash
celery -A tasks worker --loglevel=info
```