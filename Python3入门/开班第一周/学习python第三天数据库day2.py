'''
day01回顾：

数据库：

定义：存储数据的仓库(database,简称db)

常用的数据库对象有哪些？

1).数据表(table) *****

2).视图(view)

3).索引(index)

4).序列(sequence)

主流的关系型数据库有哪些？(枚举)

oracle、mysql、sqlserver、db2...

谈一谈oracle和mysql的区别？

oracle：

1).收费的(贵)

2).数据的存储量大，安全性高、效率比较快

mysql：

1).免费

2).数据的存储量小(相对而言的)，安全系数以及效率方面较低(相对而言的)

sql：structure query language(结构化查询语言)

分类：

DDL：结构层面的操作，自动提交，无法回滚 比较强硬

包括的常用的操作如下：

建表、删表、修改表、清空表 --> 总结：结构发生变化了，都是ddl操作

建表的格式：

create table 表名(

列名1 数据类型(长度),

列名2 数据类型(长度),

...

列名n 数据类型(长度)

);

建完表格之后我们可以使用desc关键字去查看表结构，

desc关键字的使用如下：

desc 表名;

DML：数据层面的操作：不会自动提交，可以回滚比较柔和

包括的常用的操作如下：

增加数据(insert into ...)

删除数据(delete from 表名 where ...)

修改数据(update 表名 set 列名1 = 值1,列名2 = 值2,... where ...)

查询数据(select ... from 表名)

总结：

对于删除和修改数据而言，一般情况下都需要配合where子句进行相应的操作，否则会出现全删或者全改的问题！！

DCL：

两个关键字：commit(提交)、rollback(回滚)

day02(上午)：

出题思考如何实现？

1).查询公司员工的编号，姓名，薪资，奖金率以及月收入？

以下代码有问题：因为有null值参与了算数运算，导致结果直接为null了，出现了与现实不符的情况！！

select employee_id,last_name,salary,commission_pct,salary + salary * commission_pct from employees;

使用去空置换函数：nvl(m,n)：

执行过程如下：

如果m得到的内容不为null，那么就拿它本身参与运算

如果m得到的内容为null，那么就用n的值参与运算

重构以上代码：

select employee_id,last_name,salary,commission_pct,salary + salary * nvl(commission_pct,0) from employees;

sql中的别名：

概念：使用别名的思想，可以让显示变得更加的优雅、简洁！并且可以优化我们的代码...

起别名有三种方式：
方式一：

select employee_id,last_name,salary,commission_pct,salary + salary * nvl(commission_pct,0) as month_sal

from employees;

方式二：

select employee_id,last_name,salary,commission_pct,salary + salary * nvl(commission_pct,0) month_sal

from employees;

方式三：

select employee_id,last_name,salary,commission_pct,salary + salary * nvl(commission_pct,0) "month_sal"

from employees;

比较理解以上的三种方式：

方式二可以认为是方式一的简化版，它们定义的别名在查询显示的时候，都是以全大写来进行显示

如果想要控制显示的大小写(效果)，我们可以使用方式三来完成；我们可以认为方式三才是最实用的方式

where子句：

在查询数据的时候，很多情况下我们需要过滤掉一些不需要的内容，所以需要用到where子句来实现

记住：

where紧随from

运算符：

分类：

1).比较运算符：

范围：

>大于

>=大于等于

<小于

<=小于等于

=等于

<>不等于(还可以这么写：!=)

案例阶段：

①.查询员工号为200的员工的姓名、薪资和入职时间？

select last_name,salary,hire_date from employees where employee_id = 200;

②.查询工资大于8000的员工有哪些？

select * from employees where salary > 8000;

③.查询在90号部门工作的员工的编号，姓名和部门号？

select employee_id,last_name,department_id from employees where department_id = 90;

2).逻辑运算符

范围：

and：逻辑与(并且，取交集)

or：逻辑或(或者，取并集)

not：逻辑非(取反)

案例阶段：

①.查询工资大于8000并且小于等于14000的员工有哪些？

select * from employees where salary > 8000 and salary <= 14000;

②.查询工资大于8000或者小于等于14000的员工有哪些？

select * from employees where salary > 8000 or salary <= 14000;

③.查询在70，80，90号部门中工作的员工的员工号，姓名和部门编号？

select employee_id,last_name,department_id from employees where department_id = 70 or department_id = 80 or department_id = 90;

3).特殊比较运算符：

范围：

between...and...：在...范围之内，特点：含头含尾闭区间 举例：[3,10]

in(散列值)：只要在散列值的范围中有满足的，就成立

like：模糊查询

is null/is not null：判断是否为空

案例阶段：

①.查询工资大于等于8000并且小于等于14000的员工有哪些？

select * from employees where salary >= 8000 and salary <= 14000;

select * from employees where salary between 8000 and 14000;

②.查询在70，80，90号部门中工作的员工的员工号，姓名和部门编号？

select employee_id,last_name,department_id from employees where department_id in(70,80,90);

看一看以下代码的执行情况，然后自己分析一下(理解一下)sql的机制!

select employee_id,last_name,department_id from employees where department_id in(70,80,90,300);

select employee_id,last_name,department_id from employees where department_id in(70,80,90,null);

select employee_id,last_name,department_id from employees where department_id in(70,'80',90);

自己的结论：

①.如果传入的散列值不存在，不会报错；

②.对于传入数据的类型没有显示

③.如果传入的数据是字符型数据，在有需要的情况下，内部是可以去进行隐式的数据类型转换的

关于模糊查询：

需要涉及的内部的符号有：

_：表示1个字符

%：表示0-多个字符

案例阶段：

①.查询姓名中有字母a的员工有哪些？

select employee_id,last_name,department_id from employees where last_name like '%a%';

②.查询姓名中最后一个字母是a的员工有哪些？

select employee_id,last_name,department_id from employees where last_name like '%a';

③.查询姓名中第一个字母是a的员工有哪些？

select employee_id,last_name,department_id from employees where last_name like 'a%';

④.查询姓名中第三个字母是a的员工有哪些？

select employee_id,last_name,department_id from employees where last_name like '__a%';

让字符转义：escape关键字

⑤.查询姓名中有_的员工的信息？

select employee_id,last_name,department_id from employees where last_name like '%_%' escape'';

select employee_id,last_name,department_id from employees where last_name like '%#_%' escape'#';

关于is null/is not null的使用：

案例阶段：

①.查询公司中有奖金的员工的信息

select * from employees where commission_pct is not null;

②.查询公司中没有奖金的员工的信息

select * from employees where commission_pct is null;

思考1：查询姓名是Bell的员工的编号、姓名、薪资以及部门号

实现代码如下：

select employee_id,last_name,salary,department_id from employees where last_name = 'bell';

select employee_id,last_name,salary,department_id from employees where last_name = 'Bell';

SELECT EMPLOYEE_ID,last_name,Salary,DEPARTMENT_ID FROM employees WHERE last_name = 'Bell';

【注意事项】:

①.sql语句对于关键字、表名、列名这些内容的书写，大小小写无所谓(都能识别)

②.sql语句对于字符串数据层面的书写，必须严格区分大小写

③.一条sql语句可以显示的在多行中书写，一般我们按照各个子句(关键字)适当的进行换行

思考2：查询1994/06/07入职的员工的信息

实现代码如下：

select employee_id,last_name,salary,hire_date,department_id from employees where hire_date = '1994-06-07';报错！

select employee_id,last_name,salary,hire_date,department_id from employees where hire_date = '1994/06/07';报错！！

select employee_id,last_name,salary,hire_date,department_id from employees where hire_date = '07-6月-94';终于对了！！！(猜出来的)

以上的select查询我们涉及到了匹配日期数据，如果直接用=号进行匹配，格式要求比较高，一旦不满足直接就报错；

所以我们需要找到一种更加有效的方式来解决，方式如下：

to_char(obj,format)：传入obj数据，以format的格式进行转换，终于返回给程序一个字符串数据

代码重构如下：

select employee_id,last_name,salary,hire_date,department_id from employees where to_char(hire_date,'yyyy-mm-dd') = '1994-06-07';

select employee_id,last_name,salary,hire_date,department_id from employees where to_char(hire_date,'yyyy/mm/dd') = '1994/06/07';

对于以下代码：

涉及到了特殊字符(年、月、日)，我们需要在定义格式的时候，在特殊字符的外侧包裹一层双引号；

select employee_id,last_name,salary,hire_date,department_id from employees where to_char(hire_date,'yyyy"年"mm"月"dd"日"') = '1994年06月07日';

select employee_id,last_name,salary,hire_date,to_char(hire_date,'yyyy-mm-dd'),department_id from employees

where to_char(hire_date,'yyyy-mm-dd') = '1994-06-07';

案例练习：

①.查询80号部门工资小于等于9000的有哪些人？

select * from employees where department_id = 80 and salary <= 9000;

②.查询工资大于等于3000且职位中有MAN的员工的姓名,薪资和职位？

select last_name,salary,job_id from employees where salary >= 3000 and job_id like '%MAN%';

③.查询工资大于等于3000或职位中有MAN的员工的姓名,薪资和职位？

select last_name,salary,job_id from employees where salary >= 3000 or job_id like '%MAN%';

④.查询职位除了PU_CLERK,ST_MAN,FI_ACCOUNT的员工姓名和职位？

select last_name,job_id from employees where job_id not in('PU_CLERK','ST_MAN','FI_ACCOUNT');

---------------------------------------------------------------------------------------------------

排序：

涉及的层面：升序、降序

order by子句：

关键字：

升序：asc

降序：desc

案例练习：

①.查询员工的编号、姓名、薪资以及部门号，然后以薪资进行升序排列

select employee_id,last_name,salary,department_id from employees order by salary asc;

select employee_id,last_name,salary,department_id from employees order by salary;不写关键字默认就是升序排列

②.查询员工的编号、姓名、薪资以及部门号，然后以薪资进行升序排列

select employee_id,last_name,salary,department_id from employees

order by salary desc;

③.查询员工的编号、姓名、薪资以及部门号，先以薪资进行升序排列，如果薪资重复了，再以姓名降序排列

select employee_id,last_name,salary,department_id from employees

order by salary asc,last_name desc;

还可以对别名进行排序

④.查询员工的编号、姓名、薪资、奖金率以及年收入(别名：year_sal)，然后以别名进行降序排列

select employee_id,last_name,salary,commission_pct,12 * (salary + salary * nvl(commission_pct,0)) "year_sal"

order by "year_sal" desc;

连接符的使用：||

需求：XXX的工作是YYY--->XXX `s job is YYY

分析：XXX数据来源是last_name，YYY数据来源是job_id，`s job is 数据内容的类型是字符型数据(写死的内容)

select last_name || ' `s job is ' || job_id "details" from employees;

今日知识点的总结：

1).nvl(a,b)函数的使用

2).别名(起别名有三种方式)

3).过滤操作(where子句)

4).运算符之比较运算符

5).运算符之特殊比较运算符

6).运算符之逻辑运算符

7).排序(order by子句)

8).连接符：||

已学子句的定义顺序归纳：select ... from ... where ... order by

1).where紧随from

2).order by 永远出现在select查询的最后位置
'''