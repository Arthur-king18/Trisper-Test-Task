# Trisper Test Task

# Features
- Асинхронная SQLAlchemy сессия
- Кастомные юзер классы
- Зависимость верхнего уровня
- Зависимости для конкретных разрешений
- Параллельное создание публикаций и голосование

### SQLAlchemy for asyncio context

```python
from core.db import Transactional, session


@Transactional()
async def create_user(self):
    session.add(User(email="padocon@naver.com"))
```

Не надо использовать `commit()`. `Transactional` class всё сделает за тебя.

### Multiple databases
 
Перейди `core/config.py` и можешь редактировать `WRITER_DB_URL` и `READER_DB_URL` в конфигурационном классе.

### Custom user for authentication

```python
from fastapi import Request


@home_router.get("/")
def home(request: Request):
    return request.user.id
```

**Примечание. Тебе нужно передать токен jwt через заголовок, например `Authorization: Bearer 1234`**

Пользовательский класс пользователя автоматически декодирует токен заголовка и сохраняет информацию о пользователе в `request.user`

Если ты хочешь изменить пользовательский класс пользователя, тебе необходимо обновить файлы ниже.

1. `core/fastapi/schemas/current_user.py`
2. `core/fastapi/middlewares/authentication.py`

## Dependencies for specific permissions

Права `IsAdmin`, `IsAuthenticated`, `AllowAll` уже реализованы.
 
```python
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAdmin,
)


user_router = APIRouter()


@user_router.get(
    "",
    response_model=List[GetUserListResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAdmin]))],  # HERE
)
async def get_user_list(
    limit: int = Query(10, description="Limit"),
    prev: int = Query(None, description="Prev ID"),
):
    pass
```
Можно вставить разрешение через `dependencies` аргумент.

## Install dependencies

```
pip install poetry

poetry shell && poetry install
```

## ENV
Создай файл `.env.local`. Скопируй содержимое `.env.example` и подставь свои переменные. 
Готово!

## How use
1. ```python3 main.py --env local|dev|prod --debug```
2. Переходишь на http://localhost:8000/docs#/
3. Создаёешь пользователя
4. Логинишься и получаешь токен
5. Нажимаешь на замочек с надписью **Authorize**
6. Вводишь `Bearer полученный токен`
7. Ты авторизован, можешь делать всё, что хочешь !!!

![Иллюстрация к проекту](https://github.com/Arthur-king18/Trisper-Test-Task/main/image/image.png)

## Tests

### Run
`pytest -v tests/`

![Тесты](https://github.com/Arthur-king18/Trisper-Test-Task/main/image/test.png)


# Спасибо, что дочитал до конца!