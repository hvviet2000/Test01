https://docs.microsoft.com/en-us/answers/questions/253555/software-list-inventory-wmic-product.html
https://silentinstallhq.com/7-zip-silent-uninstall-powershell/



$myComputers = Get-Content
"c:\scripts\mycomputers.txt"

foreach ($computer in $myComputers) {

 Uninstall-HotFix -ComputerName $computer -HotfixID KB5013624

}


KB5013624
KB5013624

function Uninstall-Hotfix {
[cmdletbinding()]
param(
$computername = $env:computername,
[string] $HotfixID
)            

$hotfixes = Get-WmiObject -ComputerName $computername -Class Win32_QuickFixEngineering | select hotfixid            

if($hotfixes -match $hotfixID) {
    $hotfixID = $HotfixID.Replace("KB","")
    Write-host "Found the hotfix KB" + $HotfixID
    Write-Host "Uninstalling the hotfix"
    $UninstallString = "cmd.exe /c wusa.exe /uninstall /KB:$hotfixID /quiet /norestart"
    ([WMICLASS]"\\$computername\ROOT\CIMV2:win32_process").Create($UninstallString) | out-null            

    while (@(Get-Process wusa -computername $computername -ErrorAction SilentlyContinue).Count -ne 0) {
        Start-Sleep 3
        Write-Host "Waiting for update removal to finish ..."
    }
write-host "Completed the uninstallation of $hotfixID"
}
else {            

write-host "Given hotfix($hotfixID) not found"
return
}            

}

hotfixID
Start-Process -FilePath "wusa.exe" -Argumentlist "/Uninstall /KB:5013624 /quiet /norestart" 

https://o365reports.com/2022/06/15/top-50-powershell-scripts-for-microsoft-365-admins/


windows
- SQL
- Portgree 
- CSV
chèn data từ csv -> Portgree 

https://www.anycodings.com/1questions/1949935/retrieve-data-from-postgresql-using-powershell

https://www.cdata.com/kb/tech/postgresql-ado-powershell.rst

function Get-ODBC-Data{
   param([string]$query=$(throw 'query is required.'))
   $conn = New-Object System.Data.Odbc.OdbcConnection
   $conn.ConnectionString = "Driver={PostgreSQL Unicode(x64)};Server=SOMENAME;Port=5432;Database=DBNAME;Uid=SOMEUSER;Pwd=SOMEPASS;"
   $conn.open()
   $cmd = New-object System.Data.Odbc.OdbcCommand($query,$conn)
   $ds = New-Object system.Data.DataSet
   (New-Object system.Data.odbc.odbcDataAdapter($cmd)).fill($ds) | out-null
   $conn.close()
   $ds.Tables[0]
}

function Set-ODBC-Data{
   param([string]$query=$(throw 'query is required.'))
  $conn = New-Object System.Data.Odbc.OdbcConnection
  $conn.ConnectionString= "Driver={PostgreSQL Unicode(x64)};Server=SOMENAME;Port=5432;Database=DBNAME;Uid=SOMEUSER;Pwd=SOMEPASS;"
  $cmd = new-object System.Data.Odbc.OdbcCommand($query,$conn)
  $conn.open()
  $cmd.ExecuteNonQuery()
  $conn.close()
}
$query = "select * from clients"
$result = Get-ODBC-Data -query $query
$query = "INSERT INTO clients (id) VALUES (3)"
set-odbc-data -query $query



https://www.enterprisedb.com/postgres-tutorials/postgresql-query-introduction-explanation-and-50-examples

PostgreSQL 14


Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]: vietis
Password for user vietis:
psql (14.5)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

show database;
postgres=# \l
connect to database

postgres=# \c vietisdatabase
show table;
postgres=# \dt

create table dummy_table(name varchar(20),address text,age int);

insert into dummy_table values('XYZ','location-A',25);
insert into dummy_table values('ABC','location-B',35);
insert into dummy_table values('DEF','location-C',40);
insert into dummy_table values('PQR','location-D',54);

select * from dummy_table;


ALTER TABLE dummy_table ADD COLUMN ngaysinh TIMESTAMP;


UPDATE dummy_table SET ngaysinh = '2020-08-01' WHERE age <= 53;
UPDATE dummy_table SET ngaysinh = '2025-08-01' WHERE age > 53;

UPDATE COMPANY SET SALARY = 15000 WHERE ID = 3

$insertDml3 = "INSERT INTO $MyTable VALUES ('AAA','location-A',57,'2030-12-01:14:25:35')"

#$insertDml3 = "INSERT INTO Message(rawMessage, loadedTime) VALUES ('$strLine',to_timestamp('$loadDate','DD-Mon-YYYY HH24:MI:SS'))"

ALTER TABLE dummy_table ALTER COLUMN name TYPE varchar(50);

timestamp: a timestamp without timezone one.
timestamptz: timestamp with a timezone.

INSERT into "Group" (name,createddate) 
VALUES ('Test', current_timestamp);




https://www.anycodings.com/1questions/1949935/retrieve-data-from-postgresql-using-powershell


$formatProvider = [System.Globalization.CultureInfo]::GetCulture('en-US')
[DateTime]::ParseExact($timeinfo, $template, $formatProvider)

[datetime]$timeinfo

$culture = [Globalization.CultureInfo]::InvariantCulture
[DateTime]::ParseExact('02-06-2018 16:25:28', 'MM-dd-yyyy HH:mm:ss', $culture)

$ngaysinh = "02-06-2018 16:25:28" 
$date1 = [DateTime]::ParseExact($ngaysinh,'MM-dd-yyyy HH:mm:ss', $culture)

