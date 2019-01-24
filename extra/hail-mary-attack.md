##What is the Hail Mary Attack?

The Hail Marry Attack is an exploiting option avilable in [Armitage](http://fastandeasyhacking.com), a Java based client for Metasploit. Essentially,
running every potential exploit you think may work on the system with a single click. In this tutorial I will be helping
you get started with Armitage, and then show you how to perform the Hail Marry Attack.

If you have Armitage installed, skip the installation section.

# 0. Installation

There are two main options for you to get started with Armitage:
  * If you have a recent [Kali](https://newblood.anonops.com/security.html#adt) distribution installed, you will most likely have Armitage already installed for you. *Recommended*
  * If you have a linux machine, follow this guide to [install](http://www.darkoperator.com/installing-metasploit-in-ubunt/) Armitage but read the note below first.

**Note** -- Setting up Armitage from scratch can be a hassle as it is highly dependant on Metasploit, and a database software,and requires lots of packages for it to run properly,
it is highly recommended that you get started with Kali as your first option. If you still want to do it, you will have lots of fun and learn a lot.


# 1. Start your engines
  
  Before we can run Armitage, we have to have to run two that Armitage needs,

  1.1 **PostgreSQL** - Armitage needs to store details about your hosts, ip addresses, ports, services, etc.
  To start PostgreSQL, open a terminal window, and in it type the following
  
    sudo service postgresql start
  1.2 **Metasploit** - Armitage does not use the Metasploit service, but starting it once will setup a database.yml file for your system.
  To start Metasploit, go back to your terminal -hopefully you did not close it, a hacker never does- and in it type the following
  
    sudo service metasploit start

# 2. Run Armitage

  2.1 **Connecting to the Database** - Armitage will have the connection details already filled in for you, just hit connect. 
  Look at the advanced section to see how to change the connection details.
  
    JUST CLICK YES!
  
  2.2 **Starting the Metasploit RPC** - We need Armitage and Metasploit to exchange data about everything that is happening, so we start a service that allows us to make remote procedure calls to Metasploit.
  So **in short**, we allow Armitage to conrtol Metasploit.
  
    JUST CLICK YES, AGAIN!
    
# 3. Understanding Armitage
  
  The main window has three main sections
  
  3.1 **Tree Menu** - This gives you access to various functions of Metasploit, such as *exploits*, *payloads*, *auxiliries*, and *additional scanners*.
  
  3.2 **Hosts Area** - This will be empty at first, but hosts will show up with important information once we start our work.
  
  3.3 **Console** - This is the equivelent of your terminal for Metasploit.
  
# 4. Adding and scanning hosts

  4.1 **Adding Hosts** - First of all we have to add hosts for Armitage and Metasploit to work with, from the top-bar menu click `Hosts > Add Hosts`, enter the ip address/es of your host/s. 
  Then click `add`. You should see machine icons show up in the `hosts area`.
  
  4.2 **Scanning Hosts** - Now we can perform nmap scans on our hosts, you can read more about nmap scans [here](https://github.com/kingcrispy/opparis/blob/master/hackingschool/nmap.md).
  Armitage gives you the option to perform different types of scans with one click. To scan a hosts, click on the `Hosts > Nmap Scan > Scan type` and choose the type of scan you would like to perform.
  
    *Quick scans
    *Comprehensive scans
    *UDP Scans
    *OS Detect - This is very useful, it helps you narrow down the number of exploits based on the speculated OS.
    *And a lot more ...

  Scan your hosts, and look at the scan results in the bottom area of the screen, next to the `Console` tab.
  If you perform a OS Detect Scan, the icon of the machine will change accordingly if the OS was successfully detected.
  You can also use the context/right-click menu to perform tasks like running an exploit, or a scanner.
  
  
#5. Prime Time: Hail Mary

To perform the Hail Mary attack select a host from the `hosts area`, and then from the top-menu select `Attack > Hail Mary`. This will start running exploits aginst the host you have selected, based on the information it already has about the machine, the OS type, or which service running on a given port, for example


The **Hail Mary Attack** is defintely one of my favorite attacks.


Enjoy the knowledge, and change the world!

-- King Crispy
