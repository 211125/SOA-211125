from fastapi import FastAPI
from controller.User_Controller import router as UserRouter

app = FastAPI()

app.include_router(UserRouter)
