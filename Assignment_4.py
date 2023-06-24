#!/usr/bin/env python
# coding: utf-8

# Design a comprehensive application that offers CRUD (Create, Read, Update, Delete) functionality for managing employee records. Users can add new employees, update existing employee details, delete employees, and view a list of all employees. Additionally, incorporate features like sorting and filtering based on department, salary, or other criteria.
# 1.Create new employee
# 2.Update existing employee
# 3.Delete Employee
# 4.List all employee
# 5.Exit

# In[2]:


get_ipython().system('pip install mysql-connector-python')


# In[4]:


import mysql.connector


# In[5]:


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ems"
)


def employee_all():
    cursor = mydb.cursor()
    query = 'SELECT * FROM employee'
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print("\nEmployee Details:")
        print("-----------------")
        for row in result:
            print("Employee Id: ", row[0])
            print("Employee Name:", row[1])
            print("Salary:", row[2])
            print("Department:", row[3])
            print("------------------------\n")
    else:
        print("\nNo employees found\n")
    cursor.close()
    

def employee_insert(id1, name1,salary1, dept1):
    cursor = mydb.cursor()
    query = 'INSERT INTO employee (emp_id, emp_name, emp_salary, emp_dept) VALUES (%s, %s, %s, %s)'
    values = (id1, name1,salary1, dept1)
    cursor.execute(query, values)
    result = cursor.fetchall()
    print('\nSuccessfully Inserted\n')
    

    
def employee_read(read_1):
    cursor = mydb.cursor()
    query = 'SELECT * FROM employee WHERE emp_id LIKE %s'
    values = (read_1,)
    cursor.execute(query,values)
    result = cursor.fetchall()
    if result:
        print('\nEmployee Details:')
        print('-----------------')
        for row in result:
            print('Employee Id: ', row[0])
            print('Employee Name:', row[1])
            print('Salary:', row[2])
            print('Department:', row[3])
            print('------------------------\n')
    else:
        print('\nNo matching employees found\n')
    cursor.close()

    
    
def employee_update(upsalary1, upid1):
    cursor = mydb.cursor()
    query = 'UPDATE employee SET emp_salary = %s where emp_id LIKE %s'
    values = (upsalary1, upid1)
    cursor.execute(query, values)
    result = cursor.fetchall()
    print('\nUpdated Successfull\n')
    
    
    
def employee_delete(dele_id1):
    cursor = mydb.cursor()
    query = 'DELETE FROM employee where emp_id LIKE %s'
    values = (dele_id1,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    print('\nDeleted Successfull\n')
    
    
def employee_sort(sort1):
    cursor = mydb.cursor()
    
    if sort1 == 'id':
        query = 'SELECT * FROM employee ORDER BY emp_id'
    elif sort1 == 'name':
        query = 'SELECT * FROM employee ORDER BY emp_name'
    elif sort1 == 'salary':
        query = 'SELECT * FROM employee ORDER BY emp_salary'
    elif sort1 == 'dept':
        query = 'SELECT * FROM employee ORDER BY emp_dept'
    else:
        print('\nInvalid Column Name!\n')
        return
    
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print('\nEmployee Details:')
        print('-----------------')
        for row in result:
            print('Employee Id:', row[0])
            print('Employee Name:', row[1])
            print('Salary:', row[2])
            print('Department:', row[3])
            print('------------------------\n')
    else:
        print('\nNo matching found\n')
    cursor.close()
    
    
    
def employee_filter(filter1):
    cursor = mydb.cursor()
    query = 'SELECT * FROM employee WHERE emp_dept = %s'
    values = (filter1,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    if result:
        print('\nFiltered Employee Details:')
        print('---------------------------')
        for row in result:
            print('Employee Id: ', row[0])
            print('Employee Name:', row[1])
            print('Salary:', row[2])
            print('Department:', row[3])
            print('------------------------\n')
    else:
        print('\nNo matching employees found\n')
    cursor.close()



if __name__ == '__main__':
    
    while True:
        print('Employee Management System')
        print('--------------------------')
        print('1. Show all Employee')
        print('2. Employee Create')
        print('3. Employee Read')
        print('4. Employee Update')
        print('5. Employee Delete')
        print('6. Employee Sort')
        print('7. Employee Filter')
        print('8. Exit')
        
        sewy = int (input('\nEnter your Choice: '))
        
        
        if sewy == 1:
            employee_all()
        
        elif sewy == 2:
            id_2 = int(input('Enter id: '))
            name_2 = input('Enter name: ')
            salary_2 = float(input('Enter salary" '))
            dept_2 = input('Enter department: ')
            employee_insert(id_2, name_2, salary_2, dept_2)
        
        elif sewy == 3:
            read_2 = int(input('Enter ID to Read: '))
            employee_read(read_2)
        
        elif sewy == 4:
            up_id2 = int(input('Enter id to Update: '))
            up_sal2 = float(input('Enter Salary to update: '))
            employee_update(up_sal2, up_id2)
        
        elif sewy == 5:
            dele_id2 = input('Enter ID to Delete: ')
            employee_delete(dele_id2)
        
        elif sewy == 6:
            sort2 = input('Enter Column(id, name, salary, dept) to Sort: ')
            employee_sort(sort2)
            
        elif sewy == 7:
            filter2 = input('Enter Department(IT,HR,ER) to Filter: ')
            employee_filter(filter2)
            
            
        elif sewy == 8:
            break
        
        else:
            print('\nInvalid choice. Please try again \n')
    mydb.close()


# In[ ]:





# In[ ]:




