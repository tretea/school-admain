#!/usr/bin/python3
#coding=utf-8
import pymysql
import os
db=pymysql.connect(host='localhost',user='root',database='school',charset='utf8')
cursor=db.cursor()
# 清空界面
def clear():
    os.system('clear')

# 查询年级
def FindGrade():
    clear()
    cursor.execute('select * from grades;')
    data=cursor.fetchall()
    print('id'.center(20,' '),'年级'.center(20,' '))

    print('-'*40)
    for idx,grade in data:
        print('{}'.format(idx).center(20,' '),end='|')
        print('{}'.format(grade).center(20,' '))
        print('-'*40)
    print('\n')
# 查询班级
def FindClass():
    cursor.execute('select class.id,GradeName,ClassName,TeacherName,SubjectName from grades right join class on class.grade_id=grades.id left join teachers on teachers.id=class.teacher_id left join subjects on subjects.id=teachers.subject_id;')
    data=cursor.fetchall()
    print('id'.center(20,' '),'班级'.center(21,' '),'年级'.center(20,' '),'老师'.center(20,' '),'学科'.center(20,' '))
    print('-'*111)
    for idx,grade,cl,teacher,subject in data:
        grade=grade if grade else '未知'
        cl=cl if cl else '未知' 
        teacher=teacher if teacher else '未知' 
        subject=subject if subject else '未知'
        print(str(idx).center(20,' '),end='|')
        print(cl.center(20,' '),end='|')
        print(grade.center(20,' '),end='|')
        print(teacher.center(20,' '),end='|')
        print(subject.center(20,' '))
        print('-'*111)
    print('\n')
# 查询老师
def FindTeacher():
    cursor.execute('select teachers.id,ClassName,TeacherName,sex,age,SubjectName from (class right join teachers on teachers.id=class.teacher_id) left join subjects on teachers.subject_id=subjects.id;')
    teachers=cursor.fetchall()
    print('id'.center(20,' '),'姓名'.center(20,' '),'性别'.center(18,' '),'年龄'.center(19,' '),'学科'.center(20,' '),'班级'.center(20,' '))
    print('-'*131)
    for idx,cl,name,sex,age,subject in teachers:
        cl=cl if cl else '未知'
        subject=subject if subject else '未知'
        print(str(idx).center(20,' '),end='|')
        print(name.center(20,' '),end='|')
        print(sex.center(20,' '),end='|')
        print(str(age).center(20,' '),end='|')
        print(subject.center(20,' '),end='|')
        print(cl.center(20,' '))
        print('-'*131)
    print('\n')
# 查询课程
def FindSubject():
    cursor.execute('select * from subjects;')
    subjects=cursor.fetchall()
    print('id'.center(20,' '),'学科'.center(20,' '))
    print('-'*40)
    for idx,subject in subjects:
        print(str(idx).center(20,' '),end='|')
        print(subject.center(20,' '))
        print('-'*40)
    print('\n')

# 添加
def AddGrade():
    while True:
        clear()
        gradeName=input('请输入年级名称:')
        try:
            cursor.execute('insert into grades(GradeName) values("{}");'.format(gradeName))
            print('添加成功\n')
        except:
            print('因为未知原因,添加失败,请稍后重试......')
        msg=input('是否继续添加 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def AddClass():
    while True:
        clear()
        print('年级'.center(100,'-'))
        FindGrade()
        print('老师'.center(80,'-'))
        FindTeacher()
        try:
            gradeid=int(input('请输入班级所在的年级:'))
            teacherid=int(input('请输入老师id'))
            className=input('请输入班级名称:')
            cursor.execute('insert into class(grade_id,ClassName,teacher_id) values({},"{}",{});'.format(gradeid,className,teacherid))
            print('添加成功\n')
        except:
            print('因为未知原因,添加失败,请稍后重试......')
        msg=input('是否继续添加 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def AddTeacher():
    while True:
        clear()
        print('学科'.center(40,'-'))
        FindSubject()
        try:
            name=input('请输入老师姓名:')
            age=int(input('请输入老师年龄:'))
            sex=input('请输入老师性别:')
            subjectid=int(input('请输入老师所授科目id:'))
            cursor.execute('insert into teachers(TeacherName,age,sex,subject_id) values("{}",{},"{}",{});'.format(name,age,sex,subjectid))
            print('添加成功\n')
        except:
            print('因为未知原因,添加失败,请稍后重试......')
        msg=input('是否继续添加 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def AddSubject():
    while True:
        clear()
        try:
            SubjectName=input('请输入您要添加的学科')
            cursor.execute('insert into subjects(SubjectName) values("{}");'.format(SubjectName))
            print('添加成功\n')
        except:
            print('因为未知原因,添加失败,请稍后重试......')
        msg=input('是否继续添加 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
options='''
**********V1.0 教务管理系统********* 
**                                **
**     ******1.查询数据******     **
**                                **
**     ******2.添加数据******     **
**                                **
**     ******3.删除数据******     **
**                                **
**     ******4.更新数据******     **
**                                **
************************************
'''

findoptions='''
************V1.0 查询界面*********** 
**                                **
**     ******1.查询年级******     **
**                                **
**     ******2.查询班级******     **
**                                **
**     ******3.查询老师******     **
**                                **
**     ******4.查询课程******     **
**                                **
************************************
'''

addoptions='''
************V1.0 添加界面*********** 
**                                **
**     ******1.添加年级******     **
**                                **
**     ******2.添加班级******     **
**                                **
**     ******3.添加老师******     **
**                                **
**     ******4.添加课程******     **
**                                **
************************************
'''

while True:
    clear()
    print(options)
    print('按其他任意键退出'.center(28,'-'),'\n')
    selected=input('请输入您要进行的操作:')
    if not selected.isdigit():
        clear()
        print('退出成功'.center(28,'*')) 
        break
    elif int(selected)==1:
        while True:
            clear()
            print(findoptions)
            print('按其他任意键返回'.center(28,'-'),'\n')
            findselect=input('请输入需要查询的选项')
            clear()
            if not findselect.isdigit():
                break
            elif int(findselect)==1:
                FindGrade()
                input('按任意键返回'.center(34,'-'))
            elif int(findselect)==2:
                FindClass()
                input('按任意键返回'.center(105,'-'))
            elif int(findselect)==3:
                FindTeacher()
                input('按任意键返回'.center(125,'-'))
            elif int(findselect)==4:
                FindSubject()
                input('按任意键返回'.center(34,'-'))
            else:
                break
    elif int(selected)==3:
        clear()
        input('功能正在开发中,按任意键继续......')
    elif int(selected)==2:
        while True:
            clear()
            print(addoptions)
            print('按其他任意键返回'.center(28,'-'),'\n')
            i=input('请输入您要添加的选项:')
            if not i.isdigit():
                break
            elif int(i)==1:
                AddGrade()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==2:
                AddClass()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==3:
                AddTeacher()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==4:
                AddSubject()
                print('按其他任意键返回'.center(28,'-'),'\n')
            else:
                break
    else:
        clear()
        print('退出成功'.center(28,'*')) 
        break
db.close()

