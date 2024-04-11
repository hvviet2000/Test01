https://toidicode.com/chuoi-trong-python-344.html
https://freetuts.net/class-trong-python-3482.html

#1.2 Biến, chuỗi

name = "Vũ Thanh Tài"
#string

age = 22
#integer

point = 8.9
#float

option = [1,2,3,4,5]
#lists

tuple = ('Vũ Thanh Tài', 22 , True)
#Tuple

dictionary = {"name": "Vu Thanh Tai", "age": 22, "male": True}
#Dictionary

point = 8.9
type(point)
#float

option = [1,2,3,4,5]
type(option)
#list

tuplet = ('Vũ Thanh Tài', 22 , True)
type(tuplet)
#Tuple

dictionary = {"name": "Vu Thanh Tai", "age": 22, "male": True}
type(dictionary)
# dict

========> khai báo
name, age, male = "Vũ Thanh Tài", 22 , True
a = b = c = 1996

=======> check kiểu
type(data)
name = "Vũ Thanh Tài"
type(name)
=======> chuyển đổi kiểu
age = 22;

# ép sang float
floatAge = float(age)
print(type(floatAge))

#ép sang integer.
intAge = int(age)
print(type(intAge))

#ép sang chuỗi.
strAge = str(age)
print(type(strAge))

===> Print

print("Toidicode.com", end = " - ")
print("Hoc lap trinh online")
=>>>Toidicode.com - Hoc lap trinh online

print("Website \"Toidicode.com\" ")
#Website "Toidicode.com"

print('Website \'Toidicode.com\' ')
#Website 'Toidicode.com'

\n ngắt xuống dòng và bắt đầu dòng mời.
\t đẩy nội dung phía sau nó cách 1 tab.
\a chuông cảnh báo.
\b xóa bỏ khoảng trắng phía trước nó.
=====================================

====>>>>định dạng cho kiểu giá trị và binding nó vào chuỗi. Sử dụng với cú pháp:
print("%type" %(binding))

%s 	chuỗi
%i 	số nguyên
%d 	số nguyên
%u 	số nguyên
%c 	character


guy = "Ban"
doamin = "toidicode.com"
full = "Chao mung %s den voi website %s" %(guy, doamin)
print(full)
# Chao mung Ban den voi website toidicode.com

#=========================================
#3 Truy cập tới từng giá trị của chuỗi.
#=========================================

stringName[index]
stringName[start:end]

name = "Vu Thanh Tai"
print(name[0:2]) # Vu
print(name[-3:12]) # Tai
12 = len(name)

print(name[9:]) # Tai
print(name[-3:]) # Tai

#=========================================
#4 Số.
#=========================================

age = 22
print(age) # 22

del age
print(age)
# name 'age' is not defined

+ 	a + b  // 15 	Phép cộng.
- 	a - b // -5 	Phép trừ.
* 	a * b // 50 	Phép nhân.
/ 	a / b // 0.5 	Phép chia.
% 	a % b // 5 	Phép chia lấy dư.


#=========================================
#4 Bài 6: List trong Python
#=========================================

name = ['VU Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0]) # Vu Thanh Tai
print(name[1]) # Nguyen Van A
print(name[2]) # Nguyen Thi E
# hoặc
print(name[-3]) # Vu Thanh Tai
print(name[-2]) # Nguyen Van A
print(name[-1]) # Nguyen Thi E

name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0:2])
# ['Vu Thanh Tai', 'Nguyen Van A']

# hoặc

print(name[-3:-1])
# ['Vu Thanh Tai', 'Nguyen Van A']

#===================================== update
name[1] = 1996
print(name)
# ['Vu Thanh Tai', 1996, 'Nguyen Thi E']

del name[2]
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A']


#====================================== lồng nhau

option = [12,5,1996]
myList = ['Vu Thanh Tai', option]
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]


for ngon_ngu in ['Python','Java','C']:
print("Tôi thích lập trình",ngon_ngu)
Tôi thích lập trình Python
Tôi thích lập trình Java
Tôi thích lập trình C

#=========================================
#5 Tuple Trong Python
#=========================================

#Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ các đối tượng không thay đổi về sau (giống như hằng số)

day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
day = 'monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday'
a = (); #tuple rỗng

a = (10,) #chú ý có dấu ,


day[0] # monday

day[-2] # saturday

tupleName[start:end]
day[:3] # ('monday', 'tuesday', 'wednesday')

#ghép:

day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday')

day = day1 + day2

print(day)

#lồng
day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday', day1)

#=========================================
#8 Dictionary
#=========================================

#dictionary trong Python là một kiểu dữ liệu lưu trữ các giá trị chứa key và value , nó giống với Json

