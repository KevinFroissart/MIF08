	.text
	.globl main
main: 	                                                           
	addi	sp,sp,-16
	sd	ra,8(sp)
## TODO Your assembly code there
	li t0, 62 #load immediat t0=5
	li t1, 10 #load immediat t1=10
	la t3, min #load address t3=min
	bgt t0, t1, else #si t0 > t1 then jump to else
		sd t3, 0(t0)
		j print #jump to print
	else:
		sd t3, 0(t1)
		j print #jump to print
print:
	ld t4, 0(t3) #load data of t3 in t4 ie. t4=0
	add a0, a0, t4 #add content of t4(min) in a0
	call print_int #print a0
	call newline #\n
	j end #jump to end
## END TODO - end of user assembly code
end:
	ld	ra,8(sp)
	addi	sp,sp,16
	jr	ra
	ret

# Data comes here
	.section	.data
mydata:
	.dword 7
	.dword 42
min:
	.dword 0
