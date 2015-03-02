#!/usr/bin/env python


import sys
import subprocess

from system_level import system_level
from ddDaemon import daemon

if (sys.version_info[1]) <= 6:
    print("Its recommended to use python version 2.7 or above. 2.7 is the best!")
    sys.exit(1)
    
ddConfig = {
        'version': 0.1.0,
        'interval': 120
           }

def no_of_cores():
    
    greppy = subprocess.Popen(['grep', 'cpu cores', '/proc/cpuinfo'], stdout=subprocess.PIPE, close_fds = True)
    printLine = subprocess.Popen(['wc -l'], stdin=greppy.stdout, stdout=subprocess.PIPE, close_fds = True)
    noOfCores = printLine.communicate()[0]
    
    return int(noOfCores)

class datadust_agent(Daemon):
    
    
    BasicStats = {
            'processorType' = platform.processor(),
             'noOfCores' = no_of_cores(),
             'os' = sys.platform,      
              'nixDist' = platform.dist()   
              } 
    #expand later when more dist support!(.) 
    
    
    #system_level instance 
    sysLevel = system_level(ddConfig) 
    schedule = sched.scheduler(time.time, time.sleep)
    sysLevel.system_levelChecks(scchedule, True, BasicStats)  
    schedule.run()
    
    
if __name__ == '__main__':
        
    #need to do logging - logFile(.)
    