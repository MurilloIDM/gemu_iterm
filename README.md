# 🎯 Gemu iTerm

**Gemu iTerm** é um sistema de gerenciamento de movimentações financeiras executado diretamente no terminal, com interface rica, limpa e responsiva usando [Rich](https://rich.readthedocs.io/).

> 💡 Desenvolvido para auxiliar no controle de entradas, saídas, saldos e fluxo financeiro, com persistência de dados em PostgreSQL.

---

## ✨ Funcionalidades

- ✅ Cadastro de movimentações financeiras
- ✅ Listagem de movimentações por período e banco
- ✅ Resumo financeiro com saldo total
- ✅ Filtros por tipo (entrada/saída) e período
- ✅ Exclusão de movimentações
- 🚧 Edição de movimentações (em desenvolvimento)
- 🧹 Interface limpa, elegante e fácil no terminal usando Rich

---

## 💻 Tecnologias

- 🐍 **Python 3.11+**
- 🐘 **PostgreSQL** (Banco de dados relacional)
- 🔗 **psycopg2** (Driver PostgreSQL para Python)
- 🎨 **Rich** (Interface bonita no terminal)
- 🔐 **dotenv** (Configurações via variáveis de ambiente)

---

## 🗂️ Estrutura de Pastas

```
gemu_iterm/
├── src/
│   ├── config/         # Configuração e conexão com o banco de dados
│   ├── use_cases/      # Lógica de negócio e manipulação dos dados
│   ├── utils/          # Funções auxiliares (validações, limpar tela, etc.)
│   ├── views/          # Interface no terminal (menus, formulários, tabelas)
│   └── main.py         # Arquivo principal que executa a aplicação
├── .env                # Arquivo de variáveis de ambiente
├── .gitignore          # Padrões ignorados pelo git
├── README.md           # Documentação do projeto
├── requirements.txt    # Dependências do projeto
```

---

## 🏗️ Banco de Dados

Banco: **PostgreSQL**

---

## 🚀 Como rodar o projeto

### 1️⃣ Clone o repositório:

```bash
git clone https://github.com/MurilloIDM/gemu_iterm.git
cd gemu_iterm
```

### 2️⃣ Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

### 5️⃣ Execute a aplicação:

```bash
python main.py
```

---

## 🧠 Autor

Feito com 💙 por [Murillo IDM](https://github.com/MurilloIDM)

---

## 📜 Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE) para mais informações.
