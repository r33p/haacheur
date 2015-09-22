#!/usr/bin/python
# coding: utf-8

# haacheuur 0.24
# port industriel de port la nouvelle - couleur - 60cm*30cm
# image source : pln.jpg
# image rendue : pln..20150910-11h59m53s.jpg


import sys
import Image
import random
import os
import ImageDraw
import ImageFont
import ImageFilter
from time import gmtime, strftime
# modifs du 30/10/2013
import ImageEnhance

#ouvertrure de l'image source et conversion en mode 1bit
#im1 = Image.open(str(sys.argv[1])).convert('1')
im1 = Image.open(str(sys.argv[1]))
im2 = im1.copy()
#im3 = Image.new("1", (im1.size[0], im1.size[1]))
#im4 = Image.new("1", (im1.size[0]*3, im1.size[1]))

#rapport d'allongement de la nouvelle image par rapport à la largeur de l'image originale
allongement = 1

im3 = Image.new("RGBA",(im1.size[0], im1.size[1]))
im4 = Image.new("RGBA",(im1.size[0]*allongement, im1.size[1]))

Larg = im1.size[0]
Haut = im1.size[1]

for i in range(50):
	
	# nombre aleatoire compris dans les limites de l'image
	def randHaut(): return random.randint(0, im1.size[1])
		
	# constitution de la liste des tranches horizontales
	# genre comme si qu'on avait un 16 pistes :)
	randomCoupeHauteur = [0, \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	im1.size[1]]

	# rangement des valeurs des plus petites au plus grandes
	randomCoupeHauteur.sort()
	
	# DEBUG
	liste = []

	# les hachures
	def Hacheur(haut, bas) :
		n=0
		while n<im4.size[0] :
		
			# constitution d'une liste de dimensions et de repetitions
			#dimen FAAAAT
			#randomListe = [(10240,1),(5120,1),(2560,1),(1280,2),(640,4),(320,8),(320,3),(160,12),(160,6),(120,8),(80,24),(40,16),(20,32),(20,16),(10,32),(10,16),(5,64)]
			#dimen FUZITU
			
			#PLN back
			#randomListe = [(2560,1),(1280,2),(640,4),(320,8),(320,3),(160,12),(160,6),(120,8),(80,24),(40,16),(20,24),(20,16),(10,32),(10,16),(5,64),(2,64),(1,64),(1,16)]
			
			#PLN recursif
			#randomListe = [(2560,1),(1280,2),(640,4),(320,8),(320,3),(160,12),(160,6),(120,8),(80,24),(40,16),(20,24),(20,16),(10,32),(10,16),(5,64)]
			randomListe = [(5120,1),(2560,1),(1280,2),(640,4),(320,8),(320,3),(160,12),(160,6),(120,8),(80,24),(40,16),(10,32),(5,64),(3,24)]
			
			#dimen BLOG CUMULONIMBUS
			#randomListe = [(320,8),(320,3),(160,12),(160,6),(120,8),(80,24),(40,16),(20,32),(20,16),(10,32),(10,16),(5,64)]
			# repeter ce qui suit 2 ou 3 fois pour realiser non pas
			# un sample, mais carrement ue sequence
# 8>< ------------------------------------------------------------------			
			# tirage au sort
			#randomFacteur = random.randint(0, len(randomListe)*3)
			choix = 0
			
			# DEBUG	
			#print len(randomListe)*3
			
			# ponderation du tirage au sort
			randomFacteur = random.randint(0, len(randomListe)-1)
			
			# DEBUG
			#liste.append(choix)
			
			# assignation des valeurs (paires) finales choisies
			randomCopyLargFinal = randomListe[randomFacteur][0]			
			repeat = randomListe[randomFacteur][1]
	
			# positionnement de la copie, aleatoirement, entre 0 et la largeur totale de l'image 
			randomCopyPosi = random.randint(0, (im1.size[0]-randomCopyLargFinal))

			cx1 = randomCopyPosi
			cx2 = randomCopyPosi + randomCopyLargFinal
			# decoupage du sample
			im3 = im2.crop((cx1,haut,cx2,bas))
# 8>< ------------------------------------------------------------------
				
			draw = ImageDraw.Draw(im4)		
			loop = 0
			
			#collage, n fois, du sample
			while loop<repeat:	
				px1 = n
				px2 = n + randomCopyLargFinal
				
				draw = ImageDraw.Draw(im3)
				
				#lignes noires 1px autour
				#draw.line((0, 0, im3.size[0]-1, 0), fill="rgb(255,255,255)")
				#draw.line((im3.size[0]-1, 0, im3.size[0]-1, im3.size[1]-1), fill="rgb(255,255,255)")
				
				im4.paste(im3, (px1, haut, px2, bas))
				
				n = n + randomCopyLargFinal
				loop = loop + 1

	# les tranches horizontales intactes soulignees de blanc 				
	def TrancheHorizontale() :
		# tirage au hasard de la bande copiee
		pos = random.randint(0, im1.size[1]-im1.size[1]/20)
		# copiage
		im5 = im2.crop((0,pos,im1.size[0],pos+im1.size[1]/20))
		
		# le soulignage en blanc
		draw = ImageDraw.Draw(im5)
		draw.line((0, im5.size[1]-1, im5.size[0], im5.size[1]-1), fill="black")
		draw.line((0, 1, im5.size[0], 1), fill="black")
		
		# collage	
		im4.paste(im5, (0,pos,im1.size[0],pos+im1.size[1]/20))

	# HAACHEUUR
	for i in range(len(randomCoupeHauteur)-1):
		Hacheur(randomCoupeHauteur[i], randomCoupeHauteur[i+1])
	
	# DEBUG
	#print liste
	#print sorted(set(liste),key=liste.count)
			
	
	# CTRL + S
	#chemin du script
	#scriptpy = sys.argv[0]
	
	#chemin de l'image : str(sys.argv[1])
	scriptpy = str(sys.argv[1])
	
	
	script = scriptpy[:-3]
	
	im4.save(script+"."+strftime("%Y%m%d-%Hh%Mm%Ss", gmtime())+".jpg",'JPEG', quality=100)
	
