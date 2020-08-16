from PIL import Image
import os

'''
img=Image.open('C:\\Users\\NITESH\Documents\\imageProcessing\\code\\image\\api.png')
img.show()

'''



def greyscale():
    for f in os.listdir('image'):
        if f.endswith('PNG'):
            path = 'C:\\Users\\NITESH\Documents\\imageProcessing\\code\\image\\'
            path = path + f
            save_path = "C:\\Users\\NITESH\Documents\\imageProcessing\\code\\convert\\" + f
            img = Image.open(path).convert('L').save(save_path)


def convert_ext():
    for f in os.listdir('image'):
        if f.endswith('PNG'):

            path = 'C:\\Users\\NITESH\Documents\\imageProcessing\\code\\image\\'
            f1=f.split('.')

            f1[0]=f1[0]+'.png'
            path = path + f
            save_path = "C:\\Users\\NITESH\Documents\\imageProcessing\\code\\convert\\" + f1[0]
            img = Image.open(path).save(save_path)
    return 'done .'


msg=convert_ext()
print(msg)







