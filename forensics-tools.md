# opensource-forensics-tools

A collection of open source forensics tools

## Collections

3rd-party lists

* [FreeBUF: 安全应急响应工具年末大放送（含下载）](http://www.freebuf.com/sectool/87400.html)
* [meirwah/awesome-incident-response - A curated list of tools for incident response](https://github.com/meirwah/awesome-incident-response)
* [Bellingcat's Digital Forensics Tools](https://docs.google.com/document/d/1BfLPJpRtyq4RFtHJoNpvWQjmGnyVkfE2HYoICKOGguA/edit)

Suite

* [fireeye/rVMI - A New Paradigm For Full System Analysis](https://github.com/fireeye/rVMI)
* [CERTCC/trommel - Sift Through Embedded Device Files to Identify Potential Vulnerable Indicators](https://github.com/CERTCC/trommel)
* [rough007/CDQR - a fast and easy to use forensic artifact parsing tool that works on disk images, mounted drives and extracted artifacts from Windows, Linux and MacOS devices](https://github.com/rough007/CDQR)
* [biggiesmallsAG/nightHawkResponse - Incident Response Forensic Framework](https://github.com/biggiesmallsAG/nightHawkResponse)
* [google/grr -Rapid Response: remote live forensics for incident response](https://github.com/google/grr)
* [davehull/Kansa - A Powershell incident response framework](https://github.com/davehull/Kansa)

Packet injection

* [netresec.com: findject.py - a simple python script that can find injected TCP packets in HTTP sessions, such as the QUANTUMINSERT Man-on-the-Side (MOTS) attacks](https://www.netresec.com/?page=findject)

Memory forensics

* [gleeda/memtriage - Allows you to quickly query a Windows machine for RAM artifacts](https://github.com/gleeda/memtriage)
* [sevagas/swap_digger - a tool used to automate Linux swap analysis during post-exploitation or forensics](https://github.com/sevagas/swap_digger)
* [google/rekall - Rekall Memory Forensic Framework](https://github.com/google/rekall)
  * [toolsmith – Hunting In-Memory Adversaries with Rekall and WinPmem](https://holisticinfosec.org/toolsmith/pdf/may2015.pdf)
* [ufrisk/MemProcFS - The Memory Process File System](https://github.com/ufrisk/MemProcFS)
* [comaeio/LiveCloudKd - Hyper-V Research is trendy now](https://github.com/comaeio/LiveCloudKd)
* [Extracting Activity History from PowerShell Process Dumps - 没给工具，用WinDBG解析powershell内存，提取HistoryInfo](http://www.leeholmes.com/blog/2019/01/04/extracting-activity-history-from-powershell-process-dumps/)

Windows

* [comaeio/Hibr2Bin - Comae Hibernation File Decompressor](https://github.com/comaeio/Hibr2Bin)
* [ANSSI-FR/bits_parser - Extract BITS jobs from QMGR queue and store them as CSV records](https://github.com/ANSSI-FR/bits_parser)
* [williballenthin/python-evtx - Pure Python parser for recent Windows Event Log files (.evtx)](https://github.com/williballenthin/python-evtx/blob/master/scripts/evtx_dump.py)
* [fox-it/danderspritz-evtx - Parse evtx files and detect use of the DanderSpritz eventlogedit module](https://github.com/fox-it/danderspritz-evtx)
* [PowerShellMafia/CimSweep - a suite of CIM/WMI-based tools that enable the ability to perform incident response and hunting operations remotely across all versions of Windows](https://github.com/PowerShellMafia/CimSweep)
* [mgreen27/Powershell-IR - Invoke-LiveResponse](https://github.com/mgreen27/Powershell-IR)
* [sysinsider/usbtracker - Quick & dirty coded incident response and forensics python script to track USB devices events and artifacts in a Windows OS (Vista and later)](https://github.com/sysinsider/usbtracker)
* [gfoss/PSRecon - gathers data from a remote Windows host using PowerShell (v2 or later), organizes the data into folders, hashes all extracted data, hashes PowerShell and various system properties, and sends the data off to the security team](https://github.com/gfoss/PSRecon)
* [B2dfir/wlrip - WaitList.dat Parser](https://github.com/B2dfir/wlrip)

Mac

* [n0fate/chainbreaker - Mac OS X Keychain Forensic Tool](https://github.com/n0fate/chainbreaker)
* [mdegrazia/OSX-QuickLook-Parser - Parse the Mac Quickook index.sqlite database](https://github.com/mdegrazia/OSX-QuickLook-Parser)
* [gist: dumpNotificationDB.py](https://gist.github.com/CaledoniaProject/e7176eb644e5e78610d9f43cacaeb84b)
* [mac4n6/macMRU-Parser - parse the Most Recently Used (MRU) plist files on macOS into a more human friendly format](https://github.com/mac4n6/macMRU-Parser)
* [dlcowen/FSEventsParser - Parser for OSX/iOS FSEvents Logs](https://github.com/dlcowen/FSEventsParser)
* [ydkhatri/mac_apt - macOS Artifact Parsing Tool](https://github.com/ydkhatri/mac_apt)
* [Yelp/osxcollector - A forensic evidence collection & analysis toolkit for OS X](https://github.com/Yelp/osxcollector)
* [pstirparo/mac4n6 - Collection of forensics artifacs location for Mac OS X and iOS](https://github.com/pstirparo/mac4n6)

Linux

* [sevagas/swap_digger - a tool used to automate Linux swap analysis during post-exploitation or forensics](https://github.com/sevagas/swap_digger)
* [JPT - A quick & dirty GPT Partition Editor](http://newandroidbook.com/tools/jpt.html)
* [lukdog/backtolife - Memory forensic tool for process resurrection starting from a memory dump](https://github.com/lukdog/backtolife)
* [eurecom-s3/linux_screenshot_xwindows - Volatility plugin to extract X screenshots from a memory dump](https://github.com/eurecom-s3/linux_screenshot_xwindows)

Browser

* [Busindre/dumpzilla - Extract all forensic interesting information of Firefox, Iceweasel and Seamonkey browsers](https://github.com/Busindre/dumpzilla)
* [obsidianforensics/hindsight - Internet history forensics for Google Chrome/Chromium](https://github.com/obsidianforensics/hindsight)

Disk tools

* [KBNLresearch/isolyzer - Verify size of ISO 9660 image against Volume Descriptor fields](https://github.com/KBNLresearch/isolyzer)
* [ntfsfix - Rescuing a broken NTFS filesystem](https://marcan.st/2015/10/rescuing-a-broken-ntfs-filesystem/)

Mobile

* [andreas-mausch/whatsapp-viewer - Small tool to display chats from the Android msgstore.db database (crypt12)](https://github.com/andreas-mausch/whatsapp-viewer)
* [B16f00t/whapa - WhatsApp Parser Tool v0.2](https://github.com/B16f00t/whapa)
* [silentsignal/burp-cfurl-cache - iOS CFURL Cache inspector for Burp Suite](https://github.com/silentsignal/burp-cfurl-cache)

Network

* [Srinivas11789/PcapXray - A Network Forensics Tool - To visualize a Packet Capture offline as a Network Diagram including device identification, highlight important communication and file extraction](https://github.com/Srinivas11789/PcapXray)

Uncategorized

* [Netflix-Skunkworks/diffy - Diffy is a triage tool used during cloud-centric security incidents, to help digital forensics and incident response (DFIR) teams quickly identify suspicious hosts on which to focus their response](https://github.com/Netflix-Skunkworks/diffy)

## Tutorials

* [OSX (Mac) Memory Acquisition and Analysis Using OSXpmem and Volatility](https://ponderthebits.com/2017/02/osx-mac-memory-acquisition-and-analysis-using-osxpmem-and-volatility/)
* [Mobile Incident Response Overview](https://books.nowsecure.com/mobile-incident-response/en/overview/index.html)
* [Cache Me If You Can - by 505Forensics](https://speakerdeck.com/505forensics/cache-me-if-you-can)
* [Advanced smartphone forensics - Apple iCloud: backups, document storage, keychain; BlackBerry 10 backup encryption ](https://www.troopers.de/media/filer_public/48/4e/484ec809-8c6c-413b-a538-abb3e24231fd/troopers14-advanced_smartphone_forensics-vladimir_katalov.pdf)
* [Logs Unite! - Forensic Analysis of Apple Unified Logs - by mac4n6](https://github.com/mac4n6/Presentations/blob/master/Logs%20Unite!%20-%20Forensic%20Analysis%20of%20Apple%20Unified%20Logs/LogsUnite.pdf)
* [DIGITAL FORENSICS – ARTIFACTS OF INTERACTIVE SESSIONS](https://countuponsecurity.com/2017/11/22/digital-forensics-artifacts-of-interactive-sessions/)

## Other resources

Artifacts

* [iOS Forensics Artifacts v0.1](https://docs.google.com/spreadsheets/d/1z-44BUA2AVf8uqnoiDDSi7UxbyWy8KJqK4uaYq_0YYg/edit)
* [Mac OS X Forensics Artifacts](https://docs.google.com/spreadsheets/d/1X2Hu0NE2ptdRj023OVWIGp5dqZOw-CfxHLOW_GNGpX8/edit#gid=3)









