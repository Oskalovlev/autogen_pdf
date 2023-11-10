import requests
from fastapi import APIRouter
from fastapi.responses import FileResponse

from src.app.core.config import settings
from src.app.internal.utils import compilation_pdf, get_id_user

router = APIRouter(prefix="/report", tags=["report"])


@router.get("/info/{id_user}")
async def report_info(id_user):

    info = get_id_user(id_user=id_user)["response"]

    info_list = []
    for item in info:
        name = item["first_name"] + " " + item["last_name"]
        info_list.append(name)
        counters = item["counters"]
        for i, n in counters.items():
            s = str(i) + ": " + str(n)
            info_list.append(s)

        compilation_pdf(list_method=info_list)

        pdf_filename = "report.pdf"

    return FileResponse(
        path=pdf_filename, filename=pdf_filename, media_type="application/pdf"
    )


@router.get("/friends/{id_user}")
async def report_friends(id_user):

    user_id = get_id_user(id_user=id_user)["response"][0]["id"]

    request_friends = requests.get(
        f"https://{settings.parser.host}/"
        f"method/{settings.parser.method_get_friends}?"
        f"user_id={user_id}&"
        # f"order={order}&"
        f"fields={settings.parser.fields_friend}&"
        # f"name_case={name_case}&"
        f"access_token={settings.parser.vk_token.get_secret_value()}&"
        f"v={settings.parser.version}"
    ).json()

    friends = request_friends["response"]["items"]

    friend_list = []
    for friend in friends:
        friend_name = friend["first_name"] + " " + friend["last_name"]
        friend_list.append(friend_name)

        compilation_pdf(list_method=friend_list)

        pdf_filename = "report.pdf"

    return FileResponse(
        path=pdf_filename, filename=pdf_filename, media_type="application/pdf"
    )


@router.get("/groups/{id_user}")
async def report_groups(id_user):

    user_id = get_id_user(id_user=id_user)["response"][0]["id"]

    request_groups = requests.get(
        f"https://{settings.parser.host}/"
        f"method/{settings.parser.method_get_group}?"
        f"user_id={user_id}&"
        f"extended=1&"
        f"filter={settings.parser.filter_group}&"
        f"access_token={settings.parser.vk_token.get_secret_value()}&"
        f"v={settings.parser.version}"
    ).json()

    groups = request_groups["response"]["items"]

    group_list = []
    for group in groups:
        group_name = group["name"]
        group_list.append(group_name)

        pdf_filename = "report.pdf"
        compilation_pdf(list_method=group_list)

    return FileResponse(
        path=pdf_filename, filename=pdf_filename, media_type="application/pdf"
    )
