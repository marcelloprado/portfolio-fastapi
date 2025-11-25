from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import json
import os
#from flask import Flask, render_template

app = FastAPI()

# Serve os arquivos estáticos (CSS, JS, imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates jinja2
templates = Jinja2Templates(directory="templates")

# Função para carregar projetos do JSON
def carregar_projetos():
    caminho_arquivo = os.path.join("data", "projetos.json")
    if not os.path.exists(caminho_arquivo):
        return []  # Retorna lista vazia se o arquivo não existe
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            # Retorna lista vazia se o arquivo estiver vazio, senão carrega o JSON
            return json.load(f) if os.path.getsize(caminho_arquivo) > 0 else []
    except json.JSONDecodeError:
        return [] # Retorna lista vazia se o JSON for inválido
    


# Função para salvar projetos
def salvar_projetos(dados):
    path = os.path.join("data", "projetos.json")
    with open(path, "w", encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
        
class Projeto(BaseModel):
    titulo: str
    texto: str
    gif: str
    video: str
    capa: str
    descricao: str
    link: str
    link_repositorio: str


#? Rotas da aplicação

@app.get("/", response_class=HTMLResponse)
async def pagina_home(request: Request):
    projetos = carregar_projetos()
    return templates.TemplateResponse("home.html", {"request": request, "projetos": projetos})

@app.get("/sobre", response_class=HTMLResponse)
async def pagina_sobre(request: Request):
    return templates.TemplateResponse("sobre.html", {"request": request})

@app.get("/projeto/{projeto_id}", response_class=HTMLResponse)
async def projeto_detalhes(request: Request, projeto_id: int):
    projetos = carregar_projetos()
    projeto = next((p for p in projetos if p['id'] == projeto_id), None)
    if projeto is None:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return templates.TemplateResponse("projeto_detalhes.html", {"request": request, "projeto": projeto})
    
@app.get("/projetos", response_class=HTMLResponse)
async def pagina_projetos(request: Request):
    projetos = carregar_projetos()
    return templates.TemplateResponse("projetos.html", {"request": request, "projetos": projetos})

@app.get("/api/projetos")
def api_listar_projetos():
    return JSONResponse(content=carregar_projetos())

@app.post("/api/projetos")
def api_adicionar_projeto(projeto: Projeto):
    projetos = carregar_projetos()
    # Define o novo ID baseado no último projeto da lista
    novo_id = projetos[-1]['id'] + 1 if projetos else 1
    novo_projeto = projeto.model_dump()
    novo_projeto['id'] = novo_id
    projetos.append(novo_projeto)
    salvar_projetos(projetos)
    return {"status": "sucesso", "projeto": novo_projeto}

@app.get("/contato", response_class=HTMLResponse)
async def pagina_contato(request: Request):
    return templates.TemplateResponse("contato.html", {"request": request})

@app.get("/certificados", response_class=HTMLResponse)
async def pagina_certificados(request: Request):
    return templates.TemplateResponse("certificados.html", {"request": request})

#^ Iniciar o projeto com: uvicorn app:app --reload