project1 = ("arun","sam","vishwa","hari")
project2 = ("vasan","saran","hari","arun")
project3 = ("arun","venkat","vishwa","suresh")
project =["project 1 : project1","project 2: project2","project 3 : project3"]

print("employee in each project:")
for project, employee in project.items():
    print("project,",employees)
    all_employee = set()

    for employee in project.values():
        all_employee = all_employee.union(employee)
        print("employees working in more than one project")

    for employees in all_employee:
        count = 0
        for employees in project.values():
            if employee in employees:
                count = 1

        if count > 1:
            print ("employee,->", count,"project")
            