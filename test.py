from fastapi import FastAPI  # type: ignore[import-not-found]
from sqlmodel import Session, select  # type: ignore[import-not-found]
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware  # type: ignore[import-not-found]

from models import Users, Bikeshop

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000", 
    "https://example.com",    
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       
    allow_credentials=True,       
    allow_methods=["*"],          
    allow_headers=["*"],          
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/{id}")
async def read_Users(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        user = session.get(Users, id)
        return {"message": user}
    

@app.post("/users")
async def root(users  : Users):
    with Session(engine) as session:
        session.add(users)
        session.commit()
        session.refresh(users)
        return {"message": users}
    
@app.post("/usersLogin")
async def root(users  : Users):
    with Session(engine) as session:


        print()
        statement = select(Users).where(Users.username == users.username).where(Users.password == users.password)
        results = session.exec(statement)

        result = results.first()
        print(result)

        if (result == None):
            return {"status":"failed"}


        return {
            "status":"success",
            "data": result
            }
    
@app.get("/bikeshop/{id}")
async def read_Bikeshop(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        user = session.get(Bikeshop, id)
        return {"message": user}
    

@app.post("/bikeshop")
async def root(bikeshop  : Bikeshop):
    with Session(engine) as session:
        session.add(bikeshop)
        session.commit()
        session.refresh(bikeshop)
        return {"message": bikeshop}
    