import mangaDownloader
import bcolor


#test url1 404
testurl1 = "http://www.mangapanda.com/shingeki-no-kyojin/53/48"

image = mangaDownloader.imageGrab(testurl1, "test1")

if not image:
	bcolor.printGreen("Test 1 (404 handling) success!\n")
else:
	bcolor.printRed("Test 1 (404 handling) failed!\n")

#test url2 mangapanda
testurl2 = "http://www.mangapanda.com/shingeki-no-kyojin/53/"

image = mangaDownloader.imageGrab(testurl2, "test2")

if image == "http://i13.mangapanda.com/shingeki-no-kyojin/53/shingeki-no-kyojin-4699239.jpg":
	bcolor.printGreen("Test 2 (mangapanda single image download) success!\n")
else:
	bcolor.printRed("Test 2 (mangapanda single image download) failed!\n")