person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'single'        
    }
	
# 
person['name'] # Vũ Thanh Tài
person['status'] # signle

#change value
person['status'] = 'married'
print(person)

dictName.clear();
person.clear()
del person
#Dictionary lồng nhau.
person = {
    'name': 'Vũ Thanh Tài',
    'option': {
                'age': 22,
                'male': True,
                'status': 'alone'
            }        
    }

print(person['option']['age'])
# 22


dict()
dic = dict()

#=========================================
#9 Các toán tử cơ bản trong Python
#=========================================
1, Toán tử số học - Arithmetic Operators.
2, Toán tử Quan hệ.
3, Toán tử gán.
4, Toán tử logic.
5, Toán tử biwter.
6, Toán Tử khai thác.
7, Toán tử xác thực.

/ 	Toán tử chia các giá trị cho nhau 	a / b = 0.7142857142857143
% 	Toán tử chia lấy phần dư  	a % b = 5
** 	Toán tử mũ. a**b = ab 	a ** b = 78125
// 	Toán tử chia làm tròn xuống.

VD:

0,57 => 0
0.9 => 0
-07 => -1
-0.1 => -1

== bằng
!= khác

#Toán tử gán.
= 	Toán tử này dùng để gán giá trị của một đối tượng cho một giá trị 	c = a (lúc này c sẽ có giá trị = 5)
+= 	Toán tử này cộng rồi gắn giá trị cho đối tượng 						c += a (tương đương với c = c + a)
-= 	Toán tử này trừ rồi gắn giá trị cho đối tượng 						c -= a (tương đương với c = c - a)
*= 	Toán tử này nhân rồi gắn giá trị cho đối tượng 						c *= a (tương đương với c = c * a)
/= 	Toán tử này chia rồi gắn giá trị cho đối tượng 						c /= a (tương đương với c = c / a)
% 	Toán tử này chia hết rồi gắn giá trị cho đối tượng 					c %= a (tương đương với c = c % a)
**= 	Toán tử này lũy thừa rồi gắn giá trị cho đối tượng 				c **= a (tương đương với c = c ** a)
//= 	Toán tử này chia làm tròn rồi gắn giá trị cho đối tượng 		c //= a (tương đương với c = c // a)

#Toán tử biwter. Toán tử này thực hiện trên các bit của các giá trị
2 biến a = 12 
b = 15 nhưng nếu chúng ta convert chúng sang hệ nhị phân thì 2 biến này sẽ có giá trị như sau: 
a = 00001100 và 
b = 00001111. 

(a & b) = 12 (00001100)
(a | b) = 14 (00001111)
a ^ b) = 2 (00000010) 
(-a) = -13 (00001101)
a>>a = 0
a<<a = 49152

#Toán Tử khai thác.

a = 4
b = [1,5,7,6,9]	

a in b //False
a not in b //True

a is b //False
a is not b //True

#==============================================
#Các câu lệnh rẽ nhánh
#++++++++++++++++++++++++++++++++++++++++++++++

if condition:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    #code
	
a = 7
if (a >= 0 and a <= 10):
    if (a >= 4):
        print('Qua mon')
    else:
        print('Hoc lai')
else:
    print('Diem khong hop le')
	
	
#Lặp
for variable in data:
for i in range(0,10):
    for j in range(i,10):
        print(j, end = " ")
    print ("")
	
	
#
i = 1;
while(i <= 10):
    print(i)
    i += 1


#=================================
#Bài 12: Hàm trong Python
#=================================
def ten_ham(param...): #có dấu :

def say():
    print("Welcome to toidicode.com")

def sum(a, b):
    print("sum = " + str(a + b))
	
	
#gọi hàm
say()
sum(3, 7)
#

def sum(a, b):
   return a+ b
   
# ví dụ
c = sum(4, 5);
print("Tong cua 4 va 5 = " + str(c))

#thay đổi giá trị

a = [5, 10, 15]
def change(a):
    a[0] = 1000
    print(a)

change(a)
# KQ: [1000, 10, 15]
print(a)
# KQ: [1000, 10, 15]

#======================Biến global

global tenbien
a = "Hello Guy!"
def say():
    global a
    a = "Toidicode.com"
    print(a)

#nó cho KQ là biến Global

#=========================================================
#khai báo một param đại diện cho các biến truyền vào hàm bằng cách thêm dấu * vào trước param đó.

def get_sum(*num):
    tmp = 0
    # duyet cac tham so
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)

print(result)
# KQ: 15

#==============================================
#Bài 13: Input và Đọc ghi file trong Python
#==============================================
print("Hello guy!")
age = input("How old are you? ")
print("age: " + age)

