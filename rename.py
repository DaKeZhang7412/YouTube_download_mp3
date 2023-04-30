
# import required module
import os
# assign directory
directory = 'H:\\Audio book\\锦衣春秋 王更新演播\\'
# change current directory
os.chdir(directory) 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    base = os.path.splitext(filename)[0]    
    os.rename(filename, base + '.mp3')