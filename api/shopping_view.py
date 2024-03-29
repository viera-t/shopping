from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter()

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify the encoding as utf-8
        content = file.read()
    return content

@router.get("/shopping_view/index", response_class=HTMLResponse)
def read_html():
    html_file_path = "web/shoppingtrends/index.html"
    html_content = read_html_file(html_file_path)
    return html_content

@router.get("/shopping_view/insert", response_class=HTMLResponse)
def read_html():
    html_file_path = "web/shoppingtrends/insert.html"
    html_content = read_html_file(html_file_path)
    return html_content

@router.get("/shopping_view/update", response_class=HTMLResponse)
def read_html():
    html_file_path = "web/shoppingtrends/update.html"
    html_content = read_html_file(html_file_path)
    return html_content

@router.get("/shopping_view/predict", response_class=HTMLResponse)
def read_html():
    html_file_path = "web/shoppingtrends/predict.html"
    html_content = read_html_file(html_file_path)
    return html_content