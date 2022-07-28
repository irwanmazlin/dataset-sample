import os

filelist = [ f for f in os.listdir('/home/irwan/models/research/tf2-object-detection-api-tutorial/data/raccoon_data/test/images') if f.endswith(".jpg") ]
for f in filelist:
	print(f)
	os.remove(os.path.join('/home/irwan/models/research/tf2-object-detection-api-tutorial/data/raccoon_data/test/images', f))