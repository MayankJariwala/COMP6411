from itertools import chain
from collections import defaultdict
import compute
studentInfo_dict={}
a1_dict ={}
a2_dict ={}
project_dict ={}
t1_dict ={}
t2_dict ={}
studentInfo_list=[]
a1_list=[]
a2_list=[]
project_list=[]
t1_list=[]
t2_list=[]
with open('class.txt') as f:
    lines = f.readlines()
    class_length = len(lines)
    next_line = 0
    while next_line < class_length:
    	studentInfo_dict={}
    	a = lines[next_line].strip('\n').split('|')
    	studentInfo_dict["studentid"] = a[0]
    	studentInfo_dict["fname"] = a[1]
    	studentInfo_dict["lname"] = a[2]
    	next_line += 1 
    	studentInfo_list.append(studentInfo_dict)

with open('a1.txt') as f:
    a1_dict = {}
    lines = f.readlines()
    a1_length = len(lines)
    a1_total = int(lines[0])
    a1 = 1
    while a1 < a1_length:
    	a1_dict={}
    	a = lines[a1].strip('\n').split('|')
    	a1_dict["studentid"]=a[0]
    	a1_dict["a1"] = a[1]
    	a1 += 1    	
    	a1_list.append(a1_dict)

with open('a2.txt') as f:
    a2_dict = {}
    lines = f.readlines()
    a2_length = len(lines)
    a2_total = int(lines[0])
    a1 = 1
    while a1 < a2_length:
    	a2_dict={}
    	a = lines[a1].strip('\n').split('|')
    	a2_dict["studentid"]=a[0]
    	a2_dict["a2"] = a[1]
    	a1 += 1    	
    	a2_list.append(a2_dict)

with open('project.txt') as f:
    project_dict = {}
    lines = f.readlines()
    project_length = len(lines)
    project_total = int(lines[0])
    a1 = 1
    while a1 < project_length:
    	project_dict={}
    	a = lines[a1].strip('\n').split('|')
    	project_dict["studentid"]=a[0]
    	project_dict["project"] = a[1]
    	a1 += 1    	
    	project_list.append(project_dict)


with open('test1.txt') as f:
    t1_dict = {}
    lines = f.readlines()
    t1_length = len(lines)
    t1_total = int(lines[0])
    a1 = 1
    while a1 < t1_length:
    	t1_dict={}
    	a = lines[a1].strip('\n').split('|')
    	t1_dict["studentid"]=a[0]
    	t1_dict["t1"] = a[1]
    	a1 += 1    	
    	t1_list.append(t1_dict)

with open('test2.txt') as f:
    t2_dict = {}
    lines = f.readlines()
    t2_length = len(lines)
    t2_total = int(lines[0])
    a1 = 1
    while a1 < t2_length:
    	t2_dict={}
    	a = lines[a1].strip('\n').split('|')
    	t2_dict["studentid"]=a[0]
    	t2_dict["t2"] = a[1]
    	a1 += 1    	
    	t2_list.append(t2_dict)


l = compute.merge_lists(studentInfo_list, a1_list , a2_list, project_list, t1_list, t2_list, 'studentid')
keysInfo = {
'a1_length':a1_length,
'a2_length':a2_length,
't1_length':t1_length,
't2_length':t2_length,
'project_length':project_length,
'a1_total':a1_total,
'a2_total':a2_total,
't1_total':t1_total,
't2_total':t2_total,
'project_total':project_total
}
sorted_list = sorted(l, key = lambda i: i['studentid'])
compute.menu_opt(sorted_list,keysInfo)