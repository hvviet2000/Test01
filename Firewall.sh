https://www.youtube.com/watch?v=fbd6ci86SRg&ab_channel=ITTraningTutorial
https://www.youtube.com/watch?v=nXIBDQqekPY&ab_channel=CiscoCommunity
https://www.cisco.com/c/en/us/products/collateral/security/firepower-2100-series/datasheet-c78-742473.html

Cisco asa
CISCO FPR2110-ASA-K9 FIREPOWER FIREWALL SECURITY APPLIANCE 

FG-200E-BDL-950-12	Hardware plus 24x7 FortiCare and FortiGuard Unified Threat Protection (UTP) - 1 Year	  86,652,800 VND chưa V
CISCO FPR2110-ASA-K9 FIREPOWER FIREWALL SECURITY APPLIANCE 

chạy hệ điều hành fire power service

CISCO FPR2110-ASA-K9 FIREPOWER FIREWALL SECURITY APPLIANCE 
giá tầm 46tr chưa VAT bảo hành 12 tháng


https://www.cisco.com/c/en/us/products/collateral/security/firepower-2100-series/datasheet-c78-742473.html



4331/k9 rồi đó đã có license perfomance lên 300Mbps

show ip route
--> show default route

https://www.youtube.com/watch?v=p73pnRNxcn8&ab_channel=TANKirivann
https://www.youtube.com/watch?v=-ZHXfy-ElgM&ab_channel=NetworkingHub


enable secret password
username user secret password
no username user

enable secret password
username user secret password
no username user

https://www.youtube.com/watch?v=wMlYrpz96Y4&ab_channel=VnPro

https://www.sysnettechsolutions.com/en/configure-ssh-gns3/

https://www.youtube.com/watch?v=0ltI4uN5_3Q&ab_channel=BitsPlease

https://www.cisco.com/c/en/us/td/docs/security/firepower/quick_start/fp2100/firepower-2100-gsg/asa-platform.html


Cách 3: Factory Reset Cisco Firepower trong ROMMON
Trong trường hợp quên mật khẩu truy cập vào thiết bị, bạn cần truy cập ROMMON để xóa cấu hình.

Kết nối dây console vào thiết bị Cisco Firepower.
Tắt nguồn thiết bị và bật lại.
Khi hệ thống đang khởi động, bạn phải vào chế độ ROMMON, để thực hiện việc đó, nhấn ESC hoặc CTRL + L để ngắt quá trình khởi động.
******************************************
Cisco System ROMMON, Version 1.0.06, RELEASE SOFTWARE
Copyright (c) 1994-2017 by Cisco Systems, Inc.
Compiled Wed 11/01/2017 18:38:59.66 by builder
********************************************

Current image running: Boot ROM1
Last reset cause: PowerCycleRequest
DIMM_1/1 : Present
DIMM_2/1 : Absent

Platform FPR-2110 with 16384 MBytes of main memory
BIOS has been successfully locked !!
MAC Address: 70:7d:b9:e2:84:ec

Use BREAK or ESC to interrupt boot.
Use SPACE to begin boot immediately.

Located '.boot_string' @ cluster 516881.

rommon 1 >
Sau khi truy cập ROMMON, sử dụng lệnh password_reset để xóa cấu hình trên thiết bị. Một số phiên bản ROMMON lệnh này được thay thế bằng lệnh factory_reset, các bạn có thể ? để check.

rommon 1 > password_reset
WARNING: User configurations will be lost with this operation
Are you sure ? yes/no [no]: yes
 
Enabling password reset..
Please continue to boot the image !
rommon 2 >boot
Hoặc sử dụng lệnh factory-reset

rommon 2 > factory-reset
WARNING: User configurations will be lost with this operation
Are you sure ? yes/no [no]: yes

Username là admin, password là Admin123. 
=====================================================
https://www.cisco.com/c/en/us/td/docs/security/asa/fxos/config/asa-2100-fxos-config/cli.html#id_69975
=====================================================
HTTPS
Step 1 	

Enter system and then services mode.

scope system

scope services
Example:


firepower-2110# scope system
firepower-2110 /system # scope services
Firepower-chassis /system/services # 

Step 2 	

To configure HTTPS access to the chassis, do one of the following:

    Allow HTTPS access to the chassis.

    enable https

========================================
Introduction to and Design of Cisco ASA with FirePOWER Services 

