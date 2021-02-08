#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

struct record {
    char piece[40];
    char * color;
};

int main() {
    // Print Title
    setbuf(stdout, 0);
    puts("Chess Analyzer\nInput your chess piece and the color of the square it is located and we will figure out the rest.\n");

    // Create the struct record
    struct record move;
    
    strcpy(move.piece, "Queen's Rook");
    move.color = (char *) malloc(sizeof(char) * 40);
    strcpy(move.color, "White");
    printf("For example we chose: \n\t\t%s \n\t\t(%s)\n\nChoose a new piece: ", move.piece, move.color);

    // Read some user data
    read(0, move.piece, 44);
    printf("You chose: \n\t\t%s \t\tOld(%s)\n\nChoose the color of the square it is located please: ", move.piece, move.color);

    // Overwrite the color
    read(0, move.color, 4);
    printf("You chose: \n\t\t%s \t\t(%s)\n\nYour chosen piece is: ", move.piece, move.color);

    // Print the piece again
    puts(move.piece);
}
