# Daily Diet API 🍽️

API REST para controle de dieta diária desenvolvida em Python com Flask, permitindo cadastro de usuários e gerenciamento de refeições.

## 📋 Funcionalidades

### 👤 Usuários
- Criar usuário
- Buscar usuário por ID ou email
- Listar todos os usuários
- Atualizar dados do usuário
- Deletar usuário

### 🍽️ Refeições
- Criar refeição
- Buscar refeição por ID
- Listar refeições do usuário
- Filtrar refeições dentro/fora da dieta
- Atualizar refeição
- Deletar refeição
- Estatísticas da dieta do usuário

### 📊 Estatísticas
- Total de refeições registradas
- Refeições dentro da dieta
- Refeições fora da dieta
- Melhor sequência de refeições na dieta
- Percentual de aderência à dieta

## 🛠️ Tecnologias

- **Python 3.12**
- **Flask** - Framework web
- **SQLite** - Banco de dados
- **pytest** - Testes unitários

## 🏗️ Arquitetura

```
src/
├── controllers/     # Lógica de negócio
├── models/         # Repositórios e conexão com DB
├── validators/     # Validação de dados
├── utils/          # Respostas HTTP padronizadas
└── main/
    ├── routes/     # Rotas da API
    └── server/     # Configuração do servidor
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.12+
- pip

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/davioliveiraes/daily_diet_api.git
cd daily_diet_api
```

2. **Crie e ative o ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**
```bash
python run.py
```

A API estará disponível em `http://localhost:3000`

## 📚 Endpoints

### 👤 Usuários
```http
POST   /users              # Criar usuário
GET    /users              # Listar usuários
GET    /users/{id}         # Buscar por ID
GET    /users/email/{email} # Buscar por email
PUT    /users/{id}         # Atualizar usuário
DELETE /users/{id}         # Deletar usuário
```

### 🍽️ Refeições
```http
POST   /users/{user_id}/meals           # Criar refeição
GET    /users/{user_id}/meals           # Listar refeições
GET    /users/{user_id}/meals/{meal_id} # Buscar refeição
GET    /users/{user_id}/meals/on-diet   # Refeições na dieta
GET    /users/{user_id}/meals/off-diet  # Refeições fora da dieta
GET    /users/{user_id}/diet-statistics # Estatísticas
PUT    /users/{user_id}/meals/{meal_id} # Atualizar refeição
DELETE /users/{user_id}/meals/{meal_id} # Deletar refeição
```

### 🔍 Health Check
```http
GET    /health             # Status da API
```

## 📝 Exemplo de Uso

### Criar usuário:
```json
POST /users
{
  "name": "Harvey Specter",
  "email": "harvey@example.com"
}
```

### Criar refeição:
```json
POST /users/{user_id}/meals
{
  "name": "Almoço",
  "description": "Frango grelhado com salada",
  "datetime": "2025-01-15T12:30:00",
  "is_on_diet": 1
}
```

## 🧪 Executar Testes

```bash
# Todos os testes
python -m pytest -s -v

# Testes específicos
python -m pytest -s -v src/controllers/users_controller_test.py
python -m pytest -s -v src/main/routes/routes_test.py
```

## 📦 Estrutura do Banco

**Tabelas:**
- `users` - Dados dos usuários
- `meals` - Refeições cadastradas  
- `user_meals` - Relacionamento usuário-refeição

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

Desenvolvido por [Davi Oliveira](https://github.com/davioliveiraes) 🚀