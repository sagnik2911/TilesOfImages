# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import image_slicer
import os,shutil

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imageFolderName = input("Enter the name of the Folder: \n")
    images = os.listdir(imageFolderName)
    imagesTilesFolder = imageFolderName + " Train"
    if os.path.exists(imagesTilesFolder):
        shutil.rmtree(imagesTilesFolder)
    os.mkdir(imagesTilesFolder)
    for image in images:
        if (image.endswith('.tif') or image.endswith('.tiff')) and "C1" in image:
            os.chdir(imageFolderName)
            tiles = image_slicer.slice(image, 16, save=False)
            os.chdir('..')
            image_slicer.save_tiles(tiles, directory=imagesTilesFolder, prefix=image)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
