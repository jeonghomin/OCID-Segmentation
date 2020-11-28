import os



# 원본 데이터셋 폴더 접근.

input_path_1 = r'/home/ailab/Desktop/mjh/OCID/Train_set/label'

file_list_input_1 = os.listdir(input_path_1)



# 파일_네임_번호

idx = 0

# 원본 파일 순회하며 -> 파일 리네임.

for i in file_list_input_1:

    idx += 1

    os.rename(r'/home/ailab/Desktop/mjh/OCID/Train_set/label/{0}'.format(i),r'/home/ailab/Desktop/mjh/OCID/Train_set/label/{0:06d}.png'.format(idx))