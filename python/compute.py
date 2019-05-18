import math
a1_wt = 7.5
a2_wt = 7.5
pr_wt = 25
t1_wt = 30
t2_wt = 30

def merge_lists(l1,l2,l3,l4,l5,l6,key):
  merged = {}
  for item in l1+l2+l3+l4+l5+l6:
    if item[key] in merged:
      merged[item[key]].update(item)
    else:
      merged[item[key]] = item
  return [val for (_, val) in merged.items()]
def merge_lists_for_two(l1,l2,key):
	merged = {}
	for item in l1+l2:
		if item[key] in merged:
		  merged[item[key]].update(item)
		else:
		  merged[item[key]] = item
	return [val for (_, val) in merged.items()]
def printA1GradesData(l):	
	for item in l:	
		x = "N/A" if (item.get("a1") == None) else item.get("a1")
		print(item.get("studentid") + "\t" + item.get("lname") + "," + item.get("fname") +"\t" + x )
def printA2GradesData(l):	
	for item in l:	
		x = "N/A" if (item.get("a2") == None) else item.get("a2")
		print(item.get("studentid") + "\t" + item.get("lname") + "," + item.get("fname") +"\t" + x )
def printProjectGradesData(l):	
	for item in l:	
		x = "N/A" if (item.get("project") == None) else item.get("project")
		print(item.get("studentid") + "\t" + item.get("lname") + "," + item.get("fname") +"\t" + x )
def printTest1GradesData(l):	
	for item in l:	
		x = "N/A" if (item.get("t1") == None) else item.get("t1")
		print(item.get("studentid") + "\t" + item.get("lname") + "," + item.get("fname") +"\t" + x )
def printTest2GradesData(l):	
	for item in l:	
		x = "N/A" if (item.get("t2") == None) else item.get("t2")
		print(item.get("studentid") + "\t" + item.get("lname") + "," + item.get("fname") +"\t" + x )
def final_grade(net_sum_final,pt):
    c1 = int(pt)
    diff= math.ceil((int(100) - c1)/7)
    m1=net_sum_final
    f = "A+"
    if(m1 >= c1+(6*diff)+6 and m1 <= 100):
        f = "A+"
        return f
    elif(m1 >= c1+(5*diff)+5 and m1 <= c1+(6*diff)+5):
        f = "A"
        return f
    elif(m1 >= c1+(4*diff)+4 and m1 <= c1+(5*diff)+4):
        f = "A-"
        return f
    elif(m1 >= c1+(3*diff)+3 and m1 <=c1+(4*diff)+3):
        f = "B+"
        return f
    elif(m1 >= c1+(2*diff)+2 and m1 <= c1+(3*diff)+2):
        f = "B"
        return f
    elif(m1 >= c1+diff+1 and m1 <=c1+(2*diff)+1):
        f = "B-"
        return f
    elif(m1 >= c1 and m1 <= c1+diff):
        f = "C" 
        return f
    elif(m1 < c1):
        f = "F"
        return f
def standardreport(pt,l,keysInfo):
	points=int(pt)
	print("ID\tLN\tFN\tA1\tA2\tPR\tT1\tT2\tGR\tFL")
	for item in l:
		a1_marks = int(0) if (item.get("a1") == None) else int(item.get("a1"))
		a2_marks = int(0) if (item.get("a2") == None) else int(item.get("a2"))
		project_marks = int(0) if (item.get("project") == None) else int(item.get("project"))
		t1_marks = int(0) if (item.get("t1") == None) else int(item.get("t1"))
		t2_marks = int(0) if (item.get("t2") == None) else int(item.get("t2"))	
		a1 = a1_marks/keysInfo.get("a1_total")*a1_wt
		a2 = a2_marks/keysInfo.get("a2_total")*a2_wt
		pr = project_marks/keysInfo.get("project_total")*pr_wt
		t1 = t1_marks/keysInfo.get("t1_total")*t1_wt
		t2 = t2_marks/keysInfo.get("t2_total")*t2_wt
		net_sum = a1+a2+pr+t1+t2
		net_sum_final=math.ceil(net_sum)
		# print(math.ceil(net_sum))
		j=final_grade(net_sum_final,points)
		print(item.get("studentid") + "\t" + item.get("lname") + "\t" + item.get("fname") + "\t" + str(a1_marks) + "\t" + str(a2_marks) + "\t" + str(project_marks) + "\t" + str(t1_marks) + "\t" + str(t2_marks) + "\t" + str(net_sum_final) + "\t" + str(j))
