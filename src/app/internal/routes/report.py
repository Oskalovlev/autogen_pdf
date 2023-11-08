import pdfkit
import requests
from fastapi import APIRouter
from vk_api import VkApi

# from src.app.core.config import settings

router = APIRouter(prefix="/report", tags=["report"])


# @router.get("/hello")
# def hello():
#     return {"hello": "world"}


# @router.get("/parser/{user_id}")
# async def parse_user(user_id: str):
#     Код для извлечения информации о пользователе и связанных контактах из VK
#     access_token = settings.base.VK_TOKEN
#     access_token = auth.exchangeSilentAuthToken
#     user_data = requests.get(
#         f"https://api.vk.com/method/users.get?user_ids={user_id}&"
#         f"fields=offline,friends,groups&access_token={access_token}&v=5.131"
#     ).json()
#     Код для обработки и извлечения информации о пользователях и их группах
#     first_name = user_data["response"][0]["first_name"]
#     last_name = user_data["response"][0]["last_name"]
#     subscribed_groups = []

#     for contact in contacts:
#         if contact["type"] == "group" and contact.get("subtype") == "page":
#             subscribed_groups.append(contact["id"])

#     return {"subscribed_groups": subscribed_groups}
#     return {"message": "Парсинг завершен!"}


@router.post("/generate_report")
async def generate_report(user_id: int):
    # Здесь подставьте свои данные авторизации ВКонтакте
    vk_session = VkApi(login="<YOUR_LOGIN>", password="<YOUR_PASSWORD>")
    vk_session.auth()
    vk = vk_session.get_api()

    # Получаем информацию о пользователя
    user = vk.users.get(user_ids=user_id)[0]
    user_name = user["first_name"] + " " + user["last_name"]

    # Получаем список подписчиков и групп пользователя
    followers = vk.users.getFollowers(user_id=user_id, count=1000)["items"]
    groups = vk.groups.get(user_id=user_id, extended=1, fields="name")["items"]

    # Формируем отчет в виде HTML
    html = f"""
    <h1>Отчет о пользователе {user_name}</h1>
    <h2>Подписчики:</h2>
    <ul>
    """
    for follower_id in followers:
        follower = vk.users.get(user_ids=follower_id)[0]
        html += f"<li>{follower['first_name']} {follower['last_name']}</li>"

    html += "</ul>"
    html += "<h2>Группы:</h2><ul>"
    for group in groups:
        html += f"<li>{group['name']}</li>"

    html += "</ul>"

    # Создаем PDF из HTML
    pdfkit.from_string(html, "report.pdf")

    return {
        "message": "Отчет успешно сгенерирован и сохранен в файле report.pdf"
    }


host = "api.vk.com"
token = (
    "vk1.a.ksgTl6eq5jPdI0uOfc14ogS7cxztf7Z6hDFZc5OmCgjyumggc_"
    "IqtDwUKA8YwOAKM0aVsYk94q4a5PVLXNe2xcrhitUluN-9adtLXCTXt3vy"
    "6uW6tuRtCjJM1ZoK-uLj7LM-NkKK8mbvQv3xhqHDP0Z_gTwDsdD2-sq87Yx"
    "RAE3ipRU80mFXUzfJZ4e-1yhnEnOn5dwMeeZ-VfC9eo2XxQ"
)
user_id = "763905368"

method_get_friends = "friends.get"
order = "hints"
fields_friend = "contacts"
name_case = "nom"

method_get_group = "groups.get"
filter_group = "groups,publics"
fields_group = ""
version = "v5.154"


request_friends = requests.get(
    f"https://{host}/method/{method_get_friends}?"
    f"user_ids={user_id}&"
    f"order={order}&"
    f"fields={fields_friend}&"
    f"name_case={name_case}&"
    f"access_token={token}&"
    f"{version}"
).json()

request_groups = requests.get(
    f"https://{host}/method/{method_get_group}?"
    f"user_ids={user_id}&"
    f"extended=1&"
    f"filter={filter_group}&"
    f"access_token={token}&"
    f"{version}"
).json()


# for req in request:
#     req = request.format(host, method_get_friends, user_id, )
