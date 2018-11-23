# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:42:13 2018

@author: Python
"""

import logging
import sys

# 获取logger的实例
logger = logging.getLogger("testLog")

# 指定logger的格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# 创建具体的日志handler
# 文件日志,终端日志
file_handler = logging.FileHandler("testLog.log")
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
# 设置日志的级别
#高于等于这个默认级别的日志才会被写
logger.setLevel(logging.DEBUG)

# 把日志的handler添加到logger实例中
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 写日志
logger.error("Test Error log")
logger.info("Test info log")
logger.debug("Test debug log")

# 清空日志handler
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)











