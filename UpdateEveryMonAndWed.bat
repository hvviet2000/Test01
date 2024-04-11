REM This scrip Run check update and restart 
REM ======================================
REM Vietis
REM Run scrip on every Monday and Wedsnesday

@echo off
setlocal enableextensions disabledelayedexpansion

set hour=%time:~0,2%
set min=%time:~3,2%
set day=%date:~0,3%

ECHO %day%
ECHO %hour%
ECHO %min%


 if "%day%" == "Wed" (
REM 	if %hour% == 14 (
REM		if %min% == 39 (
		
 		ECHO Starting run %day% 
		net start bits
		net start wuauserv
		wuauclt /detectnow /updatenow 
		shutdown /s /t 0
 	) else (
			ECHO Do Nothing
			
		)
REM	)
REM )



 if "%day%" == "Mon" (
REM 	if %hour% == 15 (
 		ECHO Starting run ssss %day% 
		net start bits
		net start wuauserv
		wuauclt /detectnow /updatenow && shutdown /s /t 0
 	) else (
			ECHO Do Nothing

	)
REM )

https://www.idkrtm.com/windows-update-commands/
https://social.technet.microsoft.com/wiki/contents/articles/53831.enable-disable-proxy-settings-via-powershell.aspx
$PSSessionOption = New-PSSessionOption -ProxyAccessType IEConfig -ProxyAuthentication Negotiate -ProxyCredential Domain01\User01
$proxyString = "http://" + $context.proxy.host + ":" + $context.proxy.port
$Env:HTTP_PROXY = $proxyString
$Env:HTTPS_PROXY = $proxyString

rem IF %hour% == 14 GOTO Test2
rem IF %min% == 58 GOTO YUP
rem IF %min% == 59 GOTO LATE






