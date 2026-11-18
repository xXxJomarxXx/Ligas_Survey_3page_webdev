from sqlmodel import Field, SQLModel  # pyright: ignore[reportMissingImports]

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    create_username: str
    create_pass: str
    confirm_pass: str


class Bikeshop(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int | None = None
    gender: str