def a1_avg(l,keysInfo):
	sum = 0
	for item in l:
		if(item.get("a1") != None):
			sum += float(item.get("a1"))
	avg = float(sum)/float(keysInfo.get("a1_length")-1)	
	print("A1 Average " + str(round(avg,2)) + "/" + str(keysInfo.get("a1_total")))
def a2_avg(l,keysInfo):
	sum = 0
	for item in l:
		if(item.get("a2") != None):
			sum += float(item.get("a2"))
	avg = float(sum)/float(keysInfo.get("a2_length")-1)	
	print("A2 Average " + str(round(avg,2)) + "/" + str(keysInfo.get("a2_total")))
def pr_avg(l,keysInfo):
	sum = 0
	for item in l:
		if(item.get("project") != None):
			sum += float(item.get("project"))
	avg = float(sum)/float(keysInfo.get("project_length")-1)	
	print("Project Average " + str(round(avg,2)) + "/" + str(keysInfo.get("project_total")))
def t1_avg(l,keysInfo):
	sum = 0
	for item in l:
		if(item.get("t1") != None):
			sum += float(item.get("t1"))
	avg = float(sum)/float(keysInfo.get("t1_length")-1)	
	print("Test1 Average " + str(round(avg,2)) + "/" + str(keysInfo.get("t1_total")))
def t2_avg(l,keysInfo):
	sum = 0
	for item in l:
		if(item.get("t2") != None):
			sum += float(item.get("t2"))
	avg = float(sum)/float(keysInfo.get("t2_length")-1)	
	print("Test2 Average " + str(round(avg,2)) + "/" + str(keysInfo.get("t2_total")))
def cal_comp_average(l,keysInfo):
	compo = input("Enter Component From Given Options : A1,A2,PR,T1,T2\n")
	if(compo == "a1" or compo == "A1"):
		a1_avg(l,keysInfo)
		menu_opt(l,keysInfo)
	elif(compo == "a2" or compo == "A2"):
		a2_avg(l,keysInfo)
		menu_opt(l,keysInfo)	
	elif(compo == "pr" or compo == "PR"):
		pr_avg(l,keysInfo)
		menu_opt(l,keysInfo)	
	elif(compo == "t1" or compo == "T1"):
		t1_avg(l,keysInfo)
		menu_opt(l,keysInfo)	
	elif(compo == "t2" or compo == "T2"):
		t2_avg(l,keysInfo)
		menu_opt(l,keysInfo)
	else:
		print("Error:Please Enter Label From Given Options")
		cal_comp_average(l,keysInfo)
def individual_component(l,keysInfo):
	menu_choice = input("Enter Component From Given Options : A1,A2,PR,T1,T2\n")
	if(menu_choice == "a1" or menu_choice == "A1"):
		print("A1 Grades (" + str(keysInfo.get("a1_total")) +")")
		printA1GradesData(l)
		menu_opt(l,keysInfo)
	elif(menu_choice == "a2" or menu_choice == "A2"):
		print("A2 Grades (" + str(keysInfo.get("a2_total")) +")")
		printA2GradesData(l)
		menu_opt(l,keysInfo)
	elif(menu_choice == "pr" or menu_choice == "PR"):
		print("Project Grades (" + str(keysInfo.get("project_total")) +")")
		printProjectGradesData(l)
		menu_opt(l,keysInfo)
	elif(menu_choice == "t1" or menu_choice == "T1"):
		print("Test1 Grades (" + str(keysInfo.get("t1_total")) +")")
		printTest1GradesData(l)
		menu_opt(l,keysInfo)
	elif(menu_choice == "t2" or menu_choice == "T2"):
		print("Test2 Grades (" + str(keysInfo.get("t2_total")) +")")
		printTest2GradesData(l)
		menu_opt(l,keysInfo)
	else:
		print("Error:Please Enter Label From Given Options")
		individual_component(l,keysInfo)


