'''
1.分组的概念：

关键字：group by子句

结论：在select列表中如果出现了聚合函数，不是聚合函数的列，必须都要定义到group by子句的后面

需求：

查询公司各个部门的平均工资？

select department_id,avg(salary)

from employees

group by department_id;

需求提升：

查询公司各个部门不同工种的平均工资？

select department_id,job_id,avg(salary)

from employees

group by department_id,job_id;

2.having子句：

作用：用来过滤包含聚合函数的相关信息(数据)

位置：

可以再group by前也可以再 group by后面(比较随意)

需求：

查询40、60、80号部门中平均工资大于6000的部门信息？

以下代码实现有问题的：报错了！！

报错原因：如果需要对于聚合函数进行过滤不能使用where子句，

需要使用having子句来实现...

select department_id,avg(salary)

from employees

where avg(salary) > 6000 and department_id in(40,60,80)

group by department_id;

代码修改如下：

select department_id,avg(salary)

from employees

where department_id in(40,60,80)

having avg(salary) > 6000

group by department_id

order by department_id desc;
'''