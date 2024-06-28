from pydantic import BaseModel
from database.schema import Course as Course_db

class Course(BaseModel):
    cid:str
    name:str
    department:str
    credit:int

    def db(self):
        return Course_db(
            cid=self.cid,
            name=self.name,
            department=self.department,
            credit=self.credit,
        )