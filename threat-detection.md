# opensource-threat-detection

A collection of open source threat detection tools

## Collections

3rd-party lists

* [MHaggis/hunt-detect-prevent - Lists of sources and utilities utilized to hunt, detect and prevent evildoers](https://github.com/MHaggis/hunt-detect-prevent)
* [0x4D31/awesome-threat-detection - A curated list of awesome threat detection and hunting resources](https://github.com/0x4D31/awesome-threat-detection)

Online scanners

* Virus scanner
  * [VirusTotal - Analyze suspicious files and URLs to detect types of malware, ](https://www.virustotal.com/#/home/upload)
  * [NoDistribute - Online Virus Scanner Without Result Distribution](https://nodistribute.com/)
  * [VirSCAN.org - 多引擎在线病毒扫描网](http://www.virscan.org/language/zh-cn/)
* Behavior analysis  
  * [any.run - Interactive malware hunting service](https://app.any.run/)
  * [hybrid-analysis - Free Automated Malware Analysis Service powered by Falcon Sandbox](https://www.hybrid-analysis.com/)
  * [Free Automated Malware Analysis Service - powered by Falcon Sandbox](https://www.reverse.it/)
* Packet analysis
  * [PacketTotal - A free, online PCAP analysis engine](https://www.packettotal.com/)
* APK
  * [Koodous](https://koodous.com/)  
* Office
  * [Office document malware analysis](https://quicksand.io/)
* Automation
  * [diogo-fernan/malsub - A Python RESTful API framework for online malware analysis and threat intelligence services](https://github.com/diogo-fernan/malsub)

Automated analysis

* [certsocietegenerale/fame - FAME Automates Malware Evaluation 有界面](https://github.com/certsocietegenerale/fame)
* [Rurik/Noriben - Noriben - Portable, Simple, Malware Analysis Sandbox](https://github.com/Rurik/Noriben)
* Macos
  * [mac-a-mal](https://github.com/phdphuc/mac-a-mal)
* Javascript
  * [CapacitorSet/box-js - A tool for studying JavaScript malware](https://github.com/CapacitorSet/box-js)
* VM enhancements
  * [nsmfoo/antivmdetection - Script to create templates to use with VirtualBox to make vm detection harder](https://github.com/nsmfoo/antivmdetection)
  * Useful posts
    * [Knowledge Fragment: Hardening Win7 x64 on VirtualBox for Malware Analysis](https://byte-atlas.blogspot.com/2017/02/hardening-vbox-win7x64.html)

Windows

* [kurtfalde/DNS-Debug - Script to enabled DNS Debug Logging across Domain Controllers in a Forest and then retrieve for analysis](https://github.com/kurtfalde/DNS-Debug)
* [AxtMueller/Windows-Kernel-Explorer - A free but powerful Windows kernel research tool](https://github.com/AxtMueller/Windows-Kernel-Explorer)
* Event Tracing for Windows (ETW)
  * [chentiangemalc/EtlToCap - Convert ETL to PCAP](https://github.com/chentiangemalc/EtlToCap)
  * [chentiangemalc/PowerShellScripts - ConvertEtl-ToPcap.ps1](https://github.com/chentiangemalc/PowerShellScripts/blob/master/ConvertEtl-ToPcap.ps1)
* Active directory
  * [vletoux/pingcastle - Get Active Directory Security at 80% in 20% of the time](https://github.com/vletoux/pingcastle)
  * [phillips321/adaudit - Powershell script to do domain auditing automation](https://github.com/phillips321/adaudit)
  * [shellster/DCSYNCMonitor - Monitors for DCSYNC and DCSHADOW attacks and create custom Windows Events for these events](https://github.com/shellster/DCSYNCMonitor)
* Windows Event forwarding  
  * [palantir/windows-event-forwarding - A repository for using windows event forwarding for incident detection and response](https://github.com/palantir/windows-event-forwarding)
  * [Windows Event Forwarding for Network Defense](https://medium.com/@palantir/windows-event-forwarding-for-network-defense-cb208d5ff86f)
  * [iadgov/Event-Forwarding-Guidance - Configuration guidance for implementing collection of security relevant Windows Event Log events by using Windows Event Forwarding. iadgov](https://github.com/iadgov/Event-Forwarding-Guidance)

Linux 

* Rootkit detection
  * [David-Reguera-Garcia-Dreg/lsrootkit - via GID bruteforcing](https://github.com/David-Reguera-Garcia-Dreg/lsrootkit)
  * [nbulischeck/tyton - Kernel-Mode Rootkit Hunter](https://github.com/nbulischeck/tyton)

Mac

* [objective-see/ReiKey - Malware and other applications may install persistent keyboard "event taps" to intercept your keystrokes. ReiKey can scan, detect, and monitor for such taps!](https://github.com/objective-see/ReiKey)

Browser

* [1lastBr3ath/drmine - Dr. Mine is a node script written to aid automatic detection of in-browser cryptojacking](https://github.com/1lastBr3ath/drmine)
* [leizongmin/js-xss - Sanitize untrusted HTML (to prevent XSS) with a configuration specified by a Whitelist](https://github.com/leizongmin/js-xss)

Traffic analysis

* [dirtbags/pcapdb - A Distributed, Search-Optimized Full Packet Capture System](https://github.com/dirtbags/pcapdb)
* [TravisFSmith/SweetSecurity - Network Security Monitoring on Raspberry Pi type devices](https://github.com/TravisFSmith/SweetSecurity)
* [noddos - Noddos client](https://github.com/noddos/noddos)
* [Suricata - a free and open source, mature, fast and robust network threat detection engine](https://suricata-ids.org/)
* [aol/moloch - Moloch is an open source, large scale, full packet capturing, indexing, and database system](https://github.com/aol/moloch)
* [stamparm/maltrail - Malicious traffic detection system](https://github.com/stamparm/maltrail)
* [360PegasusTeam/WiFi-Miner-Detector - Detecting malicious WiFi with mining cryptocurrency](https://github.com/360PegasusTeam/WiFi-Miner-Detector)
* [activecm/rita - Real Intelligence Threat Analytics](https://github.com/activecm/rita)

Network

* [europa502/shARP - An anti-ARP-spoofing application software that use active and passive scanning methods to detect and remove any ARP-spoofer from the network](https://github.com/europa502/shARP)
* Email
  * [CIRCL/IMAP-Proxy - Modular IMAP proxy (including PyCIRCLeanMail and MISP forward modules)](https://github.com/CIRCL/IMAP-Proxy)

Host based detection tools / endpoint tools

* [hasherezade/pe-sieve - Scans a given process, searching for the modules containing in-memory code modifications. When found, it dumps the modified PE](https://github.com/hasherezade/pe-sieve)
* [hasherezade/hollows_hunter - Scans all running processes. Recognizes and dumps a variety of potentially malicious implants (replaced/implanted PEs, shellcodes, hooks, in-memory patches)](https://github.com/hasherezade/hollows_hunter)
* [jaredcatkinson/Get-InjectedThread.ps1 - Looks for threads that were created as a result of code injection](https://gist.github.com/jaredcatkinson/23905d34537ce4b5b1818c3e6405c1d2)
  * [Understanding and Evading Get-InjectedThread](https://blog.xpnsec.com/undersanding-and-evading-get-injectedthread/)
* [TonyPhipps/THRecon - Collect endpoint information for use in incident response triage / threat hunting / live forensics using this toolkit](https://github.com/TonyPhipps/THRecon)
* [Neo23x0/Fenrir - Simple Bash IOC Scanner](https://github.com/Neo23x0/Fenrir)
* [0x4D31/salt-scanner - Linux vulnerability scanner based on Salt Open and Vulners audit API, with Slack notifications and JIRA integration](https://github.com/0x4D31/salt-scanner)
* [DominicBreuker/pspy - Monitor linux processes without root permissions](https://github.com/DominicBreuker/pspy)
* [mvelazc0/Oriana - a threat hunting tool that leverages a subset of Windows events to build relationships, calculate totals and run analytics](https://github.com/mvelazc0/Oriana/)
* [Hestat/minerchk - Bash script to Check for malicious Cryptomining](https://github.com/Hestat/minerchk)
* HIDS
  * [Invoke-IR/Uproot - a Host Based Intrusion Detection System (HIDS) that leverages Permanent Windows Management Instrumentation (WMI) Event Susbcriptions to detect malicious activity on a network, 2016年停止更新](https://github.com/Invoke-IR/Uproot)
  * [ysrc/yulong-hids - 一款由 YSRC 开源的主机入侵检测系统](https://github.com/ysrc/yulong-hids)
* Memory analysis
  * [DamonMohammadbagher/Meterpreter_Payload_Detection - for detecting Meterpreter in memory like IPS-IDS and Forensics tool](https://github.com/DamonMohammadbagher/Meterpreter_Payload_Detection)
* Active directory
  * [shellster/DCSYNCMonitor - Monitors for DCSYNC and DCSHADOW attacks and create custom Windows Events for these events](https://github.com/shellster/DCSYNCMonitor)
  * [AlsidOfficial/UncoverDCShadow - A PowerShell utility to dynamically uncover a DCShadow attack](https://github.com/AlsidOfficial/UncoverDCShadow)

Sysmon

* [JPCERTCC/SysmonSearch - Investigate suspicious activity by visualizing Sysmon's event log](https://github.com/JPCERTCC/SysmonSearch)
* [darkoperator/Posh-Sysmon - PowerShell module for creating and managing Sysinternals Sysmon config files](https://github.com/darkoperator/Posh-Sysmon)
* Rules
  * [SwiftOnSecurity/sysmon-config - Sysmon configuration file template with default high-quality event tracing](https://github.com/SwiftOnSecurity/sysmon-config)
  * [olafhartong/sysmon-modular - A repository of sysmon configuration modules](https://github.com/olafhartong/sysmon-modular)
  * [Neo23x0/sigma - rules/windows/sysmon](https://github.com/Neo23x0/sigma/tree/master/rules/windows/sysmon)

Webshell detection

* [baidu-security/webshell-scanner-client - A golang client of https://scanner.baidu.com](https://github.com/baidu-security/webshell-scanner-client)
* [nbs-system/php-malware-finder - Detect potentially malicious PHP files](https://github.com/nbs-system/php-malware-finder)
* [emposha/PHP-Shell-Detector - a php script that helps you find and identify php/cgi(perl)/asp/aspx shells](https://github.com/emposha/PHP-Shell-Detector)

Monitoring

* [realparisi/WMI_Monitor - Log newly created WMI consumers and processes](https://github.com/realparisi/WMI_Monitor)
* [luctalpe/WMIMon - Tool to monitor WMI activity on Windows](https://github.com/luctalpe/WMIMon)
* [9b/chirp - Interface to manage and centralize Google Alert information](https://github.com/9b/chirp)
* [facebook/osquery - SQL powered operating system instrumentation, monitoring, and analytics](https://github.com/facebook/osquery)
  * [BlueHat v17 || Detecting Compromise on Windows Endpoints with Osquery](https://www.slideshare.net/MSbluehat/bluehat-v17-detecting-compromise-on-windows-endpoints-with-osquery-84024735)
  * [trailofbits/osquery-extensions - Trail of Bits osquery Extensions](https://github.com/trailofbits/osquery-extensions)
  * [clong/detect-responder - Detect Responder (LLMNR, NBT-NS, MDNS poisoner) with osquery](https://github.com/clong/detect-responder)
* [elastic/beats - Beats - Lightweight shippers for Elasticsearch & Logstash](https://github.com/elastic/beats)
* [dgunter/evtxtoelk - A lightweight tool to load Windows Event Log evtx files into Elasticsearch](https://github.com/dgunter/evtxtoelk)
* Github
  * [FeeiCN/GSIL - GitHub Sensitive Information Leakage（GitHub敏感信息泄露监控）](https://github.com/FeeiCN/GSIL)
  * [neal1991/gshark - Scan for sensitive information in Github easily and effectively](https://github.com/neal1991/gshark)
* Zabbix plugin
  * [vulnersCom/zabbix-threat-control - Zabbix vulnerability assessment plugin](https://github.com/vulnersCom/zabbix-threat-control)
* ElasticSearch addons
  * [NVISO-BE/ee-outliers - Open-source framework to detect outliers in Elasticsearch events](https://github.com/NVISO-BE/ee-outliers)

Log analysis / Visualization

* [Scribery/tlog - Terminal I/O logger](https://github.com/Scribery/tlog)
  * [USER SESSION RECORDING - An Open Source solution](https://ruxcon.org.au/assets/2017/slides/Session%20Recording%20Ruxcon%202017.pdf)
* [JPCERTCC/LogonTracer - Investigate malicious Windows logon by visualizing and analyzing Windows event log](https://github.com/JPCERTCC/LogonTracer)
* [THIBER-ORG/userline - Query and report user logons relations from MS Windows Security Events](https://github.com/THIBER-ORG/userline)
* [austin-taylor/VulnWhisperer - Create actionable data from your Vulnerability Scans](https://github.com/austin-taylor/VulnWhisperer)
* [Windows Security Log Events](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx)

Log queries

* [beahunt3r/Windows-Hunting - Aid windows threat hunters to look for some common artifacts during their day to day operations](https://github.com/beahunt3r/Windows-Hunting)
* [Microsoft/WindowsDefenderATP-Hunting-Queries - Sample queries for Advanced hunting in Windows Defender ATP](https://github.com/Microsoft/WindowsDefenderATP-Hunting-Queries/)

SIEM

* [TheHive-Project/TheHive - TheHive: a Scalable, Open Source and Free Security Incident Response Platform](https://github.com/TheHive-Project/TheHive)
* [wazuh - Host and endpoint security](https://github.com/wazuh/wazuh)
* [uncoder.io - SOC Prime - 转换SIEM查询语句的工具](https://uncoder.io/#)

Yara tools

* [CERT-Polska/mquery - YARA malware query accelerator (web frontend)](https://github.com/CERT-Polska/mquery)
* [botherder/kraken - Cross-platform Yara scanner written in Go](https://github.com/botherder/kraken)
* [Neo23x0/yarGen - a generator for YARA rules](https://github.com/Neo23x0/yarGen)

Sandbox analysis

* [phdphuc/mac-a-mal-cuckoo - This analyzer extends the open-source Cuckoo Sandbox (legacy) with functionality for analyzing macOS malware in macOS guest VM(s)](https://github.com/phdphuc/mac-a-mal-cuckoo)
* [cuckoo-install.sh - Cuckoo auto installer for Ubuntu](https://github.com/NVISO-BE/SEC599/blob/master/cuckoo-install.sh)

Phishing

* [wesleyraptor/streamingphish - Python-based utility that uses supervised machine learning to detect phishing domains from the Certificate Transparency log network](https://github.com/wesleyraptor/streamingphish)
* [OpenPhish - Phishing Intelligence](https://openphish.com/)
* [x0rz/phishing_catcher - Phishing catcher using Certstream](https://github.com/x0rz/phishing_catcher)

Security intelligence / feeds

* [TheHive-Project/Hippocampe - Threat Feed Aggregation, Made Easy](https://github.com/TheHive-Project/Hippocampe)

Uncategorized

* [target/strelka - a real-time file scanning system used for threat hunting, threat detection, and incident response](https://github.com/target/strelka)
* [phishai/phish-protect - Chrome extension to alert and possibly block IDN/Unicode websites and zero-day phishing websites using AI and Computer Vision](https://github.com/phishai/phish-protect)
* [MiSecurity/x-patrol - Github 泄露扫描系统](https://github.com/MiSecurity/x-patrol)
* [Cyb3rWard0g/HELK - The Hunting ELK](https://github.com/Cyb3rWard0g/HELK)
   * [toolsmith #131 - The HELK vs APTSimulator - Part 1](https://holisticinfosec.blogspot.com.au/2018/02/toolsmith-131-helk-vs-aptsimulator-part.html)
* [endgameinc/ClrGuard - a proof of concept project to explore instrumenting the Common Language Runtime (CLR) for security purposes - CLR动态加载检测](https://github.com/endgameinc/ClrGuard)

## Attack Simulation

Tools

* [redhuntlabs/RedHunt-OS - Virtual Machine for Adversary Emulation and Threat Hunting](https://github.com/redhuntlabs/RedHunt-OS)
* [vysec/CACTUSTORCH - Payload Generation for Adversary Simulations](https://github.com/vysec/CACTUSTORCH)
* [NextronSystems/APTSimulator - A toolset to make a system look as if it was the victim of an APT attack](https://github.com/NextronSystems/APTSimulator)
* [redcanaryco/atomic-red-team - Small and highly portable detection tests mapped to the Mitre ATT&CK Framework](https://github.com/redcanaryco/atomic-red-team)
* [mitre/caldera - An automated adversary emulation system](https://github.com/mitre/caldera)
   * [INSTALL/SETUP MITRE CALDERA THE AUTOMATED CYBER ADVERSARY EMULATION SYSTEM](https://holdmybeersecurity.com/2018/01/13/install-setup-mitre-caldera-the-automated-cyber-adversary-emulation-system/)
* [uber-common/metta - An information security preparedness tool to do adversarial simulation](https://github.com/uber-common/metta)
* [endgameinc/RTA - RTA provides a framework of scripts designed to allow blue teams to test their detection capabilities against malicious tradecraft, modeled after MITRE ATT&CK.](https://github.com/endgameinc/RTA)
* [TryCatchHCF/DumpsterFire - DumpsterFire Toolset - "Security Incidents In A Box!"](https://github.com/TryCatchHCF/DumpsterFire)
* [jymcheong/AutoTTP - Automated Tactics Techniques & Procedures](https://github.com/jymcheong/AutoTTP)
* [Cyb3rWard0g/Invoke-ATTACKAPI - A PowerShell script to interact with the MITRE ATT&CK Framework via its own API](https://github.com/Cyb3rWard0g/Invoke-ATTACKAPI)
* [CyberMonitor/Invoke-Adversary - Simulating Adversary Operations](https://github.com/CyberMonitor/Invoke-Adversary)
* [P4T12ICK/ypsilon - an Automated Security Use Case Testing Environment using real malware to test SIEM use cases in an closed environment](https://github.com/P4T12ICK/ypsilon)
* [n0dec/MalwLess - Test Blue Team detections without running any attack](https://github.com/n0dec/MalwLess)

Dataset

* [splunk/botsv1 - Boss of the SOC (BOTS) Dataset Version 1](https://github.com/splunk/botsv1)

## Resources

* [A source for pcap files and malware samples](http://www.malware-traffic-analysis.net/)

## Tutorials

Uncategorized

* [Tales of a Threat Hunter 2 - Following the trace of WMI Backdoors & other nastiness](https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/)
* [awslabs/aws-security-automation - Collection of scripts and resources for DevSecOps and Automated Incident Response Security](https://github.com/awslabs/aws-security-automation)
* [mitre/attack-navigator - Web app that provides basic navigation and annotation of ATT&CK matrices](https://github.com/mitre/attack-navigator)
* [Establishing a Baseline for Remote Desktop Protocol](https://www.fireeye.com/blog/threat-research/2018/04/establishing-a-baseline-for-remote-desktop-protocol.html)
* [Disrupting the Empire: Identifying PowerShell Empire Command and Control Activity](https://www.sans.org/reading-room/whitepapers/incident/disrupting-empire-identifying-powershell-empire-command-control-activity-38315)
* [OffensiveSplunk vs. Grep](https://vincentyiu.co.uk/offensivesplunk/)

Books

* [OWASP - Automated Threat Handbook - Web Applications](https://www.owasp.org/images/3/33/Automated-threat-handbook.pdf)

Frameworks

* [palantir/alerting-detection-strategy-framework - A framework for developing alerting and detection strategies for incident response](https://github.com/palantir/alerting-detection-strategy-framework)

Auditing

* [WINDOWS REGISTRY AUDITING CHEAT SHEET - Win 7/Win 2008 or later](https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/5a00963153450a8779b23489/1509987890282/Windows)
* [WINDOWS ATT&CK LOGGING CHEAT SHEET - Win 7 - Win 2012 - ATT&CK模型，以及对应的日志编号，很有用](https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/5b8f091c0ebbe8644d3a886c/1536100639356/Windows+ATT&CK_Logging+Cheat+Sheet_ver_Sept_2018.pdf)
