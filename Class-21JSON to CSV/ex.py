import csv  
fp = open('emp.csv','w',newline="")
csvwriter=csv.writer(fp);
emp_list=[[1,'rahual','Male'],[2,'soniya','Female']]
csvwriter.writerow(['eid','ename','gender'])
csvwriter.writerows(emp_list)
fp.close()