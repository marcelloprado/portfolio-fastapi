# 🚀 Portfólio em FastAPI  
Refatoração completa do meu portfólio, migrando da versão original em Flask para **FastAPI**, colocando em prática tudo o que aprendi no módulo recém-finalizado.  
Este projeto está sendo desenvolvido com foco em performance, organização, boas práticas e estrutura escalável.

---

## ✨ Sobre o Projeto
Este portfólio é uma aplicação web construída com **FastAPI + Jinja2**, criada para apresentar meus projetos, certificados (em desenvolvimento) e informações profissionais.

A versão atual é uma refatoração completa do meu portfólio anterior (feito em Flask), com melhorias em:

- Estrutura de arquivos e módulos  
- Organização das rotas  
- Performance do backend  
- Separação clara entre templates e lógica  
- Preparação para futura integração com banco de dados  

---

## 🧰 Tecnologias Utilizadas

### Backend
- **FastAPI**
- **Uvicorn**
- **Python 3.10+**
- **Jinja2** (para renderização dos templates)
- **Pydantic** (estrutura e validação de dados)

### Frontend
- **HTML5**
- **CSS3**
- **Bootstrap** (ou framework que estiver usando)
- **JavaScript**

---

## 📂 Estrutura do Projeto

portfolio-fastapi/  

├── app.py # Arquivo principal da aplicação  
├── static/ # Arquivos estáticos (css, js, imagens)  
│  
├── templates/ # Templates HTML (Jinja2)  
│ ├── index.html  
│ ├── projetos.html  
│ ├── certificados.html (em desenvolvimento)  
│ └── base.html  
│  
├── requirements.txt # Dependências do projeto  
└── README.md  
---

## ▶️ Como Rodar o Projeto Localmente

### **1. Clonar o repositório**
```bash
git clone https://github.com/marcelloprado/portfolio-fastapi.git
cd portfolio-fastapi
```

**2. Criar e ativar um ambiente virtual**
```bash
pip install -r requirements.txt
```

**3. Instalar dependências**
```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

**4. Iniciar o servidor**
```
uvicorn app:app --reload
```

**5. Acesse no navegador:**
```bash
Acesse seu local host
http://127.0.0.1:8000
```

🛠️ Features (até o momento)

* Página inicial personalizada  
* Página de projetos  
* Sistema de templates organizado  
* Estrutura pronta para expansão (certificados, contatos, banco de dados)  
* Backend estruturado com FastAPI  

📌 Próximos passos

* Criar a página de certificados  
* Implementar banco de dados para armazenar projetos, certificados e skills  
* Criar API interna para alimentar o frontend  
* Melhorias no design e responsividade  
* Deploy completo (Render / Railway)  

👤 Autor: Marcello Prado  
Desenvolvedor Backend & Frontend  
Buscando a evolução constante através de projetos reais 🚀
