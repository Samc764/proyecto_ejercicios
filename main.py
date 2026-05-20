from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from mangum import Mangum

app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent


templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/temperatura/{grados}", response_class=HTMLResponse)
async def temperatura(request: Request, grados: float):
    if grados < 10:
        categoria = "Frío"
    elif grados < 25:
        categoria = "Templado"
    elif grados < 35:
        categoria = "Caluroso"
    else:
        categoria = "Extremo"

    return templates.TemplateResponse(
        "temperatura.html",
        {
            "request": request,
            "grados": grados,
            "categoria": categoria,
        }
    )


@app.get("/vocales/{frase:path}", response_class=HTMLResponse)
async def vocales(request: Request, frase: str):
    letras = list(frase)

    return templates.TemplateResponse(
        "vocales.html",
        {
            "request": request,
            "frase": frase,
            "letras": letras,
        }
    )


@app.get("/pendientes", response_class=HTMLResponse)
async def pendientes(request: Request):
    tareas = [
        {"descripcion": "Estudiar Jinja2 y plantillas", "completada": True},
        {"descripcion": "Hacer ejercicios de FastAPI",  "completada": False},
        {"descripcion": "Revisar apuntes de Python",    "completada": True},
        {"descripcion": "Entregar tarea del grupo 9",   "completada": False},
        {"descripcion": "Leer documentación oficial",   "completada": False},
        {"descripcion": "Practicar ciclos for en HTML", "completada": True},
        {"descripcion": "Subir código a GitHub",        "completada": False},
        {"descripcion": "Probar la ruta /pendientes",   "completada": True},
    ]

    return templates.TemplateResponse(
        "pendientes.html",
        {
            "request": request,
            "tareas": tareas,
        }
    )


handler = Mangum(app)