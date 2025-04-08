from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.middleware.responsive_design_middleware import ResponsiveDesignMiddleware
from app.database import SessionLocal, engine
from app import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add GZip middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Add Responsive Design middleware
app.add_middleware(ResponsiveDesignMiddleware)

templates = Jinja2Templates(directory="app/templates")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("project_details.html", {"request": request, "device_type": request.headers.get('X-Device-Type', 'desktop')})

@app.get("/project", response_class=HTMLResponse)
async def get_project_details(request: Request, db: Session = Depends(get_db)):
    project = crud.get_project(db)
    return templates.TemplateResponse("project_details.html", {"request": request, "device_type": request.headers.get('X-Device-Type', 'desktop'), "project": project})

@app.get("/task")
async def get_task_updates():
    return {"task": "Update routing", "status": "Completed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