def printSortList(li):
	print("ID\tLN\tFN\tA1\tA2\tPR\tT1\tT2\tGR\tFL")
	for item in li:
		a1 = (int(item.get("a1"))/a1_total)*a1_wt
		a2 = (int(item.get("a2"))/a2_total)*a2_wt
		pr = (int(item.get("project"))/project_total)*pr_wt
		t1 = (int(item.get("t1"))/t1_total)*t1_wt
		t2 = (int(item.get("t2"))/t2_total)*t2_wt
		net_sum = a1+a2+pr+t1+t2
		net_sum_final=math.ceil(net_sum)
		# print(math.ceil(net_sum))
		j=final_grade(net_sum_final,50)
		print(item.get("studentid") + "\t" + item.get("lname") + "\t" + item.get("fname") + "\t" + item.get("a1") + "\t" + item.get("a2") + "\t" + item.get("project") + "\t" + item.get("t1") + "\t" + item.get("t2") + "\t" + str(net_sum_final) + "\t" + str(j))


def sortByGrade(lis,keysInfo):
	gradelist = []
	for item in lis:
		tempdict ={}
		a1_marks = int(0) if (item.get("a1") == None) else int(item.get("a1"))
		a2_marks = int(0) if (item.get("a2") == None) else int(item.get("a2"))
		project_marks = int(0) if (item.get("project") == None) else int(item.get("project"))
		t1_marks = int(0) if (item.get("t1") == None) else int(item.get("t1"))
		t2_marks = int(0) if (item.get("t2") == None) else int(item.get("t2"))	
		a1 = a1_marks/keysInfo.get("a1_total")*a1_wt
		a2 = a2_marks/keysInfo.get("a2_total")*a2_wt
		pr = project_marks/keysInfo.get("project_total")*pr_wt
		t1 = t1_marks/keysInfo.get("t1_total")*t1_wt
		t2 = t2_marks/keysInfo.get("t2_total")*t2_wt
		net_sum = a1+a2+pr+t1+t2
		net_sum_final=math.ceil(net_sum)
		# print(math.ceil(net_sum))
		j=final_grade(net_sum_final,50)
		tempdict["grade"] = net_sum_final
		tempdict["grade_letter"] = j
		tempdict["studentid"] = item.get("studentid")
		gradelist.append(tempdict)	
	# sorted_list = sorted(lis, key = lambda i: i['grade'])
	# print(gradelist)
	result = merge_lists_for_two(lis,gradelist,'studentid')
	sorted_list = sorted(result, key = lambda i: i['grade'])
	standardreport(50,sorted_list,keysInfo)

def sortByLt(lis,keysInfo):
	sorted_list = sorted(lis, key = lambda i: i['lname'])
	standardreport(50,sorted_list,keysInfo)

def perform_operation(choice,l,keysInfo):
	while(choice > 0 and choice < 7):
		if(choice == 1):
			individual_component(l,keysInfo)
			menu_opt(l,keysInfo)
		elif(choice == 2):
			cal_comp_average(l,keysInfo)
			menu_opt(l,keysInfo)
		elif(choice == 3):
			standardreport(int(50),l,keysInfo)
			menu_opt(l,keysInfo)
		elif(choice == 4):
			svalue = input("Enter sort order : LT(LAST NAME)/GR(NUMERIC GRADE)")
			if(svalue == "LT" or svalue == "lt"):
				sortByLt(l,keysInfo)	
				menu_opt(l,keysInfo)
			elif(svalue == "GR" or svalue == "gr"):
				sortByGrade(l,keysInfo)
				menu_opt(l,keysInfo)
			else:
				print("Error:Please Enter Label From Given Options")
				perform_operation(4,l,keysInfo)				
		elif(choice == 5):
			point = int(input("Enter pass/fail points : "))
			standardreport(point,l,keysInfo)
			menu_opt(l,keysInfo)	
		elif(choice == 6):
			print("Good Bye")
			exit()	

def menu_opt(l,keysInfo):
	print("-------------------------------------")
	print("1> Display Individual Component")
	print("2> Display Component Avergae")
	print("3> Display Standard Report")
	print("4> Sort by alternate column")
	print("5> Change Pass/Fail Point")
	print("6> Exit")
	print("-------------------------------------")
	choice = int(input("Select Option\n"))
	perform_operation(choice,l,keysInfo)
