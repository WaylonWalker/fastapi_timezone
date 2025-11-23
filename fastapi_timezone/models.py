from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine


class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author: str
    message: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def save(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    @classmethod
    def get(cls, id: int):
        with Session(engine) as session:
            return session.get(cls, id)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

