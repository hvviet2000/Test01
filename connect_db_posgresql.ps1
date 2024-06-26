clear
$MyServer = "localhost"
$MyPort  = "5432"
$MyDB = "vietisdatabase"
$MyUid = "vietis"
$MyPass = "vietis@123"
$MyTable = "dummy_table"

#method 1
#$DBConnectionString = "Driver={PostgreSQL UNICODE(x64)};Server=$MyServer;Port=$MyPort;Database=$MyDB;Uid=$MyUid;Pwd=$MyPass;"
#$DBConn = New-Object System.Data.Odbc.OdbcConnection;
#$DBConn.ConnectionString = $DBConnectionString;
#$DBConn.Open();
#$DBCmd = $DBConn.CreateCommand();
#$DBCmd.CommandText = "SELECT * FROM dummy_table;";
#$DBCmd.ExecuteReader();
#$DBConn.Close();

#Method 2

$cnString = "Driver={PostgreSQL UNICODE(x64)};Server=$MyServer;Port=$MyPort;Database=$MyDB;Uid=$MyUid;Pwd=$MyPass;"

$conn = New-Object -comobject ADODB.Connection
$conn.Open($cnString,$MyUid,$MyPass)


#Insert Data 
#$insertDml3 = "INSERT INTO Message(rawMessage, loadedTime) VALUES ('$strLine',to_timestamp('$loadDate','DD-Mon-YYYY HH24:MI:SS'))"

$insertDml3 = "INSERT INTO $MyTable VALUES ('AAA','location-A',57)"
$DBCmd = $DBConn.CreateCommand();
$DBCmd.CommandText = $insertDml3;
$DBCmd.ExecuteReader();



$recordset = $conn.Execute("SELECT * FROM $MyTable;")


while ($recordset.EOF -ne $True) 
{  
    foreach ($field in $recordset.Fields)
    {    
        '{0,30} = {1,-30}' -f # this line sets up a nice pretty field format, but you don't really need it
        $field.name, $field.value  
    }
   ''  # this line adds a line between records
$recordset.MoveNext()
}







$conn.Close()



