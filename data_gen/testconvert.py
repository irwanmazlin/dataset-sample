# from PIL import Image
# import os

# # path = r'/home/irwan/models/research/tf2-object-detection-api-tutorial/data/raccoon_data/train/images'


# # path123 = path +'/' + file

# directory = r'/home/irwan/models/research/tf2-object-detection-api-tutorial/data/raccoon_data/train/images'
# c=1
# for filename in os.listdir(directory):
#     if filename.endswith(".png"):

#         path123 = directory +'/' + filename
#         print(path123)
#         # print(filename)
#         im = Image.open(path123)
#         name='img'+str(c)+'.png'
#         print(name)
#         rgb_im = im.convert('RGB')
#         rgb_im.save(name)
#         c+=1
#         print(os.path.join(directory, filename))
#         continue
#     else:
#         continue



# from glob import glob
# files_list = [j for i in [glob('../data/raccoon_data/train/images/'+e) for e in ['*jpg', '*png']] for j in i]
# print()



from PIL import Image 
import os 

# path = r'/home/irwan/models/research/tf2-object-detection-api-tutorial/data/raccoon_data/train/images'
path = r'/home/irwan/models/research/tf2-object-detection-api-tutorial/data/raccoon_data/test/images'

for file in os.listdir(path): 
    if file.endswith(".jpg"): 
        img = Image.open(path + '/' + file)
        rgb_im = img.convert('RGB')
        file_name, file_ext = os.path.splitext(file)

        print(file_name)
        rgb_im.save(path +'/{}.png'.format(file_name))
        # print(path +'/{}.jpg'.format(file_name))