from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="IOS-RPMP Backend")

# ✅ CORS MUST BE DEFINED IMMEDIATELY
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ IMPORT ROUTES ONLY AFTER APP + CORS EXIST
from backend.api_routes import router
app.include_router(router)
