	.text
	.globl main
main: 	                                                           
	addi	sp,sp,-16
	sd	ra,8(sp)
## TODO Your assembly code there
	li t0,5
	li t1,10
	bgt t0,t1,else
	sd t1,min
	call	print_int
	call	newline
	j end
	else:
		sd t0,min
		call	print_int
		call	newline
		j end
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


