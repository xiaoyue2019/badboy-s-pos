import aircv
from img_synthesis import Picture_Synthesis

def matchAndreplace(img_father,
                    img_sun,
                    img_replace,
                    img_save):
    '''
    img_father 母图，替换模板
    img_sun 子图，需要找的图
    img_replace 孙子图，用来替换的图
    img_save 玄孙图，结果保存的地方
    '''
    img1=aircv.imread(img_father)
    img2=aircv.imread(img_sun)
    try:    
        coo=aircv.find_template(img1,img2,threshold=0.85)['rectangle'][0]
    except Exception:
        return '[-]替换失败!'
    Picture_Synthesis(img_father,img_replace,img_save,coo)

    try:
        img1=aircv.imread(img_save)
        coo=aircv.find_template(img1,img2)['rectangle'][0]
        matchAndreplace(img_save,img_sun,img_replace,img_save)
    except Exception:
        pass
    return '[+]替换成功！'




if __name__ == "__main__":
    print(matchAndreplace('1.png','2.png','3.png','1.png'))
