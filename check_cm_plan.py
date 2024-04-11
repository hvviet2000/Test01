##=====================================================================
##
##  Script Name: check_cm_plan.py
##  Description: Check repository (gitlab) with cm plan
##
##  Copyright (C) 2022 VietIS, All Rights Reserved.
##       Author: Viet.hoang
##     Revision: 1.0
##      Created: 2022.9.2
##     Modified:
##
##  Exit Status: 1 Abnormal (Error)
##
##=====================================================================
# input: csv file with column name test.csv: Project,Member,Role,Expire Date
#        example : Axio.KeySpider,hoangdv,30,2022-12-31
# input: list.txt file with list of project
#        example: Axio.KeySpider
#                 MyPageApp
# Output: CSV file
#
# require pip install --upgrade python-gitlab
#
import gitlab.v4.objects
import csv
import datetime



# private token or personal token authentication (self-hosted GitLab instance)
#gl4 = gitlab.Gitlab(url='https://repo.vietis.com.vn:8009', private_token='glpat-yoEBMM5V5GyW2vMY4zRQ')
gl4 = gitlab.Gitlab(url='https://repo.vietis.com.vn:8009', private_token='glpat-9HDazm-3z4eEsWhc4yvV')

projects = gl4.projects.list(get_all=True)

#read csv
with open(r'C:\Python\csv\test.csv') as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    next(reader, None)  # skip the headers
    csvdata = [row for row in reader]
    #csvdata = [row for row in reader].sort(key=lambda x: x[0])
#csvdata = data_read

now = datetime.datetime.now()
f = open('C:\Python\csv\check_repo.csv', 'w')
f.write(str(now.date()) + '\n')

#read file text

with open('C:\Python\list.txt') as file:
    i = 1
    for line in sorted(file):
#   for line in file:
        duan = line.strip()
        print(duan)
        i += 1

#duan = "Axio.KeySpider"
#duan = "MyPageApp"


        list1 = []
        dict1 = dict()

        for i in range(0, len(csvdata)):
            temp = csvdata[i]
            prj_name = (temp[0])
            #if (prj_name == duan):
            if (prj_name.upper() == duan.upper()):
                uname = (temp[1]).upper()
                role = (temp[2])
                exp_date = (temp[3])
                dict1 ={'ten':uname, 'quyen':int(role), 'han':exp_date}
                list1.append(dict1)
#print(dict1)
#print(type(list1))
#       print(sorted(list1, key=lambda x: x['ten']))
        list11 = sorted(list1, key=lambda x: x['ten'])

        list2 = []
        dict2 = dict()
        for p in projects:
            p_name = p.name.upper()
            #print(p_name)
            if (p_name == duan.upper()):
                for member in p.members.list():
                    ten = (member.username).upper()
                    quyen = member.access_level
                    han_sd = member.expires_at
                    dict2 = {'ten':ten, 'quyen':quyen, 'han':han_sd}
                    list2.append(dict2)



        print(list2)
        list22 = sorted(list2, key=lambda x: x['ten'])
        print(list22)

        if (list11 == list22) and (len(list11) > 0) and (len(list22)>0):
            print ("Repo dung voi CM Plan")
            #f.write(str(list11))
            f.write("==============================" + '\n')
            f.write("Repo dung voi CM Plan:" + '\n')
            f.write(duan + '\n')
            f.write("==============================" + '\n')
            f.write("" + '\n')
        else:
             if (len(list11) == 0) or (len(list22) == 0):
                f.write("==============================" + '\n')
                f.write(duan + '\n')
                f.write("Du an khong co trong Repo hoac da dong:" + '\n')
                print ("=========== Repo khong dung vơi CM Plan")
                f.write("" + '\n')
             else:
                print ("=========== Repo khong dung vơi CM Plan")
                f.write("==============================" + '\n')
                f.write("Du an can check lai CM Plan:" + '\n')
                f.write(duan + '\n')
                f.write("danh sach tu file CM" + '\n')
                f.write(str(list11) + '\n')
                #f.write("" + '\n')
                f.write("danh sanh nay lay tu repo" + '\n')
                f.write(str(list22) +'\n')
                f.write("!!!!! Check trong csv !!!" + '\n')
                for sai in list11:
                    if sai not in list22:
                        print(sai)
                        f.write(str(sai) + '\n')
f.close()