open(filePath, mode, buffer)
r 	Chế độ chỉ được phép đọc.
rb 	Chế độ chỉ được phép đọc nhưng cho định dạn nhị phân.
r+ 	Chế độ này cho phép đọc và ghi file, con trỏ nó sẽ nằm ở đầu file.
w 	Chế độ ghi file, nếu như file không tồn tại thì nó sẽ tạo mới file và ghi nội dung, còn nếu như file đã tồn tại nó sẽ ghi đè nội dung lên file cũ.
w+ 	Mở file trong chế độ đọc và ghi. còn lại như w.
a 	Mở file trong chế độ ghi tiếp. Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung, và nếu như file chưa tồn tại thì nó sẽ tạo một file mới và ghi nội dung vào đó.

fileObject.close()

# mo file
file = open('readme.md')
# doc file
data = file.read();
# dong file
file.close()
# in du lieu doc duoc
print(data)

#===================
# mo file o che do ghi
file = open('readme.md','w')
# ghi file
file.write('Vu Thanh Tai - toidicode.com')
# dong file
file.close()
#================================
#==============================================
# Bai 14 Modules trong Python.
#==============================================
import module1, module2,...

#content
mathplus.py
# file math.py
def get_sum (a, b):
    return a + b
	
	
import mathplus

print(mathplus.get_sum(4,7))
# Kết quả: 11

#===========định danh mới
import modules as newname
# hoặc đối với from import
from modules import something as newname

import mathplus as ma

print(ma.get_sum(4,7))
# Kết quả: 11

from mathplus import get_sum as sum

print(sum(4,7))
# Kết quả: 11
#=============================================#
import os, sys
# lấy ra đường dẫn đến thư mục modules ở trong projetc hiện hành
lib_path = os.path.abspath(os.path.join('modules'))
# thêm thư mục cần load vào trong hệ thống
sys.path.append(lib_path)
# import
from mathplus import get_sum

print(get_sum(1,4));
# kết quả: 5

#=========================================
#Bài 15: Packages trong Python
#========================================

#Package trong Python là một thư mục chứa một hoặc nhiều modules hay các package khác 
#ví dụ một package views thì nó sẽ chứa các modules liên quan đến views.
# cần tạo ra một thư mục, với tên thư mục chính là tên của package 
# trong thư mục này nhất định phải có một file có tên __init__.py. 
#File __init__.py này nó giống như các constructor, và nó sẽ được gọi ra đầu tiên khi chúng ta import package đó.

demopackage/__init__py
main.py

# __init__.py
print("Duoc in tu file __init__py")

# main.py
import demopackage

Python main.py
#Duoc in tu file __init__py

|--demopackage/
|             |--modules.py
|             └── __init__py
|--main.py

#Và ở trong file modules.py các bạn tạo cho mình 2 hàm như sau:
def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

#============================================	
# main.py
from demopackage.modules import *
# Duoc in tu file __init__py

say_hello()
# Hello!

say_goodbye()
# Goodbye!
#================================Package chứa Package

|--demopackage/
|             |--modules.py
|             |--packagechild/
|                            |-- childmodule.py
|                            └── __init__py
|             └── __init__py
|--main.py


# packagechild/childmodule.py
def say():
    print("childmodule.py: Hello")
	
	
# packagechild/__init__.py
print("childpackage __init__.py")

# main.py
from demopackage.packagechild.childmodule import *
# childpackage __init__.py

say()
# childmodule.py: Hello

#==================================
#Bài 16: Exception Try catch
#==================================

try:
    # code
except exceptionName:
    # code


try :
    # code
except (ZeroDivisionError, RuntimeError):
    # code


try :
    # code
except ZeroDivisionError:
    # code
except RuntimeError:
    # code


#=====================	hàm 
def sum(a, b):
    return a / b

try :
    print(sum(6, 0))
except ZeroDivisionError:
    print('Co loi xay ra!')

#ket qua: Co loi xay ra!
#======================
def sum(a, b):
    return a / b

try:
    print(sum(6, 0))
except ZeroDivisionError:
    print('Co loi xay ra!')
finally:
    print('finally duoc goi!')

# Ket qua:
# Co loi xay ra!
# finally duoc goi!
#https://toidicode.com/exception-trong-python-356.html

#SystemError 	Xuất hiện khi trình biên dịch có vấn đề nhưng mà nó lại không tự động exit.
#SystemExit 	Xuất hiện khi trình biên dịch được thoát bởi sys.exit().
#RuntimeError 	Xuất hiện khi lỗi được sinh ra không thuộc một danh mục nào.

#4, Xây dựng một exception riêng.

