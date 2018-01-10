/*
 * dummy exploit program
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
//#include "/usr/local/src/shellcode.h"

#define TARGET "/usr/local/bin/pwgen"

int main(void)
{
  char *args[4];
  char *env[1];

  // one way to invoke pwgen, system() creates a separate process
  char *buf = 'x00' * 1000 +'\0';
  system("/usr/local/bin/pwgen -v" + buf);



  exit(0);
}
