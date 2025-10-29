from fastapi import FastAPI
from auth_router import router
from userRouter import UserRouter
from contactRouter import ContactRouter
from chatRouter import ChatRouter
from messageRouter import MessageRouter
from fastapi.middleware.cors import CORSMiddleware
from middlewares.loggingMiddleware import LoggingMiddleware
from middlewares.rateLimitingMiddleware import RateLimitingMiddleware 
from fastapi.responses import JSONResponse
from fastapi.requests import Request

app = FastAPI()

app.add_middleware(LoggingMiddleware)
app.add_middleware(RateLimitingMiddleware)



@app.exception_handler(Exception)
async def globalexceptionhandler(request : Request, exc : Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code" : 500,
                "message" : "Internal server error",
                "detail" : str(exc)
            }
        }
    ) 


app.include_router(router)
app.include_router(UserRouter)
app.include_router(ContactRouter)
app.include_router(ChatRouter)
app.include_router(MessageRouter)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#implement 
# authorized users only and add 
# forget pass/ 
# reset pass/ 
# email verification/
# add real time chat for authorized users
# add groups and punlic private groups 

