# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from time import strftime
from PIL import Image
import os
import glob
from os.path import sep
# import cv2
import uuid
import base64
from io import BytesIO
# from __init__ import network_sea, network_sky
# from chinaink.SegNet import segnet
# import SegNet
# import chinaink.test
# import chinaink.SegNet
# from chinaink.SegNet_ import test
# from django.views.decorators.csrf import csrf_exempt
# import pandas
# import tensorflow as tf
from chinaink.utils import list_image, mask_blank_


# Create your views here.
#请求主页
def index(request):
    return render(request,'chinaink/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

# @csrf_exempt
def upload(request):

    if request.method == "POST":
        # 获取用户ID
        # id = request.POST['id']
        resolution = request.POST.getlist('resolution')[0]
        # resolution: ['low']
        # print('resolution:', resolution)
        upload_image_path = request.POST.get('pic_default')
        random_ = uuid.uuid1()

        # 预设图片：做segment，然后保存分割后的图片到segment/文件夹
        if upload_image_path.startswith('/static'):
            image_name = upload_image_path.split(sep)[-1]
            image_name = resolution + "_" + image_name.replace('.jpg','') + "_" + str(random_) + '.png'

            # 处理segment
            mask_blank_(settings.BASE_DIR, upload_image_path, resolution, image_name)
            # return render(request, "chinaink/display.html", {'data': upload_image_path})

        # 自定义的图片：保存到upload/文件夹下，检查文件名重复，写入到upload_image_list.txt
        else:
            # 获取上传的图片
            img_data = request.FILES['pic']

            img = Image.open(img_data)
            image_name = img_data.name.split('.')[0][:10]
            image_name = resolution + "_" + image_name.replace('_','') + "_" + str(random_) + '.png'

            # upload_image_path_list = list_image(settings.MEDIA_ROOT)
            # upload_image_name_list = [path.split(sep)[-1] for path in upload_image_path_list]
            # if image_name in upload_image_name_list:
            #     base = image_name.split('.')[0]  
            #     suffix = image_name.split('.')[1]  
            #     image_name = base + str(random_) + '.' + suffix

            image_save_path = os.path.join(settings.MEDIA_ROOT, image_name)

            try:
                img.save(image_save_path)
                # network_sea = segnet(input_img_path='temp.png', save_img_path='temp.png')
                # network_sea.generate()
                # network_sky = segnet(input_img_path='temp.png', save_img_path=image_save_path, category='sky')
                # network_sky.generate()

                # 这也是个请求，"GET /static/media/9408514_332f2cfe31_b.jpg HTTP/1.1" 404 1717。所以nginx.conf里需要配置static静态文件请求
                # return HttpResponse('<img src="/static/media/%s"/>'%img_data.name)
                upload_image_path = image_save_path.replace(settings.BASE_DIR, '')
                # print("content image path:", upload_image_path)
                # return render(request, 'chinaink/display.html', {'data': upload_image_path })
            except Exception as e:
                print('自定义图片保存出错！')
                return HttpResponse('图片上传出错，请更换图片再试！')

        upload_image_list_path = os.path.join(settings.MEDIA_ROOT.replace("upload",""), "upload_image_list.txt")        
        f = open(upload_image_list_path, 'w', encoding="utf-8")
        f.write(image_name + "||" + resolution + "\n")
        f.close()

        return render(request, "chinaink/display.html", {'data': upload_image_path})

def Captcha(request):
    f = open(os.path.join(settings.MEDIA_ROOT.replace("upload",""), "upload_image_list.txt"), 'r', encoding="utf-8")
    lines = f.readlines() #读取所有行
    last_line = lines[-1] #取最后一行  
    image_dir = os.path.join(settings.MEDIA_GEN, last_line.replace('\n','').split('||')[0].split('.')[0][:10])
    # print(image_dir)

    gen_image_list = list_image(image_dir)
    print('已生成%d张图片' %len(gen_image_list))
    l = sorted([int(name.split(sep)[-1].split('.')[0].split('+')[1]) for name in gen_image_list])
    current_epoch = str(l[-1])
    image_name = "gen+" + current_epoch + ".png"
    image_path = os.path.join(image_dir, image_name)
    # image_path = os.path.join(settings.MEDIA_GEN, "gen+0.png")
    # Method 1 
    img = Image.open(image_path)
    buf = BytesIO()  # 构建一个输入输出流
    img.save(buf, "jpeg")     # 将图片保存到输入输出流,也就是内存中,如果是opencv加载的图片需要用其他的函数转为byte
    bur_str = buf.getvalue()    # 获得输入输出流里面的内容
    # print(str(base64.b64encode(bur_str)))
    data = str(base64.b64encode(bur_str))[1:].strip("'")
    success = 0
    # if current_epoch == "250":
    #     success = 1
    # ret = {"status":success, "data":data}
    # import json

    return HttpResponse(data, success)
    # return HttpResponse(json.dumps(ret))

    # Method 2
    # ret = {'status': True, 'data': image_path.replace(settings.BASE_DIR, '')}
    # import json
    # return HttpResponse(json.dumps(ret))

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    print('a:',a)
    return HttpResponse(str(a+b))

def cal(request):
    n1 = int(request.GET.get("n1"))
    n2 = int(request.GET.get("n2"))
    ret = n1 + n2
    return HttpResponse(ret)



    