#! /usr/bin/env python
from asm_test import Asm_Test
import sys

class Test_PUNPCKHBW(Asm_Test):
    TXT = '''
    main:
       CALL      next
       .byte 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11
       .byte 0x01, 0x02, 0xFF, 0xEE, 0xDD, 0xCC, 0xBB, 0xAA
    next:
       POP       EBP
       MOVQ      MM0, QWORD PTR [EBP]
       MOVQ      MM1, MM0
       PUNPCKHBW MM1, QWORD PTR [EBP+0x8]
       RET
    '''

    def check(self):
        assert self.myjit.cpu.MM0 == 0x1122334455667788
        assert self.myjit.cpu.MM1 == 0xAA11BB22CC33DD44


class Test_PUNPCKHWD(Asm_Test):
    TXT = '''
    main:
       CALL      next
       .byte 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11
       .byte 0x01, 0x02, 0xFF, 0xEE, 0xDD, 0xCC, 0xBB, 0xAA
    next:
       POP       EBP
       MOVQ      MM0, QWORD PTR [EBP]
       MOVQ      MM1, MM0
       PUNPCKHWD MM1, QWORD PTR [EBP+0x8]
       RET
    '''

    def check(self):
        assert self.myjit.cpu.MM0 == 0x1122334455667788
        assert self.myjit.cpu.MM1 == 0xAABB1122CCDD3344



class Test_PUNPCKHDQ(Asm_Test):
    TXT = '''
    main:
       CALL      next
       .byte 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11
       .byte 0x01, 0x02, 0xFF, 0xEE, 0xDD, 0xCC, 0xBB, 0xAA
    next:
       POP       EBP
       MOVQ      MM0, QWORD PTR [EBP]
       MOVQ      MM1, MM0
       PUNPCKHDQ MM1, QWORD PTR [EBP+0x8]
       RET
    '''

    def check(self):
        assert self.myjit.cpu.MM0 == 0x1122334455667788
        assert self.myjit.cpu.MM1 == 0xAABBCCDD11223344

if __name__ == "__main__":
    [test()() for test in [Test_PUNPCKHBW, Test_PUNPCKHWD, Test_PUNPCKHDQ]]
