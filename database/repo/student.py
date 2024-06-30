from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update
from ..database import engine
from ..schema import Student, Course
from .course import quary_course

async def quary_student(stid):
    session = Session(engine)
    try:
        query = select(Student).where(Student.stid == stid).options(joinedload(Student.courses))
        student = session.scalars(query).unique().one()
        return (True, student , [])
    except BaseException as e:
        print(e)
        return (False, {} , ["دانشجویی با این شماره دانشجویی وجود ندارد"])
    finally:
        session.close()

async def insert_student(student):
    session = Session(engine)
    try:
        session.add(student)
        session.commit()
    except IntegrityError:
        return (False, ["دانشجوی دیگری با این شماره دانشجویی وجود دارد"])
    except:
        return (False, ["خطایی در اضافه کردن دانشجو به وجود امده"])
    else:
        return (True, [])
    finally:
        session.close()

async def replace_student(student):
    session = Session(engine)
    try:
        commend = select(Student).where(Student.stid == student.stid)
        old_student = session.scalars(commend).one()
        for key, value in student.__dict__.items():
            setattr(old_student, key, value)
        session.commit()
    except BaseException as e:
        return (False, {} , ["دانشجویی با این شماره دانشجویی وجود ندارد"])
    else:
        return (True, student, [])
    finally:
        session.close()

async def remove_student(stid):
    session = Session(engine)
    try:
        query = select(Student).where(Student.stid == stid)
        student = (session.scalars(query)).one()
        student.courses.clear()
        session.delete(student)
        session.commit()
    except BaseException as e:
        print(e)
        return (False, ["دانشجویی با این شماره دانشجویی وجود ندارد"])
    else:
        return (True, [])
    finally:
        session.close()


async def inster_student_course(stid, cid):
    session = Session(engine)
    try:
        student_query = select(Student).where(Student.stid == stid)
        student = (session.scalars(student_query)).one()
        course_query = select(Course).where(Course.cid == cid)
        course = (session.scalars(course_query)).one()
        student.courses.append(course)
        session.commit()
    except BaseException as e:
        print(e)
        return (False, ["دانشجویی یا درسی با این شماره وجود ندارد"])
    else:
        return (True, [])
    finally:
        session.close()

async def remove_student_course(stid, cid):
    session = Session(engine)
    try:
        student_query = select(Student).where(Student.stid == stid)
        student = (session.scalars(student_query)).one()
        course_query = select(Course).where(Course.cid == cid)
        course = (session.scalars(course_query)).one()
        # student.courses.remove(course)
        session.commit()
    except BaseException as e:
        print(e)
        return (False, ["دانشجو یا درسی با این شماره وجود ندارد"])
    else:
        return (True, [])
    finally:
        session.close()
