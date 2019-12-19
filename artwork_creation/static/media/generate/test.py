# encoding=utf-8
import os
from os.path import sep, join
import glob
import tqdm
import time
import shutil

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

def check_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

from_path = "repeat_h_10"
to_path = "repeat_h_10_numstroke_15_hkust_sea_2"

while True:
    check_path(to_path)
    from_image_list = list_image(from_path)
    sort_list = sorted([int(name.split(sep)[-1].split('.')[0].split('+')[1]) for name in from_image_list])
    for image_index in sort_list:
        image_name = 'gen+' + str(image_index) + '.png'
        from_image_path = join(from_path, image_name)
        to_image_path = join(to_path, image_name)
        try:
            shutil.copyfile(from_image_path, to_image_path)
            time.sleep(5)
        except Exception as e:
            continue
        print(image_index)

    shutil.rmtree(to_path)
    os.mkdir(to_path)



