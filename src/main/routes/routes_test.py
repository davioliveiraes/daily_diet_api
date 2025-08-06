import pytest # type: ignore
import json
import uuid
from src.main.server.server import app

@pytest.fixture
def client():
   """Cliente de teste do Flask"""
   app.config['TESTING'] = True
   with app.test_client() as client:
      yield client

user_id = None
meal_id = None

@pytest.mark.skip(reason="teste de integracao")
def test_01_health_check(client):
   """Testa o health check da API"""
   response = client.get('/')

   assert response.status_code == 200
   data = json.loads(response.data)
   assert data['status'] == 'healthy'
   print(f"Health check: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_02_create_user(client):
   """Testa criacao de usuario"""
   user_data = {
      "name": "Mike Ross",
      "email": f"mike_{str(uuid.uuid4())[:8]}@gmail.com"
   }

   response = client.post('/users', data=json.dumps(user_data), content_type='application/json')

   assert response.status_code == 201
   data = json.loads(response.data)
   assert data['success'] == True
   assert 'data' in data

   global user_id
   user_id = data['data']['id']
   print(f"User created: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_03_get_user_by_id(client):
   """Testa busca de usuario por ID"""
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "5c3b532c-8c7b-436b-8053-3ccdd9a7eea9"

   if not user_id:
      print("Skipping: user_id not available")
      return

   response = client.get(f'/users/{user_id}')

   assert response.status_code == 200
   data = json.loads(response.data)
   assert data['success'] == True
   assert data['data']['id'] == user_id
   print(f"User found: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_04_get_all_users(client):
   """Testa listagem de todos os usuarios"""
   response = client.get('/users')

   assert response.status_code == 200
   data = json.loads(response.data)
   assert data['success'] == True
   assert len(data['data']) >= 1
   print(f"Users found: {len(data['data'])}")
   print("\nUsers Data:")
   print(json.dumps(data['data'], indent=2, ensure_ascii=False))

@pytest.mark.skip(reason="teste de integracao")
def test_05_create_meal(client):
   """Testa criacao de refeicao"""
   # Exemplo de pegar especificamente o user_id cadastrado no banco para atualizar!
   # user_id = "2feb7cbb-01db-48b9-bc8a-202726ccc7c4"

   if not user_id:
      print("Skipping: user_id not available")
      return

   meal_data = {
      "user_id": user_id,
      "name": "Salada Verde",
      "description": "Salada com alface, tomate e cenoura",
      "datetime": "2025-06-30 12:00:00",
      "is_on_diet": 1
   }

   response = client.post('/meals', data=json.dumps(meal_data), content_type='application/json')

   assert response.status_code == 201
   data = json.loads(response.data)
   assert data['success'] == True

   global meal_id
   meal_id = data['data']['id']
   print(f"Meal created: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_06_get_meal_by_id(client):
   """Testa busca de refeicao por ID"""
   # Exemplo de pegar especificamente o user_id e meal_id cadastrado no banco para atualizar!
   # user_id = "2feb7cbb-01db-48b9-bc8a-202726ccc7c4"
   # meal_id = "95fd12ef-ec70-421b-9456-2e2f3541c35c"

   if not user_id or not meal_id:
      print("Skipping: user_id not available")
      return
   
   response = client.get(f'/meals/{meal_id}/user/{user_id}')

   assert response.status_code == 200
   data = json.loads(response.data)
   assert data['success'] == True
   assert data['data']['id'] == meal_id
   print(f"Meal found: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_07_get_meals_by_user(client):
   """Testa listagem de refeicoes do usuario"""
   # Exemplo de pegar especificamente o user_id e meal_id cadastrado no banco para atualizar!
   # user_id = "2feb7cbb-01db-48b9-bc8a-202726ccc7c4"

   if not user_id:
      print("Skipping: user_id not available")
      return
   
   response = client.get(f"/meals/user/{user_id}")

   assert response.status_code == 200
   data = json.loads(response.data)
   assert data['success'] == True
   assert len(data['data']) >= 1
   print(f"User meals found: {len(data['data'])}")
   print("\nMeals Data:")
   print(json.dumps(data['data'], indent=2, ensure_ascii=False))

@pytest.mark.skip(reason="teste de integracao")
def test_08_get_diet_statistics(client):
   """Testa estatisticas da dieta"""
   # Exemplo de pegar especificamente o user_id e meal_id cadastrado no banco para atualizar!
   # user_id = "2feb7cbb-01db-48b9-bc8a-202726ccc7c4"

   if not user_id:
      print("Skipping: user_id not available")
      return
   
   response = client.get(f'/meals/user/{user_id}/statistics')

   assert response.status_code == 200
   data = json.loads(response.data)
   assert data['success'] == True
   assert 'total_meals' in data['data']
   print(f"Diet statistics: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_09_update_meal(client):
   """Testa atualizacao de refeicao"""
   # Exemplo de pegar especificamente o user_id e meal_id cadastrado no banco para atualizar!
   # user_id = "2feb7cbb-01db-48b9-bc8a-202726ccc7c4"
   # meal_id = "95fd12ef-ec70-421b-9456-2e2f3541c35c"

   if not user_id or not meal_id:
      print("Skipping: user_id or meal_id not available")
      return
   
   update_data = {
      "name": "Vitamina Verde",
      "description": "vitamina verde detoz com espinafre, maca verde, pepino, gengibre e limao",
      "datetime": "2025-07-25 17:00:00",
      "is_on_diet": 1
   }

   response = client.put(f"/meals/{meal_id}/user/{user_id}", data=json.dumps(update_data), content_type='application/json')

   assert response.status_code == 200
   data = json.loads(response.data)
   assert data['success'] == True
   assert data['data']['name'] == "Vitamina Verde"
   print(f"Meal updated: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_10_delete_meal(client):
   """Testa delecao de refeicao"""
   # Exemplo de pegar especificamente o user_id e meal_id cadastrado no banco para atualizar!
   # user_id = "5c3b532c-8c7b-436b-8053-3ccdd9a7eea9"
   # meal_id = "d5a362c3-6ded-45a2-b273-1bb356e7378b"

   if not user_id or not meal_id:
      print("Skipping: user_id or meal_id not available")
      return

   response = client.delete(f"/meals/{meal_id}/user/{user_id}")

   assert response.status_code == 200
   data = json.loads(response.data)
   assert data['success'] == True
   print(f"Meal deleted: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_12_create_user_invalid_email(client):
   """Testa craicao do usuario com email invalido"""
   user_data = {
      "name": "Alex",
      "email": "email-invalido"
   }

   response = client.post('/users', data=json.dumps(user_data), content_type='application/json')

   assert response.status_code == 400
   data = json.loads(response.data)
   assert data['success'] == False
   print(f"Invalid email test: {data}")

@pytest.mark.skip(reason="teste de integracao")
def test_13_get_user_not_found(client):
   """Testa busca de usuario inexistente"""
   fake_id = str(uuid.uuid4())

   response = client.get(f'/users/{fake_id}')

   assert response.status_code == 404
   data = json.loads(response.data)
   assert data['success'] == False
   print(f"User not found test: {data}")