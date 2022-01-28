#!/usr/bin/python3
#coding=utf-8
import pymysql
import os
db=pymysql.connect(host='localhost',user='root',database='school',charset='utf8')
cursor=db.cursor()
# 转换逻辑id为索引id
def changId(table,table_id,swatch=0):
    if not swatch:
        cursor.execute(f'select * from {table};')
    else:
        cursor.execute(table)
    grades=cursor.fetchall()
    for ind,val in enumerate(grades):
        if table_id==ind:
            table_id=val
            break
    return table_id[0]
# 清空界面
def clear():
    os.system('clear')

# TODO 课程管理
# 查询课程

# 查询年级
def FindGrade():
    cursor.execute('select * from grades;')
    data=cursor.fetchall()
    print('年级'.center(38,'-'))
    print('id'.center(20,' '),'年级'.center(18,' '))
    print('-'*40)
    for idx,grade in enumerate(data):
        print('{}'.format(idx).center(20,' '),end='|')
        print('{}'.format(grade[1]).center(20-len(grade[1]),' '))
        print('-'*40)
    print('\n')
# 查询班级
def FindClass():
    sql='select class.id,class.Type,GradeName,ClassName,TeacherName,SubjectName from grades right join class on class.grade_id=grades.id left join teachers on teachers.id=class.teacher_id left join subjects on subjects.id=teachers.subject_id'
    conditions=map(str,input('请输入查询条件(年级 0/文理科 1 (多个条件以空格分隔)):').strip().split(' '))
    for i in conditions:
        if i=='0':
           FindGrade() 
           gradeid=int(input('请输入年级id:'))
           gradeid=changId('grades',gradeid)
           strtemp=' where' if sql.find('where')<0 else ' and'
           sql=sql+strtemp+f' class.grade_id={gradeid}'
        elif i=='1':
            typeid=int(input('全科0/理科1/文科2:'))
            strtemp=' where' if sql.find('where')<0 else ' and'
            sql=sql+strtemp+f' class.Type={typeid}'
    sql=sql+';'
    cursor.execute(sql)
    data=cursor.fetchall()
    print('班级'.center(133,'-'),'\n')
    print('id'.center(20,' '),'文/理'.center(18,' '),'班级'.center(18,' '),'年级'.center(18,' '),'班主任'.center(17,' '),'学科'.center(18,' '))
    print('-'*135)
    for idx,(ind,Type,grade,cl,teacher,subject) in enumerate(data):
        if Type==0:
            Type='全科'
        else:
            Type='理科' if Type==1 else '文科'
        grade=grade if grade else '未知'
        cl=cl if cl else '未知'
        teacher=teacher if teacher else '未知'
        subject=subject if subject else '未知'
        print(str(idx).center(20,' '),end='|')
        print(Type.center(20-len(Type),' '),end='|')
        print(cl.center(20,' '),end='|')
        print(grade.center(20-len(grade),' '),end='|')
        print(teacher.center(20-len(teacher),' '),end='|')
        print(subject.center(20-len(subject),' '))
        print('-'*135)
    print('\n')
    FindClassDetail(sql)
    return sql
