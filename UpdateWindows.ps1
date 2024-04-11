####################################################################################################################
# Script: Windows Update via Powershell
# Auteur: Rick Stomps
# Versie: 1.0
# Function Check-PendingReboot: https://stackoverflow.com/questions/47867949/how-can-i-check-for-a-pending-reboot
####################################################################################################################

# Function to check pending reboot.
function Check-PendingReboot {
    if (Get-ChildItem "HKLM:\Software\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending" -EA Ignore) { return $true }
    if (Get-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired" -EA Ignore) { return $true }
    if (Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager" -Name PendingFileRenameOperations -EA Ignore) { return $true }
    try { 
        $util = [wmiclass]"\\.\root\ccm\clientsdk:CCM_ClientUtilities"
        $status = $util.DetermineIfRebootPending()
        if (($status -ne $null) -and $status.RebootPending) {
            return $true
        }
    }
    catch { }

    return $false
}

# Change Execution Policy for this process to run the script.
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force

# Install the required packages.
Install-PackageProvider -Name NuGet -Force
Install-Module -Name PSWindowsUpdate -Force

# Import the required module.
Import-Module PSWindowsUpdate

# Look for all updates, download, install and don't reboot yet.
Get-WindowsUpdate -AcceptAll -Download -Install -IgnoreReboot

# Check if a pending reboot is found, notify users if that is the case. If none found just close the session.
$reboot = Check-PendingReboot

if($reboot -eq $true){
   write-host("Pending reboot found. Reboot..")
   cmd /c "msg * "Windows update has finished downloading and needs to reboot to install the required updates. Rebooting in 5 minutes..""
   cmd /c "Shutdown /r /f /t 300"
   Exit
   
}else {
   write-host("No Pending reboot. Shutting down PowerShell..")
   Exit
}



$comps = get-content c:\folder\computers.txt

foreach ($comp in $comps){

new-pssession -computername $comp

invoke-command (get-pssession) -scriptblock{

#insert your script here! Untested, please try.



# Install required modules
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
Install-Module pswindowsupdate -force
Import-Module PSWindowsUpdate -force
# End installing required modules
# Enable ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
# SMTP Email Configuration Settings
$from = "asm.alerts@asm-inc.com"
$to = "you@email.com", "you2@email.com"
$smtp = "your smtp servername"
$sub = "$($env:COMPUTERNAME): Windows Updates Installed and Rebooted"
$sub1 = "$($env:COMPUTERNAME): No Updates Needed"
$body = "Server Windows Update Report"
$body1 = "No new updates found."
# This is needed if the smtp server requires authentication
$secpasswd = ConvertTo-SecureString "smtp password here" -asplaintext -force
# Define the email attachment report
$attachement = "c:\$(get-date -f yyyy-MM-dd)-WindowsUpdate.log"
$mycreds = New-Object System.Management.Automation.PSCredential ("smtp username", $secpasswd)
# Start WSUS updates
$updates = Get-wulist -verbose
$updatenumber = ($updates.kb).count
if ($updates -ne $null) {
Install-WindowsUpdate -AcceptAll -Install -AutoReboot | Out-File "c:\$(get-date -f yyyy-MM-dd)-WindowsUpdate.log" -force
# Now let's send the email report
Send-MailMessage -To $to -From $from -Subject $sub -Body $body -Attachments $attachement -Credential $mycreds -SmtpServer $smtp -DeliveryNotificationOption Never -BodyAsHtml -UseSsl
}
else
{ 
Send-MailMessage -To $to -From $from -Subject $sub1 -Body $body1 -Credential $mycreds -SmtpServer $smtp -DeliveryNotificationOption Never -BodyAsHtml -UseSsl 
}
# Enable ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy Restricted
}
}