#!/usr/bin/python
# coding: utf-8

import sys
import Image
import random
import os
import ImageDraw
import ImageFont
import ImageFilter
from time import gmtime, strftime
import time
import ImageEnhance
import pickle


allongement = 4
im1 = Image.open(str(sys.argv[1]))
im2 = Image.new("RGBA",(im1.size[0], im1.size[1]))
im3 = Image.new("RGBA",(im1.size[0], im1.size[1]))
im4 = Image.new("RGBA",(im1.size[0], im1.size[1]))
im5 = Image.new("RGBA",(im1.size[0], im1.size[1]))
im6 = Image.new("RGBA",(im1.size[0]*allongement, im1.size[1]))

Larg = im1.size[0]
Haut = im1.size[1]
loadfile = False
	
def randHaut():
	return random.randint(0, im1.size[1]/8)*8


randomCoupeHauteur = [0, \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
randHaut(),randHaut(),randHaut(),randHaut(), \
im1.size[1]]
randomCoupeHauteur.sort()
	

def Hacheur(haut, bas) :
	n = 0
	i = 0
	while n<im6.size[0] :
		i+=1
		loop = 0

		proportions = [\
		(2,2),(2,4),(2,5),(2,8),(2,16),(2,32),\
		(4,4),(4,5),(4,8),(4,16),(4,32),(4,64),\
		(8,3),(8,5),(8,8),(8,16),(8,32),\
		(16,2),(16,3),(16,4),(16,5),(16,8),(16,16),(16,32),\
		(32,3),(32,5),(32,8),(32,16),(32,32),\
		(64,3),(64,4),(64,8),(64,16),\
		(128,1),(128,2),(128,4),(128,8),\
		(256,1),(256,2),(256,4),\
		(512,1),(512,2),\
		(768,1),(768,2),\
		(1024,1),(1024,2),\
		(2048,1),\
		(3072,1)]

		choix_rnd = random.randint(0, len(proportions)-1)
		largeur = proportions[choix_rnd][0]
		randomCopyPosi = random.randint(0, (im1.size[0]-largeur))
		largeur = proportions[choix_rnd][0]			
		repeat = proportions[choix_rnd][1]
		
		pixelSizeList = [1,1,1,1,1,1,1,1,1,16,32,64]
		#pixelSizeList = [1,5,25,125]
		pixelSizeIndex = random.randint(0,len(pixelSizeList)-1)
		pixelSize = pixelSizeList[pixelSizeIndex]
		
		hauteur = bas-haut
		cropfinal = [largeur,hauteur]
		
		if largeur % pixelSize != 0:
			croop = int(largeur / pixelSize)
			largeur = (croop + 1 ) * pixelSize
			
		if  hauteur % pixelSize != 0:
			croop2 = int(hauteur / pixelSize)
			hauteur = (croop2 + 1 ) * pixelSize
		
		im2 = im1.crop((randomCopyPosi,haut,randomCopyPosi+largeur,haut+hauteur))
		im3 = im2.resize((im2.size[0]/pixelSize, im2.size[1]/pixelSize), Image.NEAREST)
		im4 = im3.resize((im3.size[0]*pixelSize, im3.size[1]*pixelSize), Image.NEAREST)
		im5 = im4.crop((0,0,cropfinal[0],cropfinal[1]))
		
		while loop<repeat:
			px1 = n
			px2 = n + cropfinal[0]
			'''
			draw = ImageDraw.Draw(im5)
			draw.line((0, 0, 4, 0), fill="rgb(255,255,255)")
			draw.line((0, 0, 0, 4), fill="rgb(255,255,255)")
			'''
			im6.paste(im5, (px1, haut, px2, bas))
			
			n = n + cropfinal[0]
			loop = loop + 1


for j in range(len(randomCoupeHauteur)-1):
	Hacheur(randomCoupeHauteur[j], randomCoupeHauteur[j+1])

scriptpy = str(sys.argv[1])
script = scriptpy[:-3]
n = "1.1"
#TODO : inclure version du script + taille finale image
im6.save(script+"."+n+"_"+strftime("%Y%m%d-%Hh%Mm%Ss", gmtime())+".png",'PNG', quality=100)
