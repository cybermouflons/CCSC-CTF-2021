#include <stdio.h>
#include <stdlib.h>
#include <string.h>

size_t idx = 0;
char* gms[64]; 

int create(){
    // check max size reached
    if (idx > 10){
        printf("Max. limit reached\n");
        return 0;
    }

    // assign memory for gms name
    gms[idx] = malloc(0x68);
    
    // get name
    printf("Name: ");
    read(0, gms[idx], 64);
    //gms[idx][8] = '\0'; // null-terminate name
    
    idx = idx + 1; // increment idx
    return 0;
}


void delete(){
    int idx_del;
    printf("Index: \n");
    scanf("%d",&idx_del);

    // check max size reached
    if (idx_del > idx){
        printf("Invalid index\n");
        return;
    }

    // delete gms
    free(gms[idx_del]);
}

void edit(){
    int idx_edit;
    printf("Index: ");
    scanf("%d",&idx_edit);

    // check max size reached
    if (idx_edit >= idx){
        printf("Invalid index\n");
        return;
    }

    // edit gms
    flush();
    printf("New name: ");
    read(0, gms[idx_edit], 64);
}


void view(){
    int idx_view;
    printf("Index: ");
    scanf("%d",&idx_view);

    // check max size reached
    if (idx_view >= idx){
        printf("Invalid index\n");
        return;
    }

    // view gms
    printf("Grand Master: %s\n", gms[idx_view]);
}

void flush(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    fflush(stdout);
}


int main(int argc, char** argv){
    flush();
    char empty[128]; 
    
    for (int i = 0; i < 128; i++){
        memset(empty, 0, 8);
    }

    int menu_option = 0;
    printf("\n------------------------------------------\n");
    printf("       Create a new Grand Master!!!\n");
    printf("------------------------------------------\n");

    do {
        printf("\nMain Menu\n");
        printf("1. Create Grand Master.\n");
        printf("2. Delete Grand Master.\n");
        printf("3. View Grand Master.\n");
        printf("4. Edit.\n");
        printf("5. Exit.\n");
        printf("Please enter an option from the main menu: ");
        scanf("%d", &menu_option);
        flush();

        switch(menu_option){
            case 1:
                create();
                break;
            case 2:             
                delete();
                break;
            case 3:             
                view();
                break;
            case 4:
                edit();
                break;
            case 5:
                printf("\nExiting...\n");                           
                exit(0);
            default:
                printf("\nInvalid input, try again!\n");
                break;
        } 
    } while(menu_option != 5);
    return 0;
}
