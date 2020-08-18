'''
多行函数：(聚合函数/分组函数)

解释：多条数据进入，单条结果出来(多进单出)

1).max(obj)：最大值

2).min(obj)：最小值

3).sum(num)：求和

4).avg(num)：求平均值

5).count(obj)：计数

【注意事项】：

1).max()和min()两个函数可以接受任何数据类型的实际参数

2).sum()和avg()两个函数只能接受number类型的数据

3).多行函数/聚合函数/分组函数满足自动忽略空值的特点(在某些情况下，我们不应该忽略空值...)

案例如下：

查询公司薪资最高的、最低的、工资总和以及平均值的信息？

select max(salary),min(salary),sum(salary),avg(salary)

from employees;

参看如下代码并思考：

select max(last_name),max(hire_date),min(last_name),min(hire_date)

from employees;

关于count()的使用：

需求如下：

查询公司有多少员工？

select count(employee_id),count(last_name),count(hire_date) from employees;

select count(1),count(2),count(0),count(107),count('*') from employees;

执行以上代码发现效果都是正确的，我们以后做计数操作的时候，我们都用count('*')来实现；

查看如下代码：

select count(department_id),count(commission_pct) from employees;

执行以上代码发现问题所在，只要是多行函数/聚合函数/分组函数满足自动忽略空值的特点

修改以上代码实现需要的效果：

select count(nvl(department_id,100)),count(nvl(commission_pct,1)) from employees;

思考：avg() = sum() / count()？

答：以上的等式成立

需求如下：

查询公司的平均奖金率？

select avg(commission_pct),sum(commission_pct) / count(commission_pct),

sum(commission_pct) / count(nvl(commission_pct,2)),

sum(commission_pct) / 107,

sum(commission_pct) / count(*)

from employees;

作业：

--1.显示系统时间(注：日期+时间)

select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss') from dual;

--2.查询员工号，姓名，工资，以及工资提高百分之20%后的结果（new salary）

select employee_id,last_name,salary,salary * 1.2 "new salary" from employees;

--3.将员工的姓名按首字母排序，并写出姓名的长度（length）

select last_name,length(last_name) from employees order by last_name;

--4.查询各员工的姓名，并显示出各员工在公司工作的月份数（worked_month）。

select last_name,round(months_between(sysdate,hire_date),0) "worked_month" from employees;

--5.查询员工的姓名，以及在公司工作的月份数（worked_month），并按月份数降序排列

select last_name,round(months_between(sysdate,hire_date),0) "worked_month"

from employees

order by "worked_month" desc;

--方式一：

select last_name || ' earns $' || salary || ' monthly but wants $' || 3 * salary "Dream Salary" from employees;

--方式二：

select last_name || ' earns' || to_char(salary,'$99999') || ' monthly but wants' || to_char(3 * salary,'$99999') "Dream Salary" from employees;

select last_name "Last_name",job_id "Job_id",

decode(job_id,'AD_PRES','A',

'ST_MAN','B',

'IT_PROG','C',

'SA_REP','D',

'E') "Grade"

from employees

where job_id in('AD_PRES','ST_MAN','IT_PROG','SA_REP','ST_CLERK')

order by "Grade" desc;

select last_name "Last_name",job_id "Job_id",

case job_id when 'AD_PRES' then 'A'

when 'ST_MAN' then 'B'

when 'IT_PROG' then 'C'

when 'SA_REP' then 'D'

else 'E' end "Grade"

from employees

where job_id in('AD_PRES','ST_MAN','IT_PROG','SA_REP','ST_CLERK')

order by "Grade" desc;
'''