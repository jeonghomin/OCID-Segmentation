from PIL import Image
import numpy as np
#image=Image.open('Train_set/img/mixed_kitchen_0_000044.right.seg.png')
f = open('/home/ailab/workspace/mjh/label.txt','r')
data = f.read()
print(data)
f.close()


import os
import shutil as sh
import re



# selected_dir = 'Train_set/label'
# # image=Image.open('Train_set/label/mixed_kitchen_0_000044.right.segjpg')
# j = 0
# # name = input("type what you want to search for: ")
#
# sorted_list = sorted(os.listdir(selected_dir))
#
# # path = os.path.join(selected_dir,sorted_list[0])
#
#
# # filenames = os.listdir(os.path.join(selected_dir,sorted_list[j]))
# # path = os.path.join(selected_dir,sorted_list[j])
# for filename in sorted_list:
#     full_names = os.path.join(selected_dir, filename)
#
#     f.write(full_names + '\n')
#     # if re.search('seg', os.path.splitext(filename)[0]):
#     # if os.path.splitext(filename)[1].lower() == '.jpg':
#
#     # os.rename(full_names,path+'/'+'_'.join(full_names.split("/")[8:]))
#     # sh.move(full_names,'/home/ailab/Desktop/mjh/OCID/Train_set/label')
#     # print('_'.join(full_names.split("/")[8:]))