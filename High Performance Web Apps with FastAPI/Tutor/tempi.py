import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/{name}", response_class=HTMLResponse)
async def index(name):
    ret='''
<html>
<body>
<h2 style="text-align: center;">Hello {}!</h2>
</body>
</html>
'''.format(name)
    return HTMLResponse(content=ret)




if __name__ == '__main__':
    uvicorn.run("tempi:app", host="0.0.0.0", port=8000, reload=True)