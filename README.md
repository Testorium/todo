# Todo app


---
### Как запустить

Клонируем репозиторий
```
git clone https://github.com/Testorium/todo.git
cd todo
```

Просто запускаем `docker compose`

```
docker compose up -d
```

Фронт будет доступен по адресу:

[http://localhost:3000](http://localhost:3000)


А бэк, если хотите заглинуть в сваггер, тут:

[http://localhost:8000/docs](http://localhost:8000/docs)



> **Note:** насчет "приведите пример запросов" не понял :(

но все же вот некоторые запросы


---

```
POST /auth/register
Content-Type: application/json

{
  "username": "username",
  "password": "password",
  "firstName": "John",
  "lastName": "Weak"
}

```
---

```
POST /auth/login
Content-Type: application/json

{
  "username": "username",
  "password": "password"
}
```