class ExceptionDemo(Exception):
    def __init__(self, value):
        print("Loi: " + value)
		

#
def sum(a, b):
    if (b == 0):
        raise ExceptionDemo('b phai khac 0')
    return a / b
sum(6, 0)

#==================================================
#Bài 20: Hàm ẩn danh Lambda trong Python
#=================================================

#- Lambda là một anonymous function (hàm ẩn danh) nó có thể khai báo, định nghĩa ở bất kỳ đâu và không có khả năng tái sử dụng.
#- Lambda chỉ tồn tại trong phạm vi của biến mà nó được định nghĩa, vì vậy nếu như biến đó vượt ra ngoài phạm vi thì hàm này cũng không còn tác dụng nữa.
#- Lambda thường được dùng để gán vào biến, hay được gán vào hàm, class như một tham số.

lambda arguments_list: expression
#
#    lambda là keyword bắt buộc.
#    arguments_list là các tham số truyền vào lambda.
#    expression là các biểu thức xử lý lambda.

add = lambda a, b: a + b
# call lambda
add(3, 4) # 7

type(add) # function

#===================
#https://freetuts.net/class-trong-python-3482.html
#https://python-gitlab.readthedocs.io/en/stable/gl_objects/projects.html
#https://devenum.com/how-to-write-list-of-dictionaries-to-csv-in-python/
#https://python-gitlab.readthedocs.io/en/stable/gl_objects/projects.html
#https://stackoverflow.com/questions/71734261/python-gitlab-api-find-creator-of-a-project
#===================
#https://docs.gitlab.com/ee/api/protected_branches.html

#https://note.nkmk.me/en/python-dict-list-sort/

#=======Read file====
with open('abc.txt') as file:
    i = 1
    for line in file:
        result = str(i) + ' - ' + line
        print result
        i += 1
		
		

file1 = open('list.txt', 'r')
count = 0

while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))

file1.close()
		
#====================


# run from terminal 
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#pip install --upgrade python-gitlab
access_level
Guest (10)
Reporter (20)
Developer (30)
Maintainer (40)
Owner (50).


#====================
https://developers.google.com/workspace/guides/create-credentials

example01viet

To create an API key:

    Open the Google Cloud console. https://accounts.google.com https://console.cloud.google.com/
    At the top-left, click Menu menu > APIs & Services > Credentials.
    Click Create credentials > API key.
    Your new API key is displayed.
        Click Copy content_copy to copy your API key for use in your app's code. The API key can also be found in the "API keys" section of your project's credentials.
        Click Restrict key to update advanced settings and limit use of your API key. For more details, see Applying API key restrictions.

Step 1: Create a project
example01viet

Step 2: Menu menu > APIs & Services > Credentials.
Create credentials > API key.

Step 3: create API key: pj01it
AIzaSyB4PVMtZGWotu6FrDSMYrnO-5lDqCAfpm0

https://cloud.google.com/docs/authentication/api-keys
https://thigiacmaytinh.com/upload-file-len-google-drive-bang-python/


itapp01

itapp01OAu2.0


https://devqa.io/python-compare-two-lists-of-dictionaries/


    Lists, tuples and dictionary
    Date and time
    Functions
    Files I/O
    Exception

– For system administrator

    RESTful API
    Databases
    Logging and troubleshooting
	
	 For networking

    SSH in Python
    Scapy – Networking packet manipulation
	
	

https://blog.opstree.com/2022/04/26/google-python-api-the-easy-way/
https://lucidgen.com/cach-tao-service-account-va-bat-api-google-cloud/
https://www.youtube.com/watch?v=PKLG5pfs4nY&ab_channel=JieJenn
https://developers.google.com/identity/protocols/oauth2


    OAuth 2.0 Client IDs
    Service Accounts
	Enable APIs
	Library install: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
	
Authentication
Create credential object

from googleapiclient.discovery import build
from google.oauth2 import service_account
SCOPE=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
CREDENTIAL='credentials.json'creds = service_account.Credentials.from_service_account_file(CREDENTIAL,scopes=SCOPE)

client ID
674160338005-aav3o6tnq1k5u7ktj1g0fqk259uohm4m.apps.googleusercontent.com
Client secret
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
notasecret
7931dc68f36a182248c98e442325598fea9ae4e2

Email

itapp01@pj01it.iam.gserviceaccount.com

Unique ID

104380885974630262894

{
  "role": "roles/owner",
  "members": [
    "serviceAccount:itapp01@pj01it.iam.gserviceaccount.com",
    "serviceAccount:test-233@pj01it.iam.gserviceaccount.com",
    "user:viet.hoang@vietis.com.vn"
  ]
}
