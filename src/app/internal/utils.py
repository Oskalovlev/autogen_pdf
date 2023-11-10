import requests
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from src.app.core.config import settings


def compilation_pdf(list_method: list):
    pdf_filename = "report.pdf"
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)
    pdfmetrics.registerFont(TTFont("Verdana", "Verdana.ttf"))
    pdf.setFont("Verdana", 8)
    x = 80
    y = 750
    for item in list_method:
        pdf.drawString(x, y, item)
        y -= 10
        if y == 0:
            x += 100
            y += 750
            pdf.drawString(x, y, item)
            y -= 10
    pdf.save()


def get_id_user(id_user):
    request_user = requests.get(
        f"https://{settings.parser.host}/"
        f"method/{settings.parser.method_get_user}?"
        f"user_id={id_user}&"
        f"fields=contacts,counters&"
        f"access_token={settings.parser.vk_token.get_secret_value()}&"
        f"v={settings.parser.version}"
    ).json()

    return request_user
