	.text
	.globl main
main: 	                                                           
	addi	sp,sp,-16
	sd	ra,8(sp)
## TODO Your assembly code there
	la t0, mydata #load address mydata in t0
	ld t1, 0(t0) #load data of t0 in t1
	li t2, 0 #load value 0 in t2
	li a0, 42 #load *
	l: #loop named l
		beq t2, t1, end #if t2 == t1 jump to end
		addi t2, t2, 1 #t2++
		li t3, 0 #t3 = 0
		j l2 #jump to l2
	l2: #loop named l2
		beq t3, t1, l3 #if t3 == t1 jump to l
		addi t3, t3, 1 #t3++
		call print_char #print a0
		j l2 #jump to l
	l3:
		call newline #\n
		j l
## END TODO /end of user assembly code
end:
	ld	ra,8(sp)
	addi	sp,sp,16
	jr	ra
	ret

# Data comes here
	.section	.data
mydata:
	.dword 3
