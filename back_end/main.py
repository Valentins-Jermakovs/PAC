#
# Šī programma ir projekta PAC servera puse
# Tā nepieciešama, lai front-end spētu komunicēt ar datu bāzi
# izmantojot REST API servisus
#
# FastAPI dokumentācija - https://fastapi.tiangolo.com
# Automātiski ģenerēta swagger dokumentācija - http://127.0.0.1:8000/docs
#
# Lai aktivēt virtuālo vidi:
# source "/home/engineer/Рабочий стол/PAC/back_end/myenv/bin/activate"
# Lai iedarbināt FastAPI servera, ierakstiet komandu "uvicorn main:app --reload"
#

# Tiek importētas FastAPI biblioteka
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from pathlib import Path

# Tiek izveidots FastAPI objekts (programmas ieejas punkts)
app = FastAPI()

# =========================================================================
# Montējam static files un ikonu
# =========================================================================
# Montējam static files - ikonu
app.mount("/static", StaticFiles(directory="static"), name="static")
# Maršruts - ikonu
@app.get("/favicon.ico")
async def favicon():
    return FileResponse(Path(__file__).parent / "static" / "favicon.ico")
# =========================================================================

# =========================================================================
#                           FastAPI serviss
# =========================================================================

# This is for active branch

@app.get("/")
async def root():
    return {"message": "Hello, world!"}
