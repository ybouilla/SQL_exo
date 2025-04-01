# https://docs.sqlalchemy.org/en/20/orm/quickstart.html


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select




from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Events(Base):
    __tablename__ = "events"
    event_id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] # = mapped_column(String(30))
    start_date: Mapped[str]
    end_date: Mapped[str]
    
    def __repr__(self) -> str:
        return f"event(id={self.event_id!r}, doctor_id={self.doctor_id!r}, start_date={self.start_date!r}), end_date={self.end_date!r}"

# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

# for user in session.scalars(stmt):
#     print(user)



engine = create_engine("sqlite://", echo=True)

Base.metadata.create_all(engine)
with Session(engine) as session:
    e1 = Events(event_id=1, doctor_id=123, start_date='2022-12-12 09:00:00', end_date='2022-12-12 09:30:00' )

    e2 = Events(event_id=2, doctor_id=123, start_date='2022-12-12 10:00:00', end_date='2022-12-12 10:30:00' )
    session.add_all([e1, e2])
    session.commit()

select_query = select(Events).where(Events.doctor_id==123)

with Session(engine) as session:

    print(session.query(Events).where(Events.doctor_id==123).filter(Events.start_date.between(1, 2)).order_by(Events.start_date).all())
         