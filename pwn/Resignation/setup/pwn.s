; ----------------------------------------------------------------------------------------
; nasm -felf64 pwn.s && ld pwn.o -z noexecstack -o pwn -s
; 
; ----------------------------------------------------------------------------------------

global    _start

section   .text
     _vuln:
          push      rbp                     ; save previous stack frame ret address
          mov       rbp, rsp                ; save ret address in rbp 
          sub       rsp, 0x20               ; make space for local variable
          lea       rsi, [rbp - 0x20]        ; load addr of local local_96 into RSI
          mov       rax, 0                  ; system call for read
          mov       rdi, 0                  ; file handle 1 is stdin
          mov       rdx, 0x180               ; number of bytes
          syscall                           ; invoke operating system to do the read

          mov rcx, 0x20
          lea rsi, [rbp - 0x20]
          lea rdi, [message]
     .copy:
          lodsb
          stosb
          dec rcx
          cmp rcx, 0
          jg .copy          
          leave                             ; cleanup current frame
          ret

     _start:   
          mov       rax, 1                  ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout
          mov       rsi, message            ; address of string to output
          mov       rdx, 14                 ; number of bytes
          syscall                           ; invoke operating system to do the write
          call       _vuln
          mov       rax, 0x3C               ; system call for exit
          mov       rdi, 0                  ; exit_status
          mov       rdx, 0
          syscall

     _help:
          pop rax
          ret

section   .data
     message:  db        "Hello, friend", 0xa, 0      ; note the newline at the end
