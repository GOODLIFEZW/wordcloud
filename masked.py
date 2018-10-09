"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
wordcloud 'https://amueller.github.io/word_cloud/'
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


with open('test.txt','r',encoding='utf-8') as file:
    text=file.read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open("alice_mask.png"))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(
        # font_path="SourceHanSerifK-Light.otf",  # if Chinese, need to add
        background_color="white", 
        max_words=2000, 
        mask=alice_mask,
        stopwords=stopwords, # 设置需要屏蔽的词
        contour_width=3, 
        contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
# wc.to_file("alice.png")

image = wc.to_image()
image.show()

"""
# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')  # Module 'matplotlib.cm' has no 'gray' member
plt.axis("off")
plt.show()
"""
