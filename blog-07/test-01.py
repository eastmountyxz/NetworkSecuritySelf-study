# -*- coding: utf-8 -*-
import time
from tqdm import tqdm  

for i in tqdm(range(100)):  
    time.sleep(0.01)

#设置描述
pbar = tqdm(["a", "b", "c", "d"])  
for char in pbar:  
    # 设置描述
    pbar.set_description("Processing %s" % char)
    time.sleep(1)
