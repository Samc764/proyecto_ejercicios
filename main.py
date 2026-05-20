from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# ──────────────────────────────────────────────
# EJERCICIO 9 – /temperatura/{grados}
# Clasifica la temperatura en: Frío, Templado, Caluroso o Extremo
# ──────────────────────────────────────────────
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


# ──────────────────────────────────────────────
# EJERCICIO 21 – /vocales/{frase}
# Recibe una frase y la convierte en lista de letras.
# La plantilla resalta las vocales con <strong>.
# ──────────────────────────────────────────────
@app.get("/vocales/{frase:path}", response_class=HTMLResponse)
async def vocales(request: Request, frase: str):
    # Convertir la frase en lista de letras (incluyendo espacios)
    letras = list(frase)

    return templates.TemplateResponse(
        "vocales.html",
        {
            "request": request,
            "frase": frase,
            "letras": letras,
        }
    )


# ──────────────────────────────────────────────
# EJERCICIO 33 – /pendientes
# Muestra tareas separadas en "pendientes" y "completadas".
# Usa for-else para mostrar mensaje si una sección queda vacía.
# ──────────────────────────────────────────────
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
