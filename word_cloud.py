import jieba
from PIL import Image
import numpy as np
from wordcloud import WordCloud

def get_wordcloud():
        with open('test.txt', 'r', encoding='utf-8') as file:
            text = file.read()  # 加载数据
            words = ' '.join(jieba.cut(text, cut_all=True))  # 采用结巴全分词模式
            image = np.array(Image.open('1.jpg'))  # 背景图片
            # 设置词云样式
            wc = WordCloud(
                font_path='SourceHanSerifK-Light.otf', # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
                background_color='white', 
                mask=image,
                max_font_size=100, 
                max_words=2000, # 最多显示多少个字
                random_state=20 #设置有多种配色方案
            )
            wc.generate(words)  # 生成词云
            imageobj = wc.to_image()
            imageobj.show()

get_wordcloud()