#!/usr/bin/python
# -*- coding: latin-1 -*-
import Image, random, os, ImageDraw
import ImageFont
import ImageFilter
from time import gmtime, strftime


for i in range(5):
	
	im1 = Image.open("hachage_in.jpg")
	
	Crop_x1 = random.randint(0, im1.size[0]-1024)
	Crop_x2 = Crop_x1 + 1024
	Crop_y1 = random.randint(0, im1.size[1]-1024)
	Crop_y2 = Crop_y1 + 1024
	
	print Crop_x1
	print Crop_x2
	print Crop_y1
	print Crop_y2
	
	im1 = im1.crop((Crop_x1, Crop_y1, Crop_x2, Crop_y2))
	
	im1.save("test-"+strftime("%Y-%m-%d-%Hh%Mm%Ss", gmtime())+"-"+str(i)+".jpg",quality=100)
	
	
	im2 = im1.copy()
	im3 = Image.new("RGBA", (im1.size[0], im1.size[1]))

	im4 = Image.new("RGBA", (im1.size[0], im1.size[1]))
	im4.paste(im1, (0, 0, im1.size[0], im1.size[1]))
	Larg = im1.size[0]
	Haut = im1.size[1]
	
#   constitution de la liste des valeurs de hauteur ou vont s'opérer les hachures
#-----------------------------------------------------------------------------------
	def randHaut():
		return random.randint(0, im1.size[1])
	randomCoupeHauteur = [0, \
	randHaut(),randHaut(),randHaut(),randHaut(),\
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), im1.size[1]]

	# rangement des valeurs des plus petites au plus grandes
	randomCoupeHauteur.sort()

	# print randomCoupeHauteur


#   les hachures
#-----------------------------------------------------------------------------------
	def Hacheur(haut, bas) :
		n=0
		
		
		# randomListe = [(2560,1),(1280,2),(640,3),(320,5),(160,7),(80,12),(40,19),(20,31),(10,50)]			
		#	1 3 7 15 31 63 127 255 511 1023 2047
		
		
		
		# liste
		# 2 4 8 16 32 64 128 256 512 1024 2048
			
		while n<im1.size[0] :
		
			# largeur aléatoire de la zone copiée (suite basée sur le nombre d'or)
			#~ #randomListe = [(2560,1),(1280,2),(640,3),(320,5),(160,7),(80,12),(40,19),(20,31),(10,50)]			
			
			randomListe = [(1024,1),(512,2),(256,4),(128,8),(64,16),(32,32),(16,64),(8,128),(4,256)]
			randomFacteur = random.randint(0, 8)
			
			randomCopyLargFinal = randomListe[randomFacteur][0]
			repeat = randomListe[randomFacteur][1]
	
			# a une position aleatoire inferieure a la taille de l'image 
			randomCopyPosi = random.randint(0, (im1.size[0]-randomCopyLargFinal))
			
			cx1 = randomCopyPosi
			cx2 = randomCopyPosi + randomCopyLargFinal
			
	
		#repeat = randomFacteur - randomCopyLarg
			
			loop = 0
			
			
			# effets sur im3
			# import ImageFilter
			# ...
			
			im3 = im2.crop((cx1,haut,cx2,bas))
			
			draw = ImageDraw.Draw(im4)
			'''
			draw.line((cx1,haut,cx2,haut), fill="rgb(255,255,255)")
			draw.line((cx2,haut,cx2,bas), fill="rgb(255,255,255)")
			draw.line((cx2,bas,cx1,bas), fill="rgb(255,255,255)")
			draw.line((cx1,bas,cx1,haut), fill="rgb(255,255,255)")
			'''
				
				
			
			while loop<repeat:
				
				px1 = n
				px2 = n + randomCopyLargFinal
				
				
				draw = ImageDraw.Draw(im3)
				draw.line((0, 0, im3.size[0]-1, 0), fill="rgb(255,255,255)")
				draw.line((im3.size[0]-1, 0, im3.size[0]-1, im3.size[1]-1), fill="rgb(255,255,255)")
				
				
				im4.paste(im3, (px1, haut, px2, bas))
				
				n = n + randomCopyLargFinal
				loop = loop + 1
				
		#print n


#   les tranches horizontales intactes soulignées de blanc 
#-----------------------------------------------------------------------------------				
	def TrancheHorizontale() :
		# tirage au hasard de la bande copiee
		pos = random.randint(0, im1.size[1]-im1.size[1]/20)
		# copiage
		im5 = im2.crop((0,pos,im1.size[0],pos+im1.size[1]/20))
		
		# le soulignage en blanc
		draw = ImageDraw.Draw(im5)
		draw.line((0, im5.size[1]-1, im5.size[0], im5.size[1]-1), fill="white")
		draw.line((0, 0, im5.size[0], 0), fill="white")
		
		# collage	
		im4.paste(im5, (0,pos,im1.size[0],pos+im1.size[1]/20))

			
	 
	#Hacheur(0,	im1.size[1])
	
	
	Hacheur(0, randomCoupeHauteur[0])
	Hacheur(randomCoupeHauteur[0], randomCoupeHauteur[1])
	Hacheur(randomCoupeHauteur[1], randomCoupeHauteur[2])
	Hacheur(randomCoupeHauteur[2], randomCoupeHauteur[3])
	Hacheur(randomCoupeHauteur[3], randomCoupeHauteur[4])
	Hacheur(randomCoupeHauteur[4], randomCoupeHauteur[5])
	Hacheur(randomCoupeHauteur[5], randomCoupeHauteur[6])
	Hacheur(randomCoupeHauteur[6], randomCoupeHauteur[7])
	Hacheur(randomCoupeHauteur[7], randomCoupeHauteur[8])
	Hacheur(randomCoupeHauteur[8], randomCoupeHauteur[9])
	Hacheur(randomCoupeHauteur[9], randomCoupeHauteur[10])
	Hacheur(randomCoupeHauteur[10], randomCoupeHauteur[11])
	Hacheur(randomCoupeHauteur[11], randomCoupeHauteur[12])
	Hacheur(randomCoupeHauteur[12], randomCoupeHauteur[13])
	Hacheur(randomCoupeHauteur[13], randomCoupeHauteur[14])
	Hacheur(randomCoupeHauteur[14], im1.size[1])
	
	
	'''
	TrancheHorizontale()
	TrancheHorizontale()
	TrancheHorizontale()
	TrancheHorizontale()
	TrancheHorizontale()
	'''
	
	
	# TEXTE
	# draw = ImageDraw.Draw(im4)
	# use a truetype font
	#font = ImageFont.truetype("arial.ttf", 15)
	#im4.text((10, 25), "world", font=font)



	
	im4.save("hachures-out-"+strftime("%Y-%m-%d-%Hh%Mm%Ss", gmtime())+"-"+str(i)+".jpg",qualmity=100)
	
	#im4.save(str(i)+".jpg",quality=100)
