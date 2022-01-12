#!/usr/bin/python3
#coding=utf-8
import pymysql
import os
db=pymysql.connect(host='localhost',user='root',password='123456',database='school',charset='utf8')
cursor=db.cursor()
# 清空界面
def clear(): 
    os.system('clear')
    
# 查询年级
def FindGrade():
    clear()
    cursor.execute('select GradeName,ClassName,TeacherName,SubjectName from grades left join class on class.grade_id=grades.id left join teachers on teachers.class_id=class.id left join subjects on subjects.id=teachers.subject_id;')
    data=cursor.fetchall()
    print('年级'.center(20,' '),'班级'.center(20,' '),'老师'.center(21,' '),'学科'.center(20,' '))

    print('-'*90)
    for grade,cl,teacher,subject in data:
#        print('   {}       {}          {}           {}'.format(grade,cl,teacher,subject))
        grade=grade if grade else '未知'
        cl=cl if cl else '未知' 
        teacher=teacher if teacher else '未知' 
        subject=subject if subject else '未知'
        print('{}'.format(grade).center(20,' '),end='|')
        print('{}'.format(cl).center(20,' '),end='|')
        print('{}'.format(teacher).center(20,' '),end='|')        
        print('{}'.format(subject).center(20,' '))
        print('-'*90)

# 查询班级
def FindClass():
    cursor.execute('select class.id,GradeName,ClassName,TeacherName,SubjectName from grades right join class on class.grade_id=grades.id left join teachers on teachers.class_id=class.id left join subjects on subjects.id=teachers.subject_id;')
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

# 查询老师
def FindTeacher():
    cursor.execute('select teachers.id,ClassName,TeacherName,sex,age,SubjectName from (class right join teachers on teachers.class_id=class.id) left join subjects on teachers.subject_id=subjects.id;')
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
# 查询课程
def FindSubject():
    cursor.execute('select subjects.id,GradeName,ClassName,TeacherName,SubjectName from teachers right join subjects on teachers.subject_id=subjects.id left join class on teachers.class_id=class.id left join grades on grades.id=class.grade_id;')
    subjects=cursor.fetchall()
    print('id'.center(20,' '),'学科'.center(20,' '),'年级'.center(20,' '),'班级'.center(20,' '),'老师'.center(21,' '))
    print('-'*111)
    for idx,grade,cl,teacher,subject in subjects:
        grade=grade if grade else '未知'
        cl=cl if cl else '未知' 
        teacher=teacher if teacher else '未知' 
        subject=subject if subject else '未知'
        print(str(idx).center(20,' '),end='|')
        print(subject.center(20,' '),end='|')
        print(grade.center(20,' '),end='|')
        print(cl.center(20,' '),end='|')
        print(teacher.center(20,' '))
        print('-'*111)

options='''
**********V1.0 教务管理系统********* 
**                                **
**     ******1.查询数据******     **
**                                **
**     ******2.添加数据******     **
**                                **
**     ******3.删除数据******     **
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
                input('按任意键返回'.center(84,'-'))
            elif int(findselect)==2:
                FindClass()
                input('按任意键返回'.center(105,'-'))
            elif int(findselect)==3:
                FindTeacher()
                input('按任意键返回'.center(125,'-'))
            elif int(findselect)==4:
                FindSubject()
                input('按任意键返回'.center(105,'-'))
            else:
                break
    elif int(selected)==3:
        clear()
        input('功能正在开发中,按任意键继续......')
    elif int(selected)==2:
        clear()
        input('功能正在开发中,按任意键继续......')
    else:
        clear()
        print('退出成功'.center(28,'*')) 
        break
db.close()

