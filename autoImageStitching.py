
# importing the required libraries:
import cv2
import os

# specifying the main folder under which we have our images:
mainFolder = 'Images'
# getting the list of sub-folders under the main folder:
myFolders = os.listdir(mainFolder)
print(myFolders)

# iterating over the sub-folders and retrieving our images.

for folder in myFolders:
    path = mainFolder + '/' + folder
    #print(path)
    images = []
    myList = os.listdir(path)
    print(f'Total number of images detected {len(myList)}.')
    for imgNum in myList:
        currentImg = cv2.imread(f'{path}/{imgNum}')
        currentImg = cv2.resize(currentImg, (0,0), None, 0.2,0.2)
        images.append(currentImg)

    #print(len(images))
    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if (status == cv2.Stitcher_OK):
        print('Panorama Generated')
        cv2.imshow(folder, result)
        cv2.waitKey(1)
    else:
        print('Panorama Generation Failed.')

#cv2.waitKey(0)


