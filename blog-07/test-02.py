# coding=utf-8
import json
import requests
import tqdm

#定义函数下载视频
def saveMp4(url, filename):
    res = requests.get(url, stream=True)
    file_size = int(res.headers['Content-Length'])
    num = 1
    num_size = 1024
    num_bars = int(file_size / num_size)

    with open(filename, 'wb') as fp:
        for num in tqdm.tqdm(
            res.iter_content(chunk_size = num_size),
            total = num_bars,
            unit = 'KB',
            desc = filename,
            leave = True
        ):
            fp.write(num)

#调用函数
url = "https://jsmov2.a.yximgs.com/bs2/newWatermark/MTQ5Mzk2MzMwMDg_zh_4.mp4"
filename = "test.mp4"
saveMp4(url, filename)
