# School admain

## 介绍

python+pymysql+mysql 入门项目'教务管理系统'

## 软件架构

1. Linux(wsl ubuntu20.04)
2. Python(3.5.3)+PyMySQL(0.7.1)
3. Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

## 表结构

- school 数据库
- grades 年级表
- class 班级表 teacher_id(班主任 id) t1_id ~ t5_id(老师 id) grade_id(年级 id) Type(0 全科,1 理科,2 文科)
- teachers 老师表 subject_id(学科 id)
- subjects 学科表 Type(0 全科,1 理科,2 文科)
- scores 成绩表 time(年份学期 eg:2021-2022 年第一学期) score(成绩) stu_id(学生 id) sub_id(学科 id)
- courses 课程表 time(年份学期 eg:2021-2022 年第一学期) week(第几周 eg:第一周) weeknum(周几 eg:周一) classnum(第几节课 eg:第一大节) sub_id(学科 id)
- students 学生表 idcard(学号) class_id(班级 id)
- user 用户表 Type(0 管理员权限,1 老师权限,2 学生权限) t_id(老师 id) s_id(学生 id)

## 功能

#### 管理员权限

1. 年级/班级/老师/学生/科目的增删改查
2. 课程管理 (有年份/学期,第几周条件)

#### 老师权限

1. 个人信息查询
2. 修改密码
3. 学生管理 (管理自己所在班级的学生)
4. 成绩管理 (查看自己所在班级学生自己学科成绩)
5. 课程管理 (查看自己所在班级自己学科课程表)

#### 学生权限

1. 登录账号:学号 密码:123456
2. 我的信息
3. 修改密码
4. 查看自己所在班级的课程表(有年份/学期与第几周条件)
5. 查看自己所有成绩(有年份/学期条件)
6. 查看自己所在班级的所有老师

## 导入数据库

1. 新建 school 数据库
2. mysqldump -u 用户名 -p school < school.sql
