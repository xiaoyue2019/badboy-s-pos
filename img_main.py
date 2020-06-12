import os,re
from img_matchAndreplace import matchAndreplace

for i in os.listdir('../'):
    if "image" in i:
        matchAndreplace('../'+i,'2.png','3.png','../'+i)
