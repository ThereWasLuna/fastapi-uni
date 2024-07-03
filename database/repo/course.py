from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update
from ..database import engine
from ..schema import Course

async def quary_course(cid):
    session = Session(engine)
    try:
        query = select(Course).where(Course.cid == cid)
        course = session.scalars(query).one()
        return (True, course , [])
    except:
        return (False, {} , ["درسی با این شماره وجود ندارد"])
    finally:
        session.close()

async def insert_course(course):
    session = Session(engine)
    try:
        session.add(course)
        session.commit()
    except IntegrityError:
        return (False, ["درس دیگری با این شماره وجود دارد"])
    except:
        return (False, ["خطایی در اضافه کردن درس به وجود امده"])
    else:
        return (True, [])
    finally:
        session.close()

async def replace_course(course):
    session = Session(engine)
    try:
        query = select(Course).where(Course.lid == course.lid)
        old_course = session.scalars(query).one()
        for key, value in course.__dict__.items():
            setattr(old_course, key, value)
        session.commit()
    except BaseException as e:
        return (False, {} , ["استاد با این شماره وجود ندارد"])
    else:
        return (True, course, [])
    finally:
        session.close()

async def remove_course(cid):
    session = Session(engine)
    try:
        query = select(Course).where(Course.cid == cid)
        course = (session.scalars(query)).one()
        if course:
            session.delete(course)
            session.commit()
        else:
            return (False, ["درسی با این شماره وجود ندارد"])
    except BaseException as e:
        print(e)
        return (False, ["خطایی در حذف درس به وجود امده"])
    else:
        return (True, [])
    finally:
        session.close()
