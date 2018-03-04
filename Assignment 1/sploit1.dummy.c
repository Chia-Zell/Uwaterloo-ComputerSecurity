/*
 * dummy exploit program
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "/usr/local/src/shellcode.h"

#define TARGET "/usr/local/bin/pwgen"

int main(void)
{
  char *args[4];
  char *env[1];

  // one way to invoke pwgen, system() creates a separate process
  system("/usr/local/bin/pwgen -v");

  // another way
  args[0] = TARGET; args[1] = "--type"; 
  args[2] = "3"; args[3] = NULL;

  env[0] = NULL;
  // execve() executes the target program by overwriting the
  // memory of the process in which execve() is executing, i.e., 
  // execve() should never return
  if (execve(TARGET, args, env) < 0)
    fprintf(stderr, "execve failed.\n");

  exit(0);
}
