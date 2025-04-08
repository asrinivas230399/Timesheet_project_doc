from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from middleware.responsive_design_middleware import ResponsiveDesignMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Add GZip middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Add Responsive Design middleware
app.add_middleware(ResponsiveDesignMiddleware)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/project")
async def get_project_details():
    return {"project": "FastAPI Example", "version": "1.0"}

@app.get("/task")
async def get_task_updates():
    return {"task": "Update routing", "status": "Completed"}