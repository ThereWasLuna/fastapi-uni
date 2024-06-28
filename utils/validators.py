import re
from .consts import *

def validator_student(student):
    patterns = [
        (r'\d{3}\d{8}', student.stid, "شماره دانشجویی اشتباه وارد شده"),
        (r'^[\u0600-\u06FF\s]{1,10}$', student.fname, "نام یا نام خانوادگی یا نام ‍بدر اشتباه وارد شده"),
        (r'^[\u0600-\u06FF\s]{1,10}$', student.lname, "نام یا نام خانوادگی یا نام ‍بدر اشتباه وارد شده"),
        (r'^[\u0600-\u06FF\s]{1,10}$', student.father, "نام یا نام خانوادگی یا نام ‍بدر اشتباه وارد شده"),
        (r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(1[34][0-9]{2})$', student.birth, "تاریخ تولد اشتباه وارد شده"),
        (r'^\d{6}[\u0600-\u06FF]\d{2}$', student.ids, "سریال شناسنامه اشتباه وارد شده"),
        (r'^(' + '|'.join(centers) + r')$', student.born, "محل تولد اشتباه وارد شده"),
        (r'^.{1,100}$', student.address, "آدرس اشتباه وارد شده"),
        (r'^\d{10}$', student.post, "کد پستی اشتباه وارد شده"),
        (r'^09\d{9}$', student.cphone, "تلفن همراه اشتباه وارد شده"),
        (r'^0\d{10}$', student.hphone, "تلفن ثابت اشتباه وارد شده"),
        (r'^(' + '|'.join(departments) + r')$', student.department, "دانشکده اشتباه وارد شده"),
        (r'^(' + '|'.join(majors) + r')$', student.major, "رشته اشتباه وارد شده"),
        (r'^\d{10}$', student.id, "کد ملی اشتباه وارد شده"),
    ]
    errors = [message for pattern, field, message in patterns if not re.match(pattern, field)]
    return (not errors, errors)


def validator_head(head):
    patterns = [
        (r'\d{3}\d{8}', head.lid, "شماره استاد اشتباه وارد شده"),
        (r'^[\u0600-\u06FF\s]{1,10}$', head.fname, "نام یا نام خانوادگی یا نام ‍بدر اشتباه وارد شده"),
        (r'^[\u0600-\u06FF\s]{1,10}$', head.lname, "نام یا نام خانوادگی یا نام ‍بدر اشتباه وارد شده"),
        (r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(1[34][0-9]{2})$', head.birth, "تاریخ تولد اشتباه وارد شده"),
        (r'^(' + '|'.join(centers) + r')$', head.born, "محل تولد اشتباه وارد شده"),
        (r'^.{1,100}$', head.address, "آدرس اشتباه وارد شده"),
        (r'^\d{10}$', head.post, "کد پستی اشتباه وارد شده"),
        (r'^09\d{9}$', head.cphone, "تلفن همراه اشتباه وارد شده"),
        (r'^0\d{10}$', head.hphone, "تلفن ثابت اشتباه وارد شده"),
        (r'^(' + '|'.join(departments) + r')$', head.department, "دانشکده اشتباه وارد شده"),
        (r'^(' + '|'.join(majors) + r')$', head.major, "رشته اشتباه وارد شده"),
        (r'^\d{10}$', head.id, "کد ملی اشتباه وارد شده"),
    ]
    errors = [message for pattern, field, message in patterns if not re.match(pattern, field)]
    return (not errors, errors)


def validator_course(course):
    patterns = [
        (r'\d{5}', course.cid, " کد درس اشتباه وارد شده"),
        (r'^[\u0600-\u06FF\s]{1,25}$', course.name, "نام یا نام خانوادگی یا نام ‍بدر اشتباه وارد شده"),
        (r'^(' + '|'.join(departments) + r')$', course.department, "دانشکده اشتباه وارد شده"),
        (r'^[1-4]$', str(course.credit), "دانشکده اشتباه وارد شده"),
    ]
    errors = [message for pattern, field, message in patterns if not re.match(pattern, field)]
    return (not errors, errors)