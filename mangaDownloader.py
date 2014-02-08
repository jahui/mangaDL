__author__ = 'Jonathan_Hui'

import bcolor
import urllib
import time
import sys
import getopt
import glob
import os
from subprocess import call


def imageURLFilter(source, target):
    #given a list of strings, returns the list of strings with the target string in it
    list = []
    for s in source:
        if target in s:
            if "src" in s:
            	list.append(s)
    return list


def getNum(num):

	if num < 10:
		return "0"+str(num)

	return str(num)


def imageGrab(urlstring, filename):
	#returns the image url grabbed or False if none

	#get file handle to web page
	response = urllib.urlopen(urlstring)
	#get web page contents as string
	html = response.read()

	#close file handle
	response.close()

	#get a list of src urls for images with .jpg extension
	images = imageURLFilter(html.split(), ".jpg")

	#no images found
	if not images:
		bcolor.printRed("No image to download.\n")
		return ""


	#404 for mangahere.com
	#if images[0][5:-1] == "http://m.mhcdn.net/media/images/404_img.jpg?v=297":
		#bcolor.printRed("Reached the end of the chapter.\n")
		#return ""


	#remove src=" and the trailing " part of the string
	#use as url and save to file named base.jpg
	urllib.urlretrieve(images[0][5:-1], filename + ".jpg")

	return images[0][5:-1]

def mangaChapter(start_url):
	#given the starting url, gets all the pages

	start_time = time.time()

	#mangahere note first page of every chapter is page/ with the nth page being page/n.html
	#mangapanda note first page of every chapter is page/ with the nth page being page/n
	if "mangahere" in start_url:
		url_end = ".html"
	elif "mangapanda" in start_url:
		url_end = ""
	else:
		sys.exit()


	
	curr_image = imageGrab(start_url, "01")
	last_image = ''

	if curr_image == "":
		count = 0
	else:
		count = 1

	#always loop
	while True:

		#set last image value as the current one
		last_image = curr_image

		#increment count
		count = count + 1

		#construct the next url
		next_url = start_url + str(count) + url_end

		#get the number as the string
		numString = getNum(count)

		#get the image url we just 
		curr_image = imageGrab(next_url, numString)
		print next_url

		if not curr_image:
			break

		if curr_image == last_image:
			break


	etime = time.time() - start_time
	bcolor.printGreen("Elapsed time: " + str(etime) +"\nFiles downloaded: " + str(count) +"\n")

def getStart(manga, chapter):
	base_url = "www.mangapanda.com"
	manga_name = ''


	#url format dependant on manga name. mangapanda keeps everything same except spaces are -
	if manga == "goh":
		#short cut for god of highschool
		manga_name = "the-god-of-highschool"
	else:
		manga_name = manga.replace(" ", "-")

	return base_url + '/' + manga_name + '/' + str(chapter) + '/'


def main():

	try:
		opts, args = getopt.getopt(argv,"hs:m:c:")
	except getopt.GetoptError:
		print 'mangaDownloader.py -m <manga> -c <chapter>'
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print 'mangaDownloader.py -s <starting_url>'
			sys.exit()
		#elif opt == "-s":
			#start_url = arg
		elif opt == "-m":
			manga = arg
		elif opt == "-c":
			chapter = arg

	start_url = getStart(manga, chapter)

	mangaChapter(start_url)
	
	os.mkdir(manga+chapter)
	
	#for each file ending in .jpg in the current directory move it to the appropriate directory
	for entry in os.listdir('.'):
		if entry.endswith(".jpg"):
			os.rename("./"+entry, "./"+manga+chapter+"/"+entry)

	
	call(["tar", "-czf", manga+chapter+".tar.gz", manga+chapter])

	#remove the originals
	call(["rm", "-r", "./"+manga+chapter])



if __name__ == '__main__':
	main()


