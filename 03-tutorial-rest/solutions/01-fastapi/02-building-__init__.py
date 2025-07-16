from fastapi import FastAPI

app = FastAPI(
  title="Biobank Manager API",
  version="1.0.0",
  description="Biobank manager API for managing biobank data",
)

@app.get("/")
def home():
  return {"message": f"Hello to {app.title}"}