# 查看班级详情信息
def FindClassDetail(classsql):
    while True:
        class_id=input('请输入班级id查询详情:')
        if not class_id.isdigit():
            break
        else:
            class_id=changId(classsql,int(class_id),1)
            sql=f'select t5.id,t5.ClassName,t5.TeacherName,t5.t1name,t5.t2name,t5.t3name,t5.t4name,teachers.TeacherName as t5name from (select t4.id,t4.ClassName,t4.TeacherName,t4.t1name,t4.t2name,t4.t3name,teachers.TeacherName as t4name,t4.t5_id from (select t3.id,t3.ClassName,t3.TeacherName,t3.t1name,t3.t2name,teachers.TeacherName as t3name,t3.t4_id,t3.t5_id from (select t2.id,t2.ClassName,t2.TeacherName,t2.t1name,teachers.TeacherName as t2name,t2.t3_id,t2.t4_id,t2.t5_id from (select t1.id,t1.ClassName,t1.TeacherName,teachers.TeacherName as t1name,t1.t2_id,t1.t3_id,t1.t4_id,t1.t5_id from (select class.id,ClassName,TeacherName,t1_id,t2_id,t3_id,t4_id,t5_id from class left join teachers on class .teacher_id=teachers.id where class.id={class_id}) as t1 left join teachers on t1.t1_id=teachers.id) as t2 left join teachers on t2.t2_id=teachers.id) as t3 left join teachers on teachers.id=t3.t3_id) as t4 left join teachers on teachers.id=t4.t4_id) as t5 left join teachers on t5.t5_id=teachers.id;'
            cursor.execute(sql)
            datat=cursor.fetchone()
            data=[]
            for x in datat:
                x='无数据' if not x else x
                data.append(x)
            sublist=[]
            for n in data[2:]:
                sql=f'select subjects.SubjectName from teachers left join subjects on teachers.subject_id=subjects.id where teachers.TeacherName="{n}";'
                cursor.execute(sql)
                sub=cursor.fetchone()
                sub=('无数据',) if not sub else sub
                sublist.append(sub[0])
            print('-'*113)
            print('班级'.center(13,' '),end='|')
            print('班主任'.center(12,' '),end='|')
            print(f'{sublist[1]}'.center(15-len(sublist[0]),' '),end='|')
            print(f'{sublist[2]}'.center(15-len(sublist[1]),' '),end='|')
            print(f'{sublist[3]}'.center(15-len(sublist[2]),' '),end='|')
            print(f'{sublist[4]}'.center(15-len(sublist[3]),' '),end='|')
            print(f'{sublist[5]}'.center(15-len(sublist[4]),' '))
            print('-'*113)
            print(f'{data[1]}'.center(15,' '),end='|')
            print(f'{data[2]}'.center(15-len(data[2]),' '),end='|')
            print(f'{data[3]}'.center(15-len(data[3]),' '),end='|')
            print(f'{data[4]}'.center(15-len(data[4]),' '),end='|')
            print(f'{data[5]}'.center(15-len(data[5]),' '),end='|')
            print(f'{data[6]}'.center(15-len(data[6]),' '),end='|')
            print(f'{data[7]}'.center(15-len(data[7]),' '))
            print('-'*113,'\n')
            stu_sql=f'select id,idcard,name,age,sex from students where class_id={class_id};'
            cursor.execute(stu_sql)
            stu=cursor.fetchall()
            print('-'*90)
            print('学号'.center(18,' '),end='|')
            print('姓名'.center(18,' '),end='|')
            print('年龄'.center(18,' '),end='|')
            print('性别'.center(18,' '))
            print('-'*90)
            for ind,idcard,name,age,sex in stu:
                print(str(idcard).center(20,' '),end='|')
                print(name.center(20-len(name),' '),end='|')
                print(str(age).center(20,' '),end='|')
                print(sex.center(20-len(sex),' '))
                print('-'*90)
            msg=input('是否继续查看详情 y?n ')
            if msg=='y' or msg=='Y':
                continue
            else:
                break
# 查询老师
def FindTeacher(typeid=0):
    if typeid==0:
        cursor.execute('select teachers.id,ClassName,TeacherName,sex,age,SubjectName from (class right join teachers on teachers.id=class.teacher_id) left join subjects on teachers.subject_id=subjects.id;')
    else:
        cursor.execute(f'select teachers.id,ClassName,TeacherName,sex,age,SubjectName from (class right join teachers on teachers.id=class.teacher_id) left join subjects on teachers.subject_id=subjects.id where subjects.Type=0 or subjects.Type={typeid};')
    teachers=cursor.fetchall()
    print('老师'.center(129,'-'),'\n')
    print('id'.center(20,' '),'姓名'.center(18,' '),'性别'.center(18,' '),'年龄'.center(18,' '),'学科'.center(18,' '),'班级'.center(18,' '))
    print('-'*131)
    for idx,(ind,cl,name,sex,age,subject) in enumerate(teachers):
        cl=cl if cl else '未知'
        subject=subject if subject else '未知'
        print(str(idx).center(20,' '),end='|')
        print(name.center(20-len(name),' '),end='|')
        print(sex.center(20-len(sex),' '),end='|')
        print(str(age).center(20,' '),end='|')
        print(subject.center(20-len(subject),' '),end='|')
        print(cl.center(20,' '))
        print('-'*131)
    print('\n')
