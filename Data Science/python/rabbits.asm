[bits 64]

; (string, length)
%macro  print    2
        mov     rax, 1
        mov     rdi, 1
        mov     rsi, %1
        mov     rdx, %2
        syscall
%endmacro


section .data
    string1 db  0xa, "  Hello Print!", 0xa, 0xa, 0

section .text
    global _start

    len:
        mov rax, [esp + 4]

        mov rdi, rax

        xor     rcx, rcx            ; zero rcx
        not     rcx                 ; set rcx = -1
        xor     al,al               ; zero the al register (initialize to NUL)
        cld                         ; clear the direction flag
        repnz   scasb               ; get the string length (dec rcx through NUL)
        not     rcx                 ; rev all bits of negative results in absolute value
        dec     rcx                 ; -1 to skip the null-terminator, rcx contains length
        mov     rdx, rcx            ; put length in rdx

        push rdx
        ret

    exit:
        xor     rdi,rdi             ; zero rdi (rdi hold return value)
        mov     rax, 0x3c           ; set syscall number to 60 (0x3c hex)
        syscall

    _start:
        push string1
        call len

        push string1
        call print

        call exit