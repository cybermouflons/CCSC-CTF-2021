#include <stdio.h>

int main() {
    char buffer[128];
    setbuf(stdout, 0);
    puts("Hello, unfortunately Beth is currently in the middle of a game.\nPlease wait in the waiting room until your name is called.\n\nIs there something we could help you with while you wait?\n");
    gets(buffer);

    return 0;
}


//     printf("Hi I'm Beth, what is your name?\n");
//     printf("Hello, unfortunately Beth is currently in the middle of a game.\nPlease wait in the waiting room until your name is called.\n");
// }

// Talk to me