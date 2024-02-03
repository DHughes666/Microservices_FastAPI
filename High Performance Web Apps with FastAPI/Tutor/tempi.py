import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates(directory="templates")

@app.get("/{name}", response_class=HTMLResponse)
async def index(request: Request, name: str):
    return template.TemplateResponse(
        "hello.html",{"request": request, "name": name})

@app.get("/employee/{name}/{salary}", response_class=HTMLResponse)
async def employee(request: Request, name: str, salary: int):
    data = {"name": name, "salary": salary}
    return template.TemplateResponse(
        "employee.html", {"request": request, "data": data})

@app.get("/profile/", response_class=HTMLResponse)
async def info(request: Request):
    data = {"name": "Rondha", 
            "langs": ["Python", "Java", "PHP", "Swift", "C++"]}
    return template.TemplateResponse(
        "profile.html", {"request": request, "data": data})

if __name__ == '__main__':
    uvicorn.run("tempi:app", host="0.0.0.0", port=8000, reload=True)