from fastapi import FastAPI
from auth_router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)


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

