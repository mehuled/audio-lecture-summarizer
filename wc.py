from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'summary.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg

wc = WordCloud(background_color="black", width=1280, height=720, prefer_horizontal=0.8, font_path='Aller_Rg.ttf', max_words=50, stopwords=STOPWORDS.add("said"))

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "word_cloud.png"))

# show
plt.imshow(wc)
plt.axis("off")
plt.show()
