from pydantic import BaseModel
from database.schema import Head as Head_db

class Head(BaseModel):
    lid:str
    fname:str
    lname:str
    birth:str
    born:str
    address:str
    post:str
    cphone:str
    hphone:str
    department:str
    major:str
    id:str

    def db(self):
        return Head_db(
            lid=self.lid,
            fname=self.fname,
            lname=self.lname,
            birth=self.birth,
            born=self.born,
            address=self.address,
            post=self.post,
            cphone=self.cphone,
            hphone=self.hphone,
            department=self.department,
            major=self.major,
            id=self.id,
        )