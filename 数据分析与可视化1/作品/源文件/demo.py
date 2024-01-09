import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data.xlsx',sheet_name='组件5')
# 创建一个字典，将类型作为键，大小作为值
word_freq = dict(zip(df['地区'].astype(str), df['大学（大专及以上）']))
# 创建词云对象，并将字典传递给generate_from_frequencies方法
wordcloud = WordCloud(width=800, height=400, background_color='white',font_path='C:/Windows/Fonts/msyh.ttc').generate_from_frequencies(word_freq)
wordcloud.to_file(r"大学.png")
# 绘制词云图
plt.figure(figsize=(100, 50))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.title('词云示例')
plt.show()'''

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data.xlsx',sheet_name='组件')
font_prop = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
print(df['年份'])
# 绘制折线图
plt.figure(figsize=(10, 5))
plt.plot(df['年份'], df['老年抚养比(%)'], marker='o', linestyle='-', color='b', label='折线图')
# 添加标签和标题
plt.xlabel('年份',fontproperties=font_prop)
plt.ylabel('老年抚养比(%)',fontproperties=font_prop)
plt.title('折线图示例',fontproperties=font_prop)
# 显示图例
plt.legend()
plt.savefig('老年抚养比.png')
# 显示图表
plt.show()'''

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data.xlsx',sheet_name='组件2')
print(df)
plt.figure(figsize=(10, 5))
df.plot(x='列字段', y=['内地居民再婚登记(万人)-值字段', '内地居民初婚登记(万人)-值字段'], kind='bar', stacked=True)
plt.xlabel('日期')
plt.ylabel('值')
plt.title('初婚与再婚堆叠柱形图')
plt.savefig('初婚与再婚.png')
plt.show()'''