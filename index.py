#!/usr/bin/python3
#coding=utf-8
import pymysql
import os
db=pymysql.connect(host='localhost',user='root',database='school',charset='utf8')
cursor=db.cursor()
# 转换逻辑id为索引id
def changId(table,table_id):
    cursor.execute(f'select * from {table};')
    grades=cursor.fetchall()
    for ind,val in enumerate(grades):
        if table_id==ind:
            table_id=val
            break
    return table_id[0]
# 清空界面
def clear():
    os.system('clear')

# 查询年级
def FindGrade():
    clear()
    cursor.execute('select * from grades;')
    data=cursor.fetchall()
    print('年级'.center(38,'-'))
    print('id'.center(20,' '),'年级'.center(20,' '))
    print('-'*40)
    for idx,grade in enumerate(data):
        print('{}'.format(idx).center(20,' '),end='|')
        print('{}'.format(grade[1]).center(20,' '))
        print('-'*40)
    print('\n')
# 查询班级
def FindClass():
    sql='select class.Type,class.id,GradeName,ClassName,TeacherName,SubjectName from grades right join class on class.grade_id=grades.id left join teachers on teachers.id=class.teacher_id left join subjects on subjects.id=teachers.subject_id'
    conditions=map(int,input('请输入查询条件(年级 0/文理科 1 (多个条件以空格分隔)):').strip().split(' '))
    clear()
    for i in conditions:
        if i==0:
           FindGrade() 
           gradeid=int(input('请输入年级id:'))
           strtemp=' where' if sql.find('where')<0 else ' and'
           sql=sql+strtemp+f' class.grade_id={gradeid}'
        elif i==1:
            typeid=int(input('全科0/理科1/文科2'))
            strtemp=' where' if sql.find('where')<0 else ' and'
            sql=sql+strtemp+f' class.Type={typeid}'
    sql=sql+';'
    cursor.execute(sql)
    data=cursor.fetchall()
    print('班级'.center(133,'-'),'\n')
    print('id'.center(20,' '),'文/理'.center(20,' '),'班级'.center(21,' '),'年级'.center(20,' '),'班主任'.center(20,' '),'学科'.center(18,' '))
    print('-'*135)
    for idx,(Type,ind,grade,cl,teacher,subject) in enumerate(data):
        if Type==0:
            Type='全科'
        else:
            Type='理科' if Type==1 else '文科'
        grade=grade if grade else '未知'
        cl=cl if cl else '未知'
        teacher=teacher if teacher else '未知'
        subject=subject if subject else '未知'
        print(str(idx).center(20,' '),end='|')
        print(str(Type).center(20,' '),end='|')
        print(cl.center(20,' '),end='|')
        print(grade.center(20,' '),end='|')
        print(teacher.center(20,' '),end='|')
        print(subject.center(20,' '))
        print('-'*135)
    print('\n')
