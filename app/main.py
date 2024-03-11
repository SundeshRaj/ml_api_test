# Author: Sundesh
# Date:   3/11/2024
# Description:

from fastapi import FastAPI
from app.routers import inference, training, validation, performance

app = FastAPI(title="ML Models API", version="1.0", description="An API for machine learning model operations including training, inference, validation, and performance analysis.")

# Include the routers from the 'routers' module
app.include_router(inference.router, tags=["Inference"], prefix="/inference")
app.include_router(training.router, tags=["Training"], prefix="/training")
app.include_router(validation.router, tags=["Validation"], prefix="/validation")
app.include_router(performance.router, tags=["Performance"], prefix="/performance")
