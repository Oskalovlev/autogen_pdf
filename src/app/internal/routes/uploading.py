from fastapi import APIRouter
from fastapi.responses import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

router = APIRouter(prefix="/download")


@router.get("/report")
async def report():
    # Создание нового PDF-файла с помощью ReportLab
    pdf_filename = "report.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Добавление текста и других элементов в PDF-файл
    pdfmetrics.registerFont(TTFont("Verdana", "Verdana.ttf"))
    c.setFont("Verdana", 8)
    s = "Пример отчета PDF"
    c.drawString(100, 750, s)

    # Сохранение и закрытие PDF-файла
    c.save()

    # Возврат сгенерированного PDF-файла на FastAPI
    return FileResponse(
        path=pdf_filename, filename=pdf_filename, media_type="application/pdf"
    )
