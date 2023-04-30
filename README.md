Запуск: 
```
docker compose build
docker compose up -d
```

Подключение к прокси:
```
nc -u 127.0.0.1 2000
```

Запросы:
```
get_result <FORMAT>
```
Допустимые варианты для FORMAT: NATIVE, XML, JSON, PROTO, AVRO, YAML, MSGPACK
Регистр не имеет значения