# 查询课程
def FindSubject():
    cursor.execute('select * from subjects;')
    subjects=cursor.fetchall()
    print('学科'.center(64,'-'),'\n')
    print('id'.center(20,' '),'学科'.center(18,' '),'文/理'.center(18,' '))
    print('-'*66)
    for idx,(ind,subject,Type) in enumerate(subjects):
        if Type==0:
            Type='主科'
        else:
            Type='理科' if Type==1 else '文科'
        print(str(idx).center(20,' '),end='|')
        print(subject.center(20-len(subject),' '),end='|')
        print(Type.center(20-len(Type),' '))
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
        try:
            Typeid=int(input('全科:0/理科:1/文科:2 :'))
            FindGrade()
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
def delStudent():
    while True:
        clear()
        FindClass()
        try:
            stuid=int(input('请输入要删学生的学号:'))
            issure=input('是否确认删除 y/n?')
            if issure=='y' or issure=='Y':
                cursor.execute(f'delete from students where idcard={stuid};')
                print('删除成功\n')
            else:
                continue
        except:
            print('删除失败,请稍后重试......')
        msg=input('是否继续删除 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def delClass():
    while True:
        clear()
        FindClass()
        try:
            class_id=int(input('请输入要删除的班级id:'))
            class_id=changId("class",class_id)
            issure=input('是否确认删除 y/n?')
            if issure=='y' or 'Y':
                cursor.execute(f'delete from class where id={class_id};')
                print('删除成功\n')
            else:
                continue
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
            issure=input('是否确认删除 y/n?')
            if issure=='y' or issure=='Y':
                cursor.execute(f'delete from teachers where id={teacher_id};')
                print('删除成功\n')
            else:
                continue
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
            issure=input('是否确认删除 y/n?')
            if issure=='y' or issure=='Y':
                cursor.execute(f'delete from subjects where id={subject_id};')
                print('删除成功\n')
            else:
                continue
        except:
            print('由于未知原因,删除失败,请稍后重试......')
        msg=input('是否继续删除 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
def AddStudent():
    while True:
        clear()
        classsql=FindClass()
        try:
            idcard=int(input('请输入学生学号:'))
            name=input('请输入学生姓名:')
            age=int(input('请输入学生年龄:'))
            sex=input('请输入学生性别:')
            classid=int(input('请输入班级id:'))
            classid=changId(classsql,classid,1)
            cursor.execute(f'insert into students(idcard,name,age,sex,class_id) values({idcard},"{name}",{age},"{sex}",{classid});')
            # cursor.execute(f'update students set idcard={idcard},name="{name}",age={age},sex="{sex}",class_id={classid};')
            print('添加成功\n')
        except:
            print('添加失败,请稍后重试......')
        msg=input('是否继续添加 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
# 更新
def UpdateStudent():
    while True:
        clear()
        classsql=FindClass()
        try:
            stuid=int(input('您要更新的学生学号'))
            name=input('请输入学生姓名:')
            age=int(input('请输入学生年龄:'))
            sex=input('请输入学生性别:')
            classid=int(input('请输入班级id:'))
            classid=changId(classsql,classid,1)
            cursor.execute(f'update students set name="{name}",age={age},sex="{sex}",class_id={classid} where idcard={stuid};')
            print('更新成功\n')
        except:
            print('添加失败,请稍后重试......')
        msg=input('是否继续添加 y/n?')
        if msg=='y' or msg=='Y':
            continue
        else:
            break
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
        try:
            findclass=FindClass()
            class_id=int(input('请输入要更新的班级id:'))
            class_id=changId(findclass,class_id,1)
            typeid=int(input('全科0/理科1/文科2:'))
            FindTeacher(typeid) 
            FindGrade()
            grade_id=int(input('年级id:'))
            grade_id=changId("grades",grade_id)
            class_name=input('班级:')
            class_teacher=int(input('请输入班级中的班主任id:'))
            class_teacher=changId("teachers",class_teacher)
            t1_id=int(input('请输入班级中的老师id:'))
            t1_id=changId("teachers",t1_id)
            t2_id=int(input('请输入班级中的老师id:'))
            t2_id=changId("teachers",t2_id)
            t3_id=int(input('请输入班级中的老师id:'))
            t3_id=changId("teachers",t3_id)           
            t4_id=int(input('请输入班级中的老师id:'))
            t4_id=changId("teachers",t4_id)
            t5_id=int(input('请输入班级中的老师id:'))
            t5_id=changId("teachers",t5_id)
            cursor.execute(f'update class set ClassName="{class_name}",teacher_id={class_teacher},t1_id={t1_id},t2_id={t2_id},t3_id={t3_id},t4_id={t4_id},t5_id={t5_id},grade_id={grade_id},Type={typeid} where id={class_id};')
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
**     ******5.课程管理******     **
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
**     ******4.添加学生******     **
**                                **
**     ******5.添加课程******     **
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
**     ******4.删除学生******     **
**                                **
**     ******5.删除课程******     **
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
**     ******4.更新学生******     **
**                                **
**     ******5.更新课程******     **
**                                **
************************************
'''
loginoptions='''
************V1.0 登录界面*********** 
**                                **
**     ******0.管理登录******     **
**                                **
**     ******1.老师登录******     **
**                                **
**     ******2.学生登录******     **
**                                **
************************************

------------按Enter键返回-----------

'''

teacheroptions='''
**********V1.0 教务管理系统********* 
**                                **
**     ******1.我的管理******     **
**                                **
**     ******2.学生管理******     **
**                                **
**     ******3.查看课程******     **
**                                **
************************************
'''

t_my_options='''
****************我的**************** 
**                                **
**     ******1.个人信息******     **
**                                **
**     ******2.修改密码******     **
**                                **
************************************
'''
t_s_options='''
**********V1.0 学生管理界面********* 
**                                **
**     ******1.查看学生******     **
**                                **
**     ******2.成绩管理******     **
**                                **
************************************
'''

t_score_options='''
**********V1.0 成绩管理界面********* 
**                                **
**     ******1.查看成绩******     **
**                                **
**     ******2.输入成绩******     **
**                                **
************************************

------------按Enter键返回-----------

'''

studentoptions='''
************V1.0 学生界面*********** 
**                                **
**     ******1.我的管理******     **
**                                **
**     ******2.查看课程******     **
**                                **
**     ******3.查询成绩******     **
**                                **
**     ******4.查看老师******     **
**                                **
************************************

------------按Enter键返回-----------

'''

s_my_options='''
************V1.0 学生界面*********** 
**                                **
**     ******1.个人信息******     **
**                                **
**     ******2.修改密码******     **
**                                **
************************************

------------按Enter键返回-----------

'''

def t_Student(teacherid):
    classsql=f'select class.id from teachers left join class on teachers.id=class.teacher_id or teachers.id=class.t1_id or teachers.id=class.t2_id or teachers.id=class.t3_id or teachers.id=class.t4_id or teachers.id=class.t5_id where teachers.id={teacherid};'
    cursor.execute(classsql)
    classid=cursor.fetchone()[0]
    
    sql=f'select idcard,name,age,sex from students left join class on class.id=students.class_id where class.id={classid};'
    cursor.execute(sql)
    data=cursor.fetchall()
    print('学生表'.center(87,'-'))
    print('学号'.center(18,' '),'|','姓名'.center(18,' '),'|','年龄'.center(18,' '),'|','性别'.center(18,' '))
    print('-'*90)
    for ClassName,name,age,sex in data:
        print(str(ClassName).center(20,' '),'|',name.center(20-len(name),' '),'|',str(age).center(20,' '),'|',sex.center(20-len(sex),' '))
        print('-'*90)
    print('\n')

def GuanLi():
    while True:
        clear()
        print(options)
        print('按其他任意键退出'.center(28,'-'),'\n')
        selected=input('请输入您要进行的操作:')
        if not selected.isdigit():
            clear()
            msg=input('确认退出? y/n')
            if msg=='y' or msg=='Y':
                print('退出成功'.center(28,'-'),'\n')
                break
            else:
                continue
        elif int(selected)==1:
            while True:
                clear()
                print(findoptions)
                print('按其他任意键返回'.center(28,'-'),'\n')
                findselect=input('请输入需要查询的选项:')
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
                    AddStudent()
                    print('按其他任意键返回'.center(28,' '),'\n')
                elif int(i)==5:
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
                    delStudent()
                    print('按其他任意键返回'.center(28,'-'),'\n') 
                elif int(i)==5:
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
                    UpdateStudent()
                    print('按其他任意键返回'.center(28,'-'),'\n')
                elif int(i)==5:
                    updateSubject()
                    print('按其他任意键返回'.center(28,'-'),'\n')
                else:
                    break
        else:
            clear()
            msg=input('确认退出? y/n')
            if msg=='y' or msg=='Y':
                print('退出成功'.center(28,'-'),'\n')
                break
            else:
                continue

def TeacherJiemian(teacherid):
    while True:
        clear()
        print(teacheroptions)
        print('按其他任意键退出'.center(28,'-'),'\n')
        selected=input('请输入您要进行的操作:')
        if not selected.isdigit():
            clear()
            msg=input('确认退出? y/n')
            if msg=='y' or msg=='Y':
                print('退出成功'.center(28,'-'),'\n')
                break
            else:
                continue
        elif int(selected)==1:
            while True:
                clear()
                print(t_my_options)
                print('按其他任意键返回'.center(28,'-'),'\n')
                findselect=input('请输入需要查询的选项:')
                clear()
                if not findselect.isdigit():
                    break
                elif int(findselect)==1:
                    clear()
                    sql=f'select ClassName,TeacherName,age,sex,SubjectName from teachers left join class on teachers.id=class.teacher_id left join subjects on subjects.id=teachers.subject_id where teachers.id={teacherid};'
                    cursor.execute(sql)
                    msg=cursor.fetchone()
                    print('个人信息'.center(96,'-'))
                    print('班级'.center(18,' '),end='|')
                    print('姓名'.center(18,' '),end='|')
                    print('年龄'.center(18,' '),end='|')
                    print('性别'.center(18,' '),end='|')
                    print('科目'.center(18,' '))
                    print('-'*100)
                    print(str(msg[0]).center(20,' '),end='|')
                    print(msg[1].center(20-len(msg[1]),' '),end='|')
                    print(str(msg[2]).center(20,' '),end='|')
                    print(msg[3].center(20-len(msg[3]),' '),end='|')
                    print(msg[4].center(20-len(msg[4]),' '))
                    print('-'*100,'\n')
                    input('按任意键返回'.center(94,'-'))
                elif int(findselect)==2:
                    msg=input('是否确认修改密码 y/n?')
                    if msg=='y' or msg=='Y':
                        while True:
                            newpwd=input('请输入30以内字符:')
                            while True:
                                if not newpwd:
                                    input('更新失败,新密码不能为空')
                                    break
                                elif len(newpwd)>30:
                                    input('更新失败,密码限制30个字符')
                                    break
                                else:
                                    surepwd=input('请输入确认密码:')
                                    if not newpwd==surepwd:
                                        input('确认密码错误')
                                        continue
                                    else:
                                        sql=f'update user set password="{newpwd}" where t_id={teacherid};'
                                        input('修改该密码成功')
                                        break
                            break
                    else:
                        continue
        elif int(selected)==2:
            while True:
                clear()
                print(t_s_options)
                print('按其他任意键返回'.center(28,'-'),'\n')
                i=input('请输入您要添加的选项:')
                if not i.isdigit():
                    break
                elif int(i)==1:
                    clear()
                    t_Student(teacherid)
                    input('按其他任意键返回'.center(82,'-'))
                elif int(i)==2:
                    while True:
                        clear()
                        print(t_score_options)
                        scoreselected=input('请输入选项:')
                        if not scoreselected.isdigit():
                            break
                        elif int(scoreselected)==1:
                            while True:
                                clear()
                                try:
                                    time=input('请输入某年某学期:')
                                    sub_sql=f'select subject_id from teachers where teachers.id={teacherid};'
                                    cursor.execute(sub_sql)
                                    sub_id=cursor.fetchone()[0]
                                    sql=f'select scores.time,students.name,SubjectName,scores.score from teachers left join class on teachers.id=class.teacher_id or teachers.id=class.t1_id or teachers.id=class.t2_id or  teachers.id=class.t3_id or  teachers.id=class.t4_id or  teachers.id=class.t5_id left join students on students.class_id=class.id left join scores on scores.stu_id=students.id left join subjects on scores.sub_id=subjects.id where teachers.id={teacherid} and scores.time="{time}" and scores.sub_id={sub_id} order by students.id;'
                                    cursor.execute(sql)
                                    data=cursor.fetchall()
                                    clear()
                                    print(f'{time}'.center(60,'-'))
                                    print('姓名'.center(18,' '),'|','学科'.center(18,' '),'|','成绩'.center(18,' '))
                                    print('-'*65)
                                    for utime,name,subject,uscore in data:
                                        print(f'{name}'.center(20-len(name),' '),'|',f'{subject}'.center(20-len(subject),' '),'|',f'{uscore}'.center(20,' '))
                                        print('-'*65)
                                    print('\n')
                                    input('按其他任意键返回'.center(57,'-')) 
                                    break
                                except:
                                    print('查询失败,请稍后重试......')
                        elif int(scoreselected)==2:
                            while True:
                                clear()
                                t_Student(teacherid)
                                time=input('请输入某年某学期:')
                                idcard=input('请输入学生号:')
                                score=input('请输入学生本门课的成绩:')
                                stusql=f'select id from students where idcard={idcard};'
                                subsql=f'select teachers.subject_id from teachers where teachers.id={teacherid};'
                                cursor.execute(stusql)
                                stuid=cursor.fetchone()[0]
                                cursor.execute(subsql)
                                subid=cursor.fetchone()[0]
                                try:
                                    sql=f'insert into scores(time,score,stu_id,sub_id)values("{time}",{score},{stuid},{subid});'
                                    cursor.execute(sql)
                                    print('输入成功')
                                except:
                                    print('输入失败,请稍后重试.....')
                                msg=input('是否继续输入成绩 y?n')
                                if msg=='y' or msg=='Y':
                                    continue
                                else:
                                    break
                            input('按其他任意键返回'.center(82,'-')) 
                        else:
                            break
                else:
                    break
        elif int(selected)==3:
            clear()
            sql=f'select ClassName,time,week,weeknum,classnum,SubjectName from teachers left join subjects on teachers.subject_id=subjects.id left join courses on courses.sub_id=teachers.subject_id left join class on class.teacher_id=teachers.id where teachers.id={teacherid} and class.id=courses.class_id;'
            cursor.execute(sql)
            data=cursor.fetchall()
            
            table={'周一':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周二':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周三':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周四':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周五':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周六':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周日':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''}}
            
            for classname,time,week,weeknum,classnum,subjectname in data:
                table[weeknum][classnum]=subjectname
            

            print(f'2019年第一学期第一周'.center(93,'-'))
            print(' '.center(10,' '),'|','周一'.center(8,' '),'|','周二'.center(8,' '),'|','周三'.center(8,' '),'|','周四'.center(8,' '),'|','周五'.center(8,' '),'|','周六'.center(8,' '),'|','周日'.center(8,' '))
            print('-'*101)
            print('第一大节'.center(6,' '),'|',table['周一']['第一大节'].center(10 if table['周一']['第一大节']=='' else 8,' '),'|',table['周二']['第一大节'].center(10 if table['周二']['第一大节']=='' else 8,' '),'|',table['周三']['第一大节'].center(10 if table['周三']['第一大节']=='' else 8,' '),'|',table['周四']['第一大节'].center(10 if table['周四']['第一大节']=='' else 8,' '),'|',table['周五']['第一大节'].center(10 if table['周五']['第一大节']=='' else 8,' '),'|',table['周六']['第一大节'].center(10 if table['周六']['第一大节']=='' else 8,' '),'|',table['周日']['第一大节'].center(10 if table['周日']['第一大节']=='' else 8,' '))

            print('-'*101)
            
            print('第二大节'.center(6,' '),'|',table['周一']['第二大节'].center(10 if table['周一']['第二大节']=='' else 8,' '),'|',table['周二']['第二大节'].center(10 if table['周二']['第二大节']=='' else 8,' '),'|',table['周三']['第二大节'].center(10 if table['周三']['第二大节']=='' else 8,' '),'|',table['周四']['第二大节'].center(10 if table['周四']['第二大节']=='' else 8,' '),'|',table['周五']['第二大节'].center(10 if table['周五']['第二大节']=='' else 8,' '),'|',table['周六']['第二大节'].center(10 if table['周六']['第二大节']=='' else 8,' '),'|',table['周日']['第二大节'].center(10 if table['周日']['第二大节']=='' else 8,' '))

            print('-'*101)
            print('第三大节'.center(6,' '),'|',table['周一']['第三大节'].center(10 if table['周一']['第三大节']=='' else 8,' '),'|',table['周二']['第三大节'].center(10 if table['周二']['第三大节']=='' else 8,' '),'|',table['周三']['第三大节'].center(10 if table['周三']['第三大节']=='' else 8,' '),'|',table['周四']['第三大节'].center(10 if table['周四']['第三大节']=='' else 8,' '),'|',table['周五']['第三大节'].center(10 if table['周五']['第三大节']=='' else 8,' '),'|',table['周六']['第三大节'].center(10 if table['周六']['第三大节']=='' else 8,' '),'|',table['周日']['第三大节'].center(10 if table['周日']['第三大节']=='' else 8,' '))

            print('-'*101)
            print('第四大节'.center(6,' '),'|',table['周一']['第四大节'].center(10 if table['周一']['第四大节']=='' else 8,' '),'|',table['周二']['第四大节'].center(10 if table['周二']['第四大节']=='' else 8,' '),'|',table['周三']['第四大节'].center(10 if table['周三']['第四大节']=='' else 8,' '),'|',table['周四']['第四大节'].center(10 if table['周四']['第四大节']=='' else 8,' '),'|',table['周五']['第四大节'].center(10 if table['周五']['第四大节']=='' else 8,' '),'|',table['周六']['第四大节'].center(10 if table['周六']['第四大节']=='' else 8,' '),'|',table['周日']['第四大节'].center(10 if table['周日']['第四大节']=='' else 8,' '))

            print('-'*101)
            print('\n')
            input('按Enter返回'.center(98,'-'))
        else:
            clear()
            msg=input('确认退出? y/n')
            if msg=='y' or msg=='Y':
                print('退出成功'.center(28,'-'),'\n')
                break
            else:
                continue

def StudentJiemian(stuid):
    while True:
        clear()
        print(studentoptions)
        selected=input('请输入您要进行的操作:')
        if not selected.isdigit():
            clear()
            msg=input('确认退出? y/n')
            if msg=='y' or msg=='Y':
                print('退出成功'.center(28,'-'),'\n')
                break
            else:
                continue
        elif int(selected)==1:
            while True:
                clear()
                print(s_my_options)
                my_selected=input('请输入您要进行的操作:')
                if not my_selected.isdigit():
                    break
                elif int(my_selected)==1:
                    clear()
                    sql=f'select ClassName,idcard,name,age,sex from students left join class on students.class_id=class.id where students.id={stuid};'
                    cursor.execute(sql)
                    data=cursor.fetchone()
                    print('学生个人信息'.center(104,'-'))
                    print('班级'.center(18,' '),'|','学号'.center(18,' '),'|','姓名'.center(18,' '),'|','年龄'.center(18,' '),'|','性别'.center(18,' '))
                    print('-'*110)
                    print(data[0].center(20,' '),'|',str(data[1]).center(20,' '),'|',data[2].center(20-len(data[2]),' '),'|',str(data[3]).center(20,' '),'|',data[4].center(20-len(data[4]),' '))
                    print('-'*110,'\n')
                    input('按Enter键退出'.center(106,'-'))
                    continue
                elif int(my_selected)==2:
                    clear()
                    msg=input('是否确认修改密码 y/n?')
                    if msg=='y' or msg=='Y':
                        while True:
                            newpwd=input('请输入30以内字符:')
                            while True:
                                if not newpwd:
                                    input('更新失败,新密码不能为空')
                                    break
                                elif len(newpwd)>30:
                                    input('更新失败,密码限制30个字符')
                                    break
                                else:
                                    surepwd=input('请输入确认密码:')
                                    if not newpwd==surepwd:
                                        input('确认密码错误')
                                        continue
                                    else:
                                        sql=f'update user set password="{newpwd}" where s_id={stuid};'
                                        input('修改该密码成功')
                                        break
                            break
                    else:
                        continue
                else:
                    break
        elif int(selected)==2:
            clear()
            sql=f'select weeknum,classnum,SubjectName from students left join courses on students.class_id=courses.class_id left join subjects on courses.sub_id=subjects.id where students.id={stuid};'
            cursor.execute(sql)
            data=cursor.fetchall()
            
            table={'周一':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周二':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周三':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周四':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周五':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周六':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''},'周日':{'第一大节':'','第二大节':'','第三大节':'','第四大节':''}}
            
            for weeknum,classnum,subjectname in data:
                table[weeknum][classnum]=subjectname
            

            print(f'2019年第一学期第一周'.center(93,'-'))
            print(' '.center(10,' '),'|','周一'.center(8,' '),'|','周二'.center(8,' '),'|','周三'.center(8,' '),'|','周四'.center(8,' '),'|','周五'.center(8,' '),'|','周六'.center(8,' '),'|','周日'.center(8,' '))
            print('-'*101)
            print('第一大节'.center(6,' '),'|',table['周一']['第一大节'].center(10 if table['周一']['第一大节']=='' else 8,' '),'|',table['周二']['第一大节'].center(10 if table['周二']['第一大节']=='' else 8,' '),'|',table['周三']['第一大节'].center(10 if table['周三']['第一大节']=='' else 8,' '),'|',table['周四']['第一大节'].center(10 if table['周四']['第一大节']=='' else 8,' '),'|',table['周五']['第一大节'].center(10 if table['周五']['第一大节']=='' else 8,' '),'|',table['周六']['第一大节'].center(10 if table['周六']['第一大节']=='' else 8,' '),'|',table['周日']['第一大节'].center(10 if table['周日']['第一大节']=='' else 8,' '))

            print('-'*101)
            
            print('第二大节'.center(6,' '),'|',table['周一']['第二大节'].center(10 if table['周一']['第二大节']=='' else 8,' '),'|',table['周二']['第二大节'].center(10 if table['周二']['第二大节']=='' else 8,' '),'|',table['周三']['第二大节'].center(10 if table['周三']['第二大节']=='' else 8,' '),'|',table['周四']['第二大节'].center(10 if table['周四']['第二大节']=='' else 8,' '),'|',table['周五']['第二大节'].center(10 if table['周五']['第二大节']=='' else 8,' '),'|',table['周六']['第二大节'].center(10 if table['周六']['第二大节']=='' else 8,' '),'|',table['周日']['第二大节'].center(10 if table['周日']['第二大节']=='' else 8,' '))

            print('-'*101)
            print('第三大节'.center(6,' '),'|',table['周一']['第三大节'].center(10 if table['周一']['第三大节']=='' else 8,' '),'|',table['周二']['第三大节'].center(10 if table['周二']['第三大节']=='' else 8,' '),'|',table['周三']['第三大节'].center(10 if table['周三']['第三大节']=='' else 8,' '),'|',table['周四']['第三大节'].center(10 if table['周四']['第三大节']=='' else 8,' '),'|',table['周五']['第三大节'].center(10 if table['周五']['第三大节']=='' else 8,' '),'|',table['周六']['第三大节'].center(10 if table['周六']['第三大节']=='' else 8,' '),'|',table['周日']['第三大节'].center(10 if table['周日']['第三大节']=='' else 8,' '))

            print('-'*101)
            print('第四大节'.center(6,' '),'|',table['周一']['第四大节'].center(10 if table['周一']['第四大节']=='' else 8,' '),'|',table['周二']['第四大节'].center(10 if table['周二']['第四大节']=='' else 8,' '),'|',table['周三']['第四大节'].center(10 if table['周三']['第四大节']=='' else 8,' '),'|',table['周四']['第四大节'].center(10 if table['周四']['第四大节']=='' else 8,' '),'|',table['周五']['第四大节'].center(10 if table['周五']['第四大节']=='' else 8,' '),'|',table['周六']['第四大节'].center(10 if table['周六']['第四大节']=='' else 8,' '),'|',table['周日']['第四大节'].center(10 if table['周日']['第四大节']=='' else 8,' '))

            print('-'*101)
            print('\n')
            input('按Enter返回'.center(98,'-'))
        elif int(selected)==3:
            clear()
            sql=f'select SubjectName,scores.score from students left join scores on students.id=scores.stu_id left join subjects on subjects.id=scores.sub_id where students.id={stuid};'
            cursor.execute(sql)
            data=cursor.fetchall()
            print('2019年第二学期学生成绩表'.center(30,'-'))
            print('科目'.center(18,' '),'|','成绩'.center(18,' '))
            print('-'*40)
            for sub,score in data:
                print(sub.center(20-len(sub),' '),'|',str(score).center(20,' '))
                print('-'*40)
            print('\n')
            input('按Enter键返回'.center(36,'-'))
        elif int(selected)==4:
            clear()
            classsql=f'select class_id from students where id={stuid};'
            cursor.execute(classsql)
            class_id=cursor.fetchone()[0]
            sql=f'select t5.id,t5.ClassName,t5.TeacherName,t5.t1name,t5.t2name,t5.t3name,t5.t4name,teachers.TeacherName as t5name from (select t4.id,t4.ClassName,t4.TeacherName,t4.t1name,t4.t2name,t4.t3name,teachers.TeacherName as t4name,t4.t5_id from (select t3.id,t3.ClassName,t3.TeacherName,t3.t1name,t3.t2name,teachers.TeacherName as t3name,t3.t4_id,t3.t5_id from (select t2.id,t2.ClassName,t2.TeacherName,t2.t1name,teachers.TeacherName as t2name,t2.t3_id,t2.t4_id,t2.t5_id from (select t1.id,t1.ClassName,t1.TeacherName,teachers.TeacherName as t1name,t1.t2_id,t1.t3_id,t1.t4_id,t1.t5_id from (select class.id,ClassName,TeacherName,t1_id,t2_id,t3_id,t4_id,t5_id from class left join teachers on class .teacher_id=teachers.id where class.id={class_id}) as t1 left join teachers on t1.t1_id=teachers.id) as t2 left join teachers on t2.t2_id=teachers.id) as t3 left join teachers on teachers.id=t3.t3_id) as t4 left join teachers on teachers.id=t4.t4_id) as t5 left join teachers on t5.t5_id=teachers.id;'
            cursor.execute(sql)
            datat=cursor.fetchone()
            data=[]
            for x in datat:
                x='无数据' if not x else x
                data.append(x)
            sublist=[]
            for n in data[2:]:
                sql=f'select subjects.SubjectName from teachers left join subjects on teachers.subject_id=subjects.id where teachers.TeacherName="{n}";'
                cursor.execute(sql)
                sub=cursor.fetchone()
                sub=('无数据',) if not sub else sub
                sublist.append(sub[0])
            print('-'*113)
            print('班级'.center(13,' '),end='|')
            print('班主任'.center(12,' '),end='|')
            print(f'{sublist[1]}'.center(15-len(sublist[0]),' '),end='|')
            print(f'{sublist[2]}'.center(15-len(sublist[1]),' '),end='|')
            print(f'{sublist[3]}'.center(15-len(sublist[2]),' '),end='|')
            print(f'{sublist[4]}'.center(15-len(sublist[3]),' '),end='|')
            print(f'{sublist[5]}'.center(15-len(sublist[4]),' '))
            print('-'*113)
            print(f'{data[1]}'.center(15,' '),end='|')
            print(f'{data[2]}'.center(15-len(data[2]),' '),end='|')
            print(f'{data[3]}'.center(15-len(data[3]),' '),end='|')
            print(f'{data[4]}'.center(15-len(data[4]),' '),end='|')
            print(f'{data[5]}'.center(15-len(data[5]),' '),end='|')
            print(f'{data[6]}'.center(15-len(data[6]),' '),end='|')
            print(f'{data[7]}'.center(15-len(data[7]),' '))
            print('-'*113,'\n')
            input('按Enter返回'.center(110,'-'))
        else:
            clear()
            msg=input('确认退出? y/n')
            if msg=='y' or msg=='Y':
                print('退出成功'.center(28,'-'),'\n')
                break
            else:
                continue

while True:
    clear()
    print(loginoptions)
    model=input('请输入选项:')
    if not model.isdigit():
        clear()
        print('退出成功'.center(36,'-'))
        break
    elif int(model)==0:
        username=input('请输入管理员账号:')
        userpwd=input('请输入密码:')
        sql=f'select password from user where username="{username}" and Type=0;'
        cursor.execute(sql)
        pwd=cursor.fetchone()
        if not pwd==None:
            pwd=pwd[0]
            if userpwd==pwd:
                GuanLi() 
            else:
                input('密码错误!!!')
        else:
            input('账号错误!!!')
    elif int(model)==1: 
        username=input('请输入老师账号:')
        userpwd=input('请输入密码:')
        sql=f'select password,t_id from user where username="{username}" and Type=1;'
        cursor.execute(sql)
        data=cursor.fetchone()
        if not data==None:
            pwd=data[0]
            if userpwd==pwd:
                TeacherJiemian(data[1])
            else:
                input('密码错误!!!')
        else:
            input('账号错误!!!')
    elif int(model)==2: 
        username=input('请输入学生账号:')
        userpwd=input('请输入密码:')
        sql=f'select password,s_id from user where username="{username}" and Type=2;'
        cursor.execute(sql)
        data=cursor.fetchone()
        if not data==None:
            pwd=data[0]
            if userpwd==pwd:
                StudentJiemian(data[1])
            else:
                input('密码错误!!!')
        else:
            input('账号错误!!!')
    else:
        clear()
        print('退出成功'.center(36,'-'))
        break

db.close()

