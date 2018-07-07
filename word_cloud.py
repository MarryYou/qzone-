import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
text = ''
with open('word.txt', 'r', encoding='utf-8') as fin:
    for line in fin.readlines():
        text += ' '.join(jieba.cut(line))
background_Image = plt.imread('bg_1.jpg')
print('加载图片成功')
wc = WordCloud(
    background_color='#fff',
    mask=background_Image,
    font_path='C:\Windows\Fonts\STZHONGS.TTF',
    max_words=1000000,
    stopwords=STOPWORDS,
    max_font_size=100,
    min_font_size=5,
    random_state=30
)
wc.generate_from_text(text)
print('加载文本')
img_colors = ImageColorGenerator(background_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
d = path.dirname(__file__)
wc.to_file(path.join(d, 'ciyun2.jpg'))
print('次云生成成功')
