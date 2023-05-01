### Запуск (из корня репозитория): 

```
docker compose build
docker compose up -d
```

### Подключение к прокси:

```
nc -u localhost 2000
```

### Запросы:

```
get_result <FORMAT>
```

##### Допустимые варианты для FORMAT:
`NATIVE`, `XML`, `JSON`, `PROTO`, `AVRO`, `YAML`, `MSGPACK` - регистр не имеет значения
