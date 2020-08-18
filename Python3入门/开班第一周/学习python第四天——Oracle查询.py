'''
3.子查询(难)：

当进行查询的时候，发现需要的数据信息不明确，需要先通过另一个查询得到，

此查询称为子查询；

执行顺序：先执行子查询得到结果以后返回给主查询

组成部分：

1).主查询部分

2).子查询部分

【注意事项】：

子查询一定需要被定义/包裹在小括号内部，可以认为是显示的提升了代码执行的优先级

需求1：

查询薪资比Abel的高的有谁？

分析：

①.先查询出Abel的薪资是多少？

②.将过滤条件定义为>①，然后进行查询得到最终需要的结果

代码实现：

select last_name,salary

from employees

where salary > (

select salary from employees

where last_name = 'Abel'

);

需求2：

查询job_id与141号员工相同，salary比143号员工多的员工的姓名,job_id和salary？

代码实现：

select last_name,job_id,salary

from employees

where job_id = (

select job_id

from employees

where employee_id = 141

)

and salary > (

select salary

from employees

where employee_id = 143

);

课堂练习：

1).返回公司工资最少的员工的employee_id,job_id和salary

select employee_id,job_id,salary

from employees

where salary = (

select min(salary)

from employees

);

2).查询平均工资高于公司平均工资的部门有哪些

select department_id,avg(salary)

from employees

group by department_id

having avg(salary) > (

select avg(salary)

from employees

)

order by department_id desc;

3).查询最低工资大于20号部门最低工资的部门id和最低工资

select department_id,min(salary)

from employees

where department_id is not null

group by department_id

having min(salary) > (

select min(salary)

from employees

having department_id = 20

);

4).返回其它职位中比job_id为'IT_PROG'中最低工资低的员工的员工号,姓名,job_id以及salary

select employee_id,last_name,job_id,salary

from employees

where salary < (

select min(salary)

from employees

where job_id = 'IT_PROG'

);

4.多表查询/多表联查

概念：

使用场景，如果一条select语句中需要查询的列遍布多张数据表，

那么我们就必须使用多表查询了！！

分类：

等值连接和非等值连接

对于等值连接分方向：

1).内连接：返回多张表中共同满足的数据，取交集

2).外连接(左、右、满)：返回内连接数据的同时还会继续返回某张表中不匹配的一些记录数

3).自连接：从始至终都是一张表，模拟一张表派生为两张(它们的结构式一模一样的)，自己连自己

等值连接中的内连接：

需求：

查询所有员工的员工号、员工姓名以及部门的名字？

select employee_id,last_name,department_name

from employees,departments;

【注意】

以上查询得到了2889条记录，很多都是没有用的数据(脏数据)，

出现的原因是：没有添加有效的连接条件导致的，

而这种现象我们称为笛卡尔集现象；

我们日后的学习和开发环境中是绝对要避免的！！

如何保证我们之后的多表查询绝对不会出现笛卡尔集现象？

1).不能不写连接条件

2).连接条件必须是有效的

思考：如何修改上述的代码？

代码实现如下：

select employee_id,last_name,department_name

from employees,departments

where employees.department_id = departments.department_id;

需求：使用内连接来实现

查询员工的员工号、姓名、部门号、部门名字？

select employee_id,last_name,department_id,department_name

from employees,departments

where employees.department_id = departments.department_id;

以上代码出错了，出错原因：

因为对于department_id这个列在employees和departments两张表中都存在，

所以需要显示的告诉编译器，我从哪张表中获取数据内容的！

修改代码如下：

select employee_id,last_name,departments.department_id,department_name

from employees,departments

where employees.department_id = departments.department_id;

select employee_id,last_name,employees.department_id,department_name

from employees,departments

where employees.department_id = departments.department_id;

思考：没有重复的列可以使用名字.的形式来定义吗？---> 可以的

select employee.employee_id,employee.last_name,employees.department_id,departments.department_name

from employees,departments

where employees.department_id = departments.department_id;

上述代码运行以及结果方面不存在问题，但是在代码量上比较冗余！！我们可以使用如下的方式解决...

给名字起别名的方式：

修改代码如下：

select e.employee_id,e.last_name,e.department_id,d.department_name

from employees e,departments d

where e.department_id = d.department_id;

总结：对于多表查询，如果涉及n张表，至少需要有n-1个连接条件；

非等值连接：

需求：

查询员工的姓名、薪资以及薪资的等级

select last_name,salary,grade_level

from employees,job_grades

where salary between lowest_sal and highest_sal;

以上代码有问题，可以看到各个人的薪资等级，但是由于没有追加连接连接，还是出现了笛卡尔集现象；

我们需要慎用！一般之后非等值连接用的比较少，而且必须配合等值连接一起用；
'''