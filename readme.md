# Описание API

## Отправка кода активации

**URL:** `http://localhost:8000/send_activation_code/`

**Метод:** POST

**Параметры запроса:**
```json
{
    "phone_number": "+1234567890"
}
Ответ:

json
{
    "code": "123456"
}
Активация пользователя
URL: http://localhost:8000/activate_user/

Метод: POST

Параметры запроса:

json
Copy code
{
    "codde": "123456"
}
Ответ:

json
{
    "messages": "your code activated successfully"
}
Получение списка пользователей с активированными инвайт-кодами
URL: http://localhost:8000/users_with_invites/

Метод: GET

Ответ:

json
[
    {
        "phone_number": "+1234567890",
        "invite_code": "ABCDEF",
        "activated_invite_code": "123456"
    },
    {
        "phone_number": "+0987654321",
        "invite_code": "ZYXWVU",
        "activated_invite_code": "654321"
    }
]