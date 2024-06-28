from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, ForeignKey, String

class Base(DeclarativeBase):
    pass


student_course_association = Table(
    "student_course",
    Base.metadata,
    Column("student_stid", ForeignKey("student.stid"), primary_key=True),
    Column("course_cid", ForeignKey("course.cid"), primary_key=True)
)

head_course_association = Table(
    "head_course",
    Base.metadata,
    Column("head_lid", ForeignKey("head.lid"), primary_key=True),
    Column("course_cid", ForeignKey("course.cid"), primary_key=True)
)

class Student(Base):
    __tablename__ = "student"
    stid: Mapped[str] = mapped_column(primary_key=True)
    fname: Mapped[str] = mapped_column(String(100))
    lname: Mapped[str] = mapped_column(String(100))
    father: Mapped[str] = mapped_column(String(100))
    birth: Mapped[str] = mapped_column(String(100))
    ids: Mapped[str] = mapped_column(String(100))
    born: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(100))
    post: Mapped[str] = mapped_column(String(100))
    cphone: Mapped[str] = mapped_column(String(100))
    hphone: Mapped[str] = mapped_column(String(100))
    department: Mapped[str] = mapped_column(String(100))
    major: Mapped[str] = mapped_column(String(100))
    married: Mapped[bool] = mapped_column()
    id: Mapped[str] = mapped_column()
    courses: Mapped[list["Course"]] = relationship(
        "Course",
        secondary=student_course_association,
        back_populates="students"
    )


class Head(Base):
    __tablename__ = "head"
    lid: Mapped[str] = mapped_column(primary_key=True)
    fname: Mapped[str] = mapped_column(String(100))
    lname: Mapped[str] = mapped_column(String(100))
    birth: Mapped[str] = mapped_column(String(100))
    born: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(100))
    post: Mapped[str] = mapped_column(String(100))
    cphone: Mapped[str] = mapped_column(String(100))
    hphone: Mapped[str] = mapped_column(String(100))
    department: Mapped[str] = mapped_column(String(100))
    major: Mapped[str] = mapped_column(String(100))
    id: Mapped[str] = mapped_column()
    courses: Mapped[list["Course"]] = relationship(
        "Course",
        secondary=head_course_association,
        back_populates="heads"
    )


class Course(Base):
    __tablename__ = "course"
    cid: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    department: Mapped[str] = mapped_column(String(100))
    credit: Mapped[int] = mapped_column(String(100))
    students: Mapped[list["Student"]] = relationship(
        "Student",
        secondary=student_course_association,
        back_populates="courses"
    )
    heads: Mapped[list["Head"]] = relationship(
        "Head",
        secondary=head_course_association,
        back_populates="courses"
    )