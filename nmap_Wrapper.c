
/*****
- nmap scripts that uses shared library through
ctypes.

This code will do the following

1. Creating a C shared library that can execute Nmap commands.
2. Creating a Python script that uses ctypes to interact with this library.
3. Using the Nmap tool to execute specific scripts

This C code provides a function run_nmap_script that takes a target IP/hostname
and a script name, then constructs and executes the Nmap command using the system function.

*****/


#include <stdio.h>
#include <stdlib.h>


void run_nmap_script(const char* target, const char* script ) {
    char command[256];
    snprintf(command, sizeof(command), "nmap --script=%s %s", script,target);
    system(command);


}
