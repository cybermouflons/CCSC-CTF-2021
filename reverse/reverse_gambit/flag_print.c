#include <stdio.h>
#include <stdint.h>
#include <malloc.h>
#include <string.h>
#include "includes.h"

#pragma GCC push_options
#pragma GCC optimize ("-fno-omit-frame-pointer")
#pragma GCC optimize ("-fno-stack-protector")

void run_code() {
    unsigned char crypt[24];
    __asm__ volatile (
    "movq $0x4141414141414141, %%rcx;"
    "movq $0x3372373a22322222, %%rax;"
    "xorq %%rcx, %%rax;"
    "movq %%rax, (%%rdi);"
    "movq $0x221e383275241e38, %%rax;"
    "xorq %%rcx, %%rax;"
    "movq %%rax, 8(%%rdi);"
    "movq $0x3c2d2d7529, %%rax;"
    "xorq %%rcx, %%rax;"
    "movq %%rax, 16(%%rdi);"
    : /* outputs */
    : "D" (crypt)/* inputs */
    : "rax", "rcx"
    );
    __asm__ volatile (
    "syscall"
    ::"a" (1), "D" (1), "S" (crypt), "d" (sizeof(crypt) - 3)
    );
}

void CODE_END(void) { return; }

#pragma GCC pop_options

int main(int argc, char *argv[]) {
    unsigned long shellcode_size = (unsigned long) CODE_END - (unsigned long) run_code;
    uint32_t *raw_code = (uint32_t *) malloc(shellcode_size);
    memcpy(raw_code, (unsigned char *) run_code, shellcode_size);
    uint32_t key = FLAG_CIPHERTEXT_KEY;
    for (int i = 0; i < shellcode_size / sizeof(uint32_t); i++) {
        raw_code[i] ^= key;
    }

    uint8_t *ptrb_raw_code = (uint8_t *) raw_code;
    printf("Generating file at %s", argv[1]);
    FILE *fp = fopen(argv[1], "w");
    fprintf(fp, "__attribute__((section(\".secret\"))) unsigned char flag_ciphertext[] = {\n\t");
    for (int i = 0; i < shellcode_size; i++) {
        fprintf(fp, "0x%02x", ptrb_raw_code[i]);
        if (i + 1 != shellcode_size) fprintf(fp, ", ");
        if ((i + 1) % 16 == 0) fprintf(fp, "\n\t");
    }
    fprintf(fp, "\n};");
    fclose(fp);
}