from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Welcome to My FastAPI Server</h1>
        <p>This is the home page of the server.</p>
        <p>You can navigate to other pages or APIs from here.</p>
    </body>
    </html>
    """
@app.get("/fhtrust.yaml")
async def get_yaml():
    file_path = "fhtrust.yaml"
    return FileResponse(file_path)
