#!"C:\Program Files\Python35\python.exe"
import os

os.system("net stop dbsrvr_mw_2014_1401")

os.system("net start dbsrvr_mw_2014_1401")

print("")
print("<h1>")
print("")
print("Success!  You have restarted the Mailware 2014 Database Server.")
print("</h1>")