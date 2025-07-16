from fastapi import FastAPI
from biobank_manager.controllers.participants import router as participant_router

app = FastAPI(
  title="Biobank Manager API",
  version="1.0.0",
  description="Biobank manager API for managing biobank data",
)
app.include_router(participant_router)

@app.get("/")
def home():
  return {"message": f"Hello to {app.title}"}