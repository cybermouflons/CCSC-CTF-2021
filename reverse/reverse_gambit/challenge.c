#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include "challenge.h"
#include <sys/mman.h>
#include <stdlib.h>

#pragma GCC push_options
#pragma GCC optimize ("-fno-tree-vectorize")
void decrypt(uint32_t key) {
    long page_size = sysconf(_SC_PAGESIZE);
    uintptr_t page_start = (uintptr_t) flag_ciphertext & -page_size;
    int size = (int) ((uint8_t *) flag_ciphertext - (uint8_t *) page_start);

    if (mprotect((void *) page_start, size, PROT_READ | PROT_WRITE | PROT_EXEC) < 0) {
        perror("mprotect:");
    }

    uint32_t *ciphertext_ptr = (uint32_t *) flag_ciphertext;
    for (int i = 0; i < sizeof(flag_ciphertext) / sizeof(uint32_t); i++) {
        ciphertext_ptr[i] ^= key;
    }
}
#pragma GCC pop_options


int main(int argc, char *argv[]) {
    void (*print_flag)() = 0;
    if (argc < 2) {
        printf("Usage: %s hex_key", argv[0]);
        return 1;
    }
    uint32_t key = strtol(argv[1], NULL, 16);
    decrypt(key);
    if (*((uint32_t *) flag_ciphertext) == 0xe5894855) {
        print_flag = (void (*)()) flag_ciphertext;
        print_flag();
        printf("\n");
    } else {
        printf("Invalid key\n");
    }
    return 0;
}