# encoding=utf-8
import os
import shutil
import cv2
import numpy as np
import glob
from os.path import sep, join

def list_image(target_dir, **kw):
    if str(target_dir)[-1] != sep:
        target_dir += sep
    print(target_dir)
    listglob = list()
    if "image_format" in kw:
        listglob += glob.glob(target_dir + "*." + kw['image_format'])
    else:
        listglob += glob.glob(target_dir + "*.jpeg")
        listglob += glob.glob(target_dir + "*.jpg")
        listglob += glob.glob(target_dir + "*.png")
    # 满足条件时继续往下执行
    # assert len(listglob) != 0
    return listglob

def mask_blank_(base_path, image_path, resolution, saved_image_name):
    image_path = base_path + image_path
    image_name = image_path.split(sep)[-1]

    mask_blank(base_path, image_path, 'sea', image_path.replace("default","temp"))
    mask_blank(base_path, image_path.replace("default","temp"), 'sky', image_path.replace("default", "segment").replace(image_name, saved_image_name))

def mask_blank(base_path, image_path, mode, saved_path):
  mask_img_path = image_path.replace('.jpg', '-'+str(mode)+'-msk.png').replace("temp","default")
  # /Users/xufeng/Code/Demo/Django/artwork_creation/static/media/default/001-sky-msk.png
  print('mask_img_path:',mask_img_path)
  if mode == 'sea':
    target_path = join(base_path, 'FileMonitor/seg/predict_sea.png')
    shutil.copy(mask_img_path, target_path)
  elif(mode == 'sky'):
    target_path = join(base_path, 'FileMonitor/seg/predict_sky.png')
    shutil.copy(mask_img_path, target_path)

  generate_img = cv2.imread(image_path) 
  # print('generate shape:', generate_img.shape)

  mask_img = cv2.imread(mask_img_path, cv2.IMREAD_GRAYSCALE) 
  mask_img = cv2.resize(mask_img, (int(generate_img.shape[1]), int(generate_img.shape[0])), interpolation=cv2.INTER_CUBIC)
  mask_img = cv2.medianBlur(mask_img, 9)

  # print('segment shape:', mask_img.shape)
  array_none_zero = np.nonzero(mask_img)

  index_list = []
  for i, j in zip(array_none_zero[0], array_none_zero[1]):
      index_list.append((i, j))
  index_list = np.array(index_list)

  # 三维中的每一维都要将指定index设置成255
  for index in index_list:
      h, w = index
      generate_img[h,w,0] = 255 #193 # 255
      generate_img[h,w,1] = 255 #210 # 255
      generate_img[h,w,2] = 255 #240 # 255

  # generate_img = cv2.medianBlur(generate_img, 9)
  cv2.imwrite(saved_path, generate_img)