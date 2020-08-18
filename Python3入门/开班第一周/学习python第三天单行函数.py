'''
1.去重：distinct关键字

需求：查看公司一共有多少部门？

select department_id from employees;此代码会查出107条记录，存在部门重复的问题！

select distinct department_id from employees;

思考：参看如下代码有没有问题？

select employee_id,last_name,distinct department_id from employees;

解答：会出现问题(报错了)，出错原因，因为在执行代码的过程中对于employee_id，last_name这两列都有107条数据，

而department_id去重之后只有12条数据，数量对不上了！所以报错了！总结：使用distinct需谨慎...

2.单行函数：

概念：单数据进单结果出(单进单出)

分类学习：

1).字符函数

2).数字函数

3).日期函数

4).转换函数

5).通用函数

字符函数：
1).大小写转换函数：3个

①.lower(m)：将字符串中所有字符转换为全小写

②.upper(m)：将字符串中所有字符转换为全大写

③.initcap(m)：将字符串中首字母转为大写，其余字母转换小写

代码实现：

select lower('ORACLE'),upper('oracle'),initcap('oRACLE') from dual;

需求：查询名字为Bell这个人的信息？

select * from employees where lower(last_name) = 'bell';

select * from employees where upper(last_name) = 'BELL';

select * from employees where initcap(last_name) = 'Bell';

2).字符控制函数：8个

①.concat(m,n)：将字符串m和字符串n拼接得到一个更长的新字符串

代码实现：

select concat('Hello','World') from dual;

select concat(last_name,first_name) from employees;

②.length(m)：得到某个数据的长度

代码实现：

select length('python'),length(123456) from dual;

select length(employee_id),length(first_name),length(hire_date) from employees;

③.substr(x,y,z)：将x从y位置开始截取z个长度得到一个新的字符串返回给程序

参数解释：

x：原本的字符串数据

y：起点位置(下标，索引)

z：截取的长度

代码实现：

select substr('HelloWorld',1,5) from dual;

④.instr(m,n)：

参数解释：判断某个字符在字符串中首次出现的位置

m：字符串

n：一个字符

代码实现：

select instr('HelloWorld','l') from dual;

⑤.replace(x,y,z)：将x中的字符y，全部替换为字符z

参数解释：

x：字符串

y：字符串中某个字符

z：需要被替换成的字符

代码实现：

select replace('aaabcdaacdaabefaanba','a','6') from dual;

⑥.trim(x from y)：去除y字符串中首尾的字符x

参数解释：

x：字符

y：字符串

代码实现：

select trim('m' from 'mmmmHellmmmomWmmorldmmmmm') from dual;

⑦和⑧.lpad和rpad函数(了解)

lpad(x,y,z)：

rpad(x,y,z)：

代码实现：

select lpad(salary,10,'*'),rpad(salary,10,'*') from employees;

2.数字函数：3个

①.round(m,n)：四舍五入

②.trunc(m,n)：截断

③.mod(m,n)：求余

代码实现：

select round(439.456,1),round(439.456,0),round(439.456,-1) from dual;

select trunc(439.456,1),trunc(439.456,0),trunc(439.456,-1) from dual;

select mod(1100,300) from dual;

3.日期函数：3个

1).日期

2).时间

①.months_between(m,n)：用于计算两个日期之间相差的月数(精确)

②.add_months(m,n)：在原本的m月份基础上增加或者删除n个月

③.last_day(m)：得到某个日期所在月份的最后一天

关键字：sysdate表示当前系统时间

测试如下代码：

select sysdate from dual;

以上代码由于数据库内部的格式限制只能显示出日期部分数据而不能显示出时间，

我们可以使用转换函数to_char(x,y)来实现日期和时间的显示

补充：oracle中的特殊字母有以下这些

yyyy：年

mm：月

dd：天

day：星期

hh：小时(1-12)

hh24：小时(0-23)

mi：分钟

ss：秒

重构上述代码实现日期时间数据的显示：

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;

参看如下代码：

select sysdate + 1,sysdate,sysdate - 2 from dual;

select (sysdate - hire_date) from employees;

总结：

对于日期数据可以和数字做加减运算，得到的结果就是往前或者往后的天数

对于日期和日期数据之间只能做减法运算，得到的结果就是两个日期数据之间相差的天数

案例：

1).查询公司员工入职至今一共多少天了？(使用截断保留到整数位，别名worked_day)

select last_name,hire_date,trunc(sysdate - hire_date) "worked_day" from employees;

2).查询公司员工入职至今一共多少个月了？(粗糙版本：假设每月都是30天)

select last_name,hire_date,(sysdate - hire_date) / 30 "month_work",

months_between(sysdate,hire_date) "mon_work" from employees;

3).查询公司在每个月倒数第二天入职的员工有哪些？

select last_name,hire_date from employees

where last_day(hire_date) - 1 = hire_date;

select last_day(sysdate) from dual;

select add_months(sysdate,2),add_months(sysdate,-3) from dual;

4.转换函数：3个

1).to_date

2).to_char

3).to_number

补充：

转换函数中涉及到的格式字符：

9-->表示1位

99-->表示2位

举例：

select to_number('123456','999999') from dual;早版本，需要定义格式(位数)

select to_number('123456') from dual;新版本，可以省略格式

【注意事项】：

在使用to_number函数进行数据转换时，我们一定要计算正确需要被转换的数据的长度，

才能精确定义格式中需要的位数，一旦位数过少，直接报错！！

需求：

查询公司员工的部门编号，如果没有部门的显示"没有部门"

select last_name,department_id,nvl(to_char(department_id,'999'),'没有部门') from employees;

select last_name,department_id,nvl(to_char(department_id),'没有部门') from employees;

5.通用函数

1).nvl(expr1,expr2)：

2).nvl2(expr1,expr2,expr3)：

nvl2函数的执行流程：

在执行过程中会先执行expr1，如果expr1的结果不为null，那么执行expr2；

如果expr1的结果为null，那么执行expr3；

需求：

查询员工编号，姓名，薪资，奖金率；

如果奖金率不为空，那么显示奖金率 + 0.015以后的结果，

如果奖金率为空，那么显示0.01；

代码实现：

select employee_id,last_name,salary,commission_pct,

nvl2(commission_pct,commission_pct + 0.015,0.01) "new_comm"

from employees;

sql中的判断结构的引入讲解：

两种：

1).case表达式

模板格式：

case 字段 when expr1 then x

when expr2 then y

when expr3 then z

...

else n end;

需求：

查询公司员工的编号、姓名、薪资，部门号，

如果是70号部门的员工，就显示工资的1.1倍，

如果是80号部门的员工，就显示工资的1.2倍，

如果是90号部门的员工，就显示工资的1.3倍，

其余部门已正常工资显示；

代码如下：

select employee_id,last_name,salary,department_id,

case department_id when 70 then salary * 1.1

when 80 then salary * 1.2

else salary * 1.3 end

-- when 90 then salary * 1.3 end

-- else salary end

from employees

where department_id in(70,80,90);

2).decode函数

模板格式：

decode(字段,expr1,val1,expr2,val2,...)：

需求：

查询公司员工的编号、姓名、薪资，部门号，

如果是70号部门的员工，就显示工资的1.1倍，

如果是80号部门的员工，就显示工资的1.2倍，

如果是90号部门的员工，就显示工资的1.3倍，

其余部门已正常工资显示；

代码如下：

select employee_id,last_name,salary,department_id,

decode(department_id,70,salary * 1.1,

80,salary * 1.2,

-- 90,salary * 1.3,

salary * 1.3)

from employees

where department_id in(70,80,90);
'''