# Chinese-Painting-Generator
Chinese Painting Generator

## Set up
Python3.5 + Django + Nginx + Tensorflow + Keras
详见requirements.txt
pip install -r requirements.txt

## RUN
1. 启动Nginx: sudo nginx
2. 启动uwsgi: uwsgi --ini uwsgi.ini
3. 启动两个文件监听程序。
目录：/FileMonitor
python run.py
目录：/FileMonitor/seg
python run_seg.py

## Usage
1. 选择上传自己的山水照片或者使用预设照片
2. 选择分辨率
3. 点击上传