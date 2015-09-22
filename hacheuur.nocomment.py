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
import ImageEnhance

im1 = Image.open(str(sys.argv[1]))
im2 = im1.copy()
allongement = 1
im3 = Image.new("RGBA",(im1.size[0], im1.size[1]))
im4 = Image.new("RGBA",(im1.size[0]*allongement, im1.size[1]))
Larg = im1.size[0]
Haut = im1.size[1]

for i in range(50):
	def randHaut(): return random.randint(0, im1.size[1])
	randomCoupeHauteur = [0, \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	randHaut(),randHaut(),randHaut(),randHaut(),randHaut(), \
	im1.size[1]]
	randomCoupeHauteur.sort()
	liste = []

	def Hacheur(haut, bas) :
		n=0
		while n<im4.size[0] :
			randomListe = [(5120,1),(2560,1),(1280,2),(640,4),(320,8),(320,3),(160,12),(160,6),(120,8),(80,24),(40,16),(10,32),(5,64),(3,24)]
			choix = 0
			randomFacteur = random.randint(0, len(randomListe)-1)
			randomCopyLargFinal = randomListe[randomFacteur][0]			
			repeat = randomListe[randomFacteur][1]
			randomCopyPosi = random.randint(0, (im1.size[0]-randomCopyLargFinal))
			cx1 = randomCopyPosi
			cx2 = randomCopyPosi + randomCopyLargFinal
			im3 = im2.crop((cx1,haut,cx2,bas))
			draw = ImageDraw.Draw(im4)		
			loop = 0
			while loop<repeat:	
				px1 = n
				px2 = n + randomCopyLargFinal
				draw = ImageDraw.Draw(im3)
				im4.paste(im3, (px1, haut, px2, bas))
				n = n + randomCopyLargFinal
				loop = loop + 1

	def TrancheHorizontale() :
		pos = random.randint(0, im1.size[1]-im1.size[1]/20)
		im5 = im2.crop((0,pos,im1.size[0],pos+im1.size[1]/20))
		draw = ImageDraw.Draw(im5)
		draw.line((0, im5.size[1]-1, im5.size[0], im5.size[1]-1), fill="black")
		draw.line((0, 1, im5.size[0], 1), fill="black")
		im4.paste(im5, (0,pos,im1.size[0],pos+im1.size[1]/20))
		
	for i in range(len(randomCoupeHauteur)-1):
		Hacheur(randomCoupeHauteur[i], randomCoupeHauteur[i+1])
	
	scriptpy = str(sys.argv[1])
	script = scriptpy[:-3]
	im4.save(script+"."+strftime("%Y%m%d-%Hh%Mm%Ss", gmtime())+".jpg",'JPEG', quality=100)
	
