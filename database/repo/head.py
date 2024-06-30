from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update
from ..database import engine
from ..schema import Head, Course

async def quary_head(lid):
    session = Session(engine)
    try:
        query = select(Head).where(Head.lid == lid).options(joinedload(Head.courses))
        head = session.scalars(query).unique().one()
        return (True, head, [])
    except BaseException as e:
        print(e)
        return (False, {} , ["استادی با این شماره وجود ندارد"])
    finally:
        session.close()

async def insert_head(head):
    session = Session(engine)
    try:
        session.add(head)
        session.commit()
    except IntegrityError:
        return (False, ["استاد دیگری با این شماره وجود دارد"])
    except:
        return (False, ["خطایی در اضافه کردن استاد به وجود امده"])
    else:
        return (True, [])
    finally:
        session.close()

async def replace_head(head):
    session = Session(engine)
    try:
        query = select(Head).where(Head.lid == head.lid)
        old_head = session.scalars(query).one()
        for key, value in head.__dict__.items():
            setattr(old_head, key, value)
        session.commit()
    except BaseException as e:
        return (False, {} , ["استاد با این شماره وجود ندارد"])
    else:
        return (True, head, [])
    finally:
        session.close()

async def remove_head(lid):
    session = Session(engine)
    try:
        query = select(Head).where(Head.lid == lid)
        head = (session.scalars(query)).one()
        head.courses.clear()
        session.delete(head)
        session.commit()
    except BaseException as e:
        print(e)
        return (False, ["استادی با این شماره وجود ندارد"])
    else:
        return (True, [])
    finally:
        session.close()

async def insert_head_course(lid, cid):
    session = Session(engine)
    try:
        head_query = select(Head).where(Head.lid == lid)
        head = (session.scalars(head_query)).one()
        course_query = select(Course).where(Course.cid == cid)
        course = (session.scalars(course_query)).one()
        head.courses.append(course)
        session.commit()
    except BaseException as e:
        return (False, ["استاد یا درسی با این شماره وجود ندارد"])
    else:
        return (True, [])
    finally:
        session.close()

async def remove_head_course(lid, cid):
    session = Session(engine)
    try:
        head_query = select(Head).where(Head.lid == lid)
        head = (session.scalars(head_query)).one()
        course_query = select(Course).where(Course.cid == cid)
        course = (session.scalars(course_query)).one()
        # head.courses.remove(course)
        session.commit()
    except BaseException as e:
        return (False, ["استاد یا درسی با این شماره وجود ندارد"])
    else:
        return (True, [])
    finally:
        session.close()