from pydantic import BaseModel
from database.schema import Student as Student_db

class Student(BaseModel):
    stid:str
    fname:str
    lname:str
    father:str
    birth:str
    ids:str
    born:str
    address:str
    post:str
    cphone:str
    hphone:str
    department:str
    major:str
    married:bool
    id:str

    def db(self):
        return Student_db(
            stid=self.stid,
            fname=self.fname,
            lname=self.lname,
            father=self.father,
            birth=self.birth,
            ids=self.ids,
            born=self.born,
            address=self.address,
            post=self.post,
            cphone=self.cphone,
            hphone=self.hphone,
            department=self.department,
            major=self.major,
            married=self.married,
            id=self.id,
        )

