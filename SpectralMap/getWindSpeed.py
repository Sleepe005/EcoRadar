import requests
import json

# Создаём необходимые заголовки
head = {'X-Yandex-API-Key' : '11191b39-0d3b-48f0-95d9-6c1fa2d6fe60'}
# Делаем запрос
r = requests.get("https://api.weather.yandex.ru/v2/informers?lat=44.69492&lon=37.78357", headers=head)
# Загружаем ответ в json (python dict)
json_data = json.loads(r.text)
# Выводим нужные данные
print(json_data['fact']['temp'])