# 查询老师
def FindTeacher(typeid=0):
    if typeid==0:
        cursor.execute('select teachers.id,ClassName,TeacherName,sex,age,SubjectName from (class right join teachers on teachers.id=class.teacher_id) left join subjects on teachers.subject_id=subjects.id;')
    else:
        cursor.execute(f'select teachers.id,ClassName,TeacherName,sex,age,SubjectName from (class right join teachers on teachers.id=class.teacher_id) left join subjects on teachers.subject_id=subjects.id where subjects.Type=0 or subjects.Type={typeid};')
    teachers=cursor.fetchall()
    print('老师'.center(129,'-'),'\n')
    print('id'.center(20,' '),'姓名'.center(20,' '),'性别'.center(18,' '),'年龄'.center(19,' '),'学科'.center(20,' '),'班级'.center(20,' '))
    print('-'*131)
    for idx,(ind,cl,name,sex,age,subject) in enumerate(teachers):
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
    print('学科'.center(64,'-'),'\n')
    print('id'.center(20,' '),'学科'.center(20,' '),'文/理'.center(20,' '))
    print('-'*66)
    for idx,(ind,subject,Type) in enumerate(subjects):
        if Type==0:
            Type='主科'
        else:
            Type='理科' if Type==1 else '文科'
        print(str(idx).center(20,' '),end='|')
        print(subject.center(20,' '),end='|')
        print(Type.center(20,' '))
        print('-'*66)
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
        FindGrade()
        try:
            Typeid=int(input('全科:0/理科:1/文科:2 :'))
            FindTeacher(Typeid)
            gradeid=int(input('请输入班级所在的年级id:'))
            gradeid=changId("grades",gradeid)
            teacherid=int(input('请输入班主任id:'))
            t1_id=int(input('请输入老师id:'))
            t2_id=int(input('请输入老师id:'))
            t3_id=int(input('请输入老师id:'))
            t4_id=int(input('请输入老师id:'))
            t5_id=int(input('请输入老师id:'))
            teacherid=changId("teachers",teacherid)
            t1_id=changId("teachers",t1_id)
            t2_id=changId("teachers",t2_id)
            t3_id=changId("teachers",t3_id)
            t4_id=changId("teachers",t4_id)
            t5_id=changId("teachers",t5_id)
            className=input('请输入班级名称:')
            cursor.execute(f'insert into class(Type,grade_id,ClassName,teacher_id,t1_id,t2_id,t3_id,t4_id,t5_id) values({Typeid},{gradeid},"{className}",{teacherid},{t1_id},{t2_id},{t3_id},{t4_id},{t5_id});')
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
        FindSubject()
        try:
            name=input('请输入老师姓名:')
            age=int(input('请输入老师年龄:'))
            sex=input('请输入老师性别:')
            subjectid=int(input('请输入老师所授科目id:'))
            subjectid=changId("subjects",subjectid)
            subs=cursor.execute('select id from subjects;')
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
            Typeid=int(input('主课0/理科1/文科2:'))
            SubjectName=input('请输入您要添加的学科:')
            cursor.execute('insert into subjects(SubjectName,Type) values("{}",{});'.format(SubjectName,Typeid))
            print('添加成功\n')
        except:
            print('因为未知原因,添加失败,请稍后重试......')
        msg=input('是否继续添加 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def delGrade():
    while True:
        clear()
        FindGrade()
        try:
            grade_id=int(input('请输入要删除的年级id:'))
            grade_id=changId("grades",grade_id)
            cursor.execute(f'delete from grades where id={grade_id};')
            print('删除成功\n')
        except:
            print('由于未知原因,删除失败,请稍后重试......')
        msg=input('是否继续删除 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
# 删除
def delClass():
    while True:
        clear()
        FindClass()
        try:
            class_id=int(input('请输入要删除的班级id:'))
            class_id=changId("class",class_id)
            cursor.execute(f'delete from class where id={class_id};')
            print('删除成功\n')
        except:
            print('由于未知原因,删除失败,请稍后重试......')
        msg=input('是否继续删除 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def delTeacher():
    while True:
        clear()
        FindTeacher()
        try:
            teacher_id=int(input('请输入要删除的老师id:'))
            teacher_id=changId("teachers",teacher_id)
            cursor.execute(f'delete from teachers where id={teacher_id};')
            print('删除成功\n')
        except:
            print('由于未知原因,删除失败,请稍后重试......')
        msg=input('是否继续删除 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def delSubject():
    while True:
        clear()
        FindSubject()
        try:
            subject_id=int(input('请输入要删除的学科id:'))
            subject_id=changId("subjects",subject_id)
            cursor.execute(f'delete from subjects where id={subject_id};')
            print('删除成功\n')
        except:
            print('由于未知原因,删除失败,请稍后重试......')
        msg=input('是否继续删除 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break

# 更新
def updateGrade():
    while True:
        clear()
        FindGrade()
        try:
            grade_id=int(input('请输入需要更新的年级id:'))
            grade_id=changId("grades",grade_id)
            grade_name=input('请输入年级:')
            cursor.execute(f'update grades set GradeName="{grade_name}" where id={grade_id};')
            print('更新成功\n')
        except:
            print('由于未知原因,更新失败,请稍后重试......')
        msg=input('是否继续更新 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break

def updateClass():
    while True:
        clear()
        FindGrade()
        FindClass()
        try:
            typeid=int(input('全科0/理科1/文科2:'))
            FindTeacher(typeid)
            class_id=int(input('请输入要更新的班级id:'))
            class_id=changId("class",class_id)
            grade_id=int(input('年级id:'))
            grade_id=changId("grades",grade_id)
            class_name=input('班级:')
            class_teacher=int(input('请输入班级中的班主任id:'))
            class_teacher=changId("teachers",class_teacher)
            cursor.execute(f'update class set ClassName="{class_name}",teacher_id={class_teacher},grade_id={grade_id},Type={typeid} where id={class_id};')
            print('更新成功\n')
        except:
            print('由于未知原因,更新失败,请稍后重试......')
        msg=input('是否继续更新 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def updateTeacher():
    while True:
        clear()
        FindTeacher()
        FindSubject()
        try:
            teacher_id=int(input('请输入要更新的老师id:'))
            teacher_id=changId("teachers",teacher_id)
            teacher_name=input('姓名:')
            teacher_age=int(input('年龄:'))
            teacher_sex=input('性别:')
            subject_id=int(input('学科id:'))
            subject_id=changId("subjects",subject_id)
            cursor.execute(f'update teachers set TeacherName="{teacher_name}",age={teacher_age},sex="{teacher_sex}",subject_id={subject_id} where id={teacher_id};')
            print('更新成功\n')
        except:
            print('由于未知原因,更新失败,请稍后重试......')
        msg=input('是否继续更新 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break

def updateSubject():
    while True:
        clear()
        FindSubject()
        try:
            sub_id=int(input('请输入要更新的学科id:'))
            sub_id=changId("subjects",sub_id)
            typeid=int(input('主科0/理科1/文科2:'))
            sub_name=input('学科:')
            cursor.execute(f'update subjects set SubjectName="{sub_name}",Type={typeid} where id={sub_id};')
            print('更新成功\n')
        except:
            print('由于未知原因,更新失败,请稍后重试......')
        msg=input('是否继续更新 y/n?')
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

deloptions='''
************V1.0 删除界面*********** 
**                                **
**     ******1.删除年级******     **
**                                **
**     ******2.删除班级******     **
**                                **
**     ******3.删除老师******     **
**                                **
**     ******4.删除课程******     **
**                                **
************************************
'''

updateoptions='''
************V1.0 更新界面*********** 
**                                **
**     ******1.更新年级******     **
**                                **
**     ******2.更新班级******     **
**                                **
**     ******3.更新老师******     **
**                                **
**     ******4.更新课程******     **
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
                input('按任意键返回'.center(129,'-'))
            elif int(findselect)==3:
                FindTeacher()
                input('按任意键返回'.center(125,'-'))
            elif int(findselect)==4:
                FindSubject()
                input('按任意键返回'.center(60,'-'))
            else:
                break
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
    elif int(selected)==3:
        while True:
            clear()
            print(deloptions)
            print('按其他任意键返回'.center(28,'-'),'\n')
            i=input('请输入您要添加的选项:')
            if not i.isdigit():
                break
            elif int(i)==1:
                delGrade()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==2:
                delClass()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==3:
                delTeacher()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==4:
                delSubject()
                print('按其他任意键返回'.center(28,'-'),'\n')
            else:
                break
    elif int(selected)==4:
        while True:
            clear()
            print(updateoptions)
            print('按其他任意键返回'.center(28,'-'),'\n')
            i=input('请输入您要添加的选项:')
            if not i.isdigit():
                break
            elif int(i)==1:
                updateGrade()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==2:
                updateClass()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==3:
                updateTeacher()
                print('按其他任意键返回'.center(28,'-'),'\n')
            elif int(i)==4:
                updateSubject()
                print('按其他任意键返回'.center(28,'-'),'\n')
            else:
                break
    else:
        clear()
        print('退出成功'.center(28,'*')) 
        break
db.close()

