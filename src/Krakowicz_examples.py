# Some code sequences from
# http://www.textfiles.com/100/krckwczt.app

# This shows how to simply feed in straight text
# by passing it through splitlines()

from asm6502 import asm6502

thecode = """
  ORG  $100
  LDY  #$00    ;CLEAR Y-REGISTER
  LDA  $00,Y   ;GET A BYTE FROM 0+Y
  STA  $2000,Y ;STORE AT 2000+Y
  LDA  $0100,Y ;THEN FROM 100+Y
  STA  $2100,Y ;TO 2100+Y
  LDA  $0200,Y ;AND SO ON UNTIL
  STA  $2200,Y ;WE HAVE COVERED
  LDA  $0300,Y ;ALL THE MEMORY
  STA  $2300,Y ;'PAGES' FROM 0 TO 8
  LDA  $0400,Y ;AND STORED INTO
  STA  $2400,Y ;PAGES 20 TO 28
  LDA  $0500,Y
  STA  $2500,Y
  LDA  $0600,Y
  LDA  $2600,Y
  LDA  $0700,Y
  STA  $2700,Y
  LDA  $0800,Y
  STA  $2800,Y
  INY	       ;THEN ADD 1 TO Y-REG
  BNE  $FED0   ;AND REPEAT IF < 256
  JMP  $FF59   ;WHEN WE'RE ALL DONE
	       ;JUMP TO MONITOR START

  ORG  $1000   ; A new location for a different code sequence
  LDY  #$00    ;CLEAR Y-REGISTER
  LDA  $00,Y   ;XFER THE ZERO PAGE TO
  STA  $2000,Y ;2000-20FF SO WE CAN USE
  INY	       ;THE ZERO PAGE MEMORY
  BNE  $FED0   ;FOR THE OTHER MOVES
  LDA  #$00    ;SET UP LOCNS 0 & 1 AS A
  STA  $00     ;2-BYTE POINTER FOR THE
  STA  $02     ;SOURCE ADDRESS, USE 2&3
  LDA  #$01    ;AS 2-BYTE POINTER FOR
  STA  $01     ;THE DESTINATION ADDRESS
  LDA  #$21    ;STARTING AT $2100
  STA  $03
  loophere: LDA  ($00)   ;GET A BYTE FROM 100-UP
  STA  ($02)   ;STORE AT 2100-UP
  INC  $02     ;INCREMENT LO-ORDER BYTE
  INC  $00     ;OF SOURCE & DESTINATION
  BNE  loophere        ;(BACK TO LDA ($00) IF
	       ;LO-ORDER IS <256
  INC  $03     ;IF LO-ORDER=0, INC THE
  INC  $01     ;HI BYTE OF EACH
  LDA  $01     ;CHECK TO SEE IF HI-BYTE
  CMP  #$09    ;IS 9 -WE'RE THRU AT 8FF
  BNE  loophere        ;IF NOT, LOOP BACK TO
	       ;THE LOAD/STORE UNTIL
	       ;WE'RE ALL DONE
  JMP  $FF59   ;EXIT THRU MONITOR
"""

lines = thecode.splitlines()

a = asm6502()
a.assemble(lines)

