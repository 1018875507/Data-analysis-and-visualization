import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data1.xlsx',sheet_name='组件1')
# 创建一个字典，将类型作为键，大小作为值
word_freq = dict(zip(df['用户名称'].astype(str), df['访问次数']))
# 创建词云对象，并将字典传递给generate_from_frequencies方法
wordcloud = WordCloud(width=800, height=400, background_color='white',font_path='C:/Windows/Fonts/msyh.ttc').generate_from_frequencies(word_freq)
wordcloud.to_file(r"用户.png")
# 绘制词云图
plt.figure(figsize=(100, 50))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.title('词云示例')
plt.show()'''

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data1.xlsx',sheet_name='组件')
plt.bar(df['访问平台'], df['用户名称'])
plt.title('用户访问平台')
plt.savefig('访问平台.png')
plt.show()'''

df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data1.xlsx',sheet_name='组件2')
plt.pie(df['用户ID'], labels=df['性别'],autopct='%1.1f%%')
plt.tight_layout()
plt.title('用户性别比例')
plt.savefig('用户性别比例.png')
plt.show()