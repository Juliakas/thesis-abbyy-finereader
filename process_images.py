import os

images = os.listdir('../data/icdar2013/filtered_images/')
for img in images:
    full_img_path = '../data/icdar2013/filtered_images/' + img
    os.system(
        f'python3 process.py -xml {full_img_path} results/{img[:-4]}.xml')
