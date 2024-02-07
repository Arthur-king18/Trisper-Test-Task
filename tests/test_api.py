from httpx import AsyncClient
from sqlalchemy import insert, select

from app.publication.models import Publication
from app.user.models import User
from tests.conftest import async_session_maker


async def test_create_user(ac: AsyncClient):
    response = await ac.post("/api/v1/users", json={
        "email": "testmail@gmail.com",
        "password1": "12345678",
        "password2": "12345678",
        "username": "Test",
        "full_name": "Test Name",
    })

    assert response.status_code == 200


async def test_add_publication(ac: AsyncClient):
    async with async_session_maker() as session:
        query = insert(User).values(
            email="testmail@gmail.com",
            password="12345678",
            username="Test",
            full_name="Test name",
        )
        await session.execute(query)
        await session.commit()

        query = insert(Publication).values(text="Hello world", user_id=1)
        await session.execute(query)
        await session.commit()

        query = select(Publication)
        result = await session.execute(query)

        for publication in result.scalars().all():
            assert publication.text == "Hello world", "Публикация не добавилась"

