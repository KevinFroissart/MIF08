	.text
	.globl main
main: 	                                                           
	addi	sp,sp,-16
	sd	ra,8(sp)
	## TODO Your assembly code there
	la t0, mydata #load address mydata in t0
	ld t2, 0(t0) #load data t0 in t2 /compteur des espaces à afficher en début de ligne
	li t4, 0 #load value 0 in t2, /compteur des étoiles a afficher
	li t6, 0 #valeur à 0, sert de comparaison dans les if
	l: #initialisation des valeurs
		beq t2, t6, end #if t2 == 0 then jump to end, on a affiché toutes les étoiles
		addi t2, t2, -1 #t2-- on commente à n et descend vers 0 (pour les espaces)
		addi t4, t4, 1 #t4++ on commence à 0 et monte vers n (pour les étoiles)
		li t5, 0
		add t5, t5, t2 #on fait une copie de t2 pour boucler sur espace et afficher les espaces nécessaire (n-1)
		li t3, 0 #au début de la ligne, t3=0 correspond aux étoiles affichées sur la ligne
		j space
	space: #espace avant * pour aligner
		beq t2, t6, l2 #si t2==t6 on est à la dernière ligne, pas d'espace à mettre
		beq t5, t6, l2 #si t5==t6 on a déjà mit tous les espaces nécessaire
		addi t5, t5, -1 #t5-- un espace de moins à mettre
		li a0, 32 #load espace
		call print_char
		j space 
	l2:
		beq t4, t3, l3 #si t4==t3 on a print tous les *
		addi t3, t3, 1 #t3++ un * de plus a été affiché sur la ligne
		li a0, 42 #load *
		call print_char
		j space_between 
	space_between: #entre chaque * on met un espace
		beq t4, t3, l3 #si t4==t3 pas besoin d'ajouter un espace car on à déjà mit toutes les *
		li a0, 32 #load espace
		call print_char
		j l2 #l2 et space_between permet d'afficher les * séparées d'espace: * * * *
	l3:
		call newline #\n
		j l
	## END TODO /end of user assembly code
end:
	ld	ra,8(sp)
	addi	sp,sp,16
	ret
# Data comes here
	.section	.data
mydata:
	.dword 40
