import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud
from matplotlib import rcParams
rcParams['font.family'] = 'SimHei'

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data2.xlsx',sheet_name='组件4')
# 创建一个字典，将类型作为键，大小作为值
word_freq = dict(zip(df['指标'].astype(str), df['绝对数']))
# 创建词云对象，并将字典传递给generate_from_frequencies方法
wordcloud = WordCloud(width=800, height=400, background_color='white',font_path='C:/Windows/Fonts/msyh.ttc').generate_from_frequencies(word_freq)
wordcloud.to_file(r'服务业货物运输量.png')
# 绘制词云图
plt.figure(figsize=(100, 50))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.title('服务业货物运输量')
plt.show()'''

'''df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data2.xlsx',sheet_name='组件2')
plt.pie(df['产量'], labels=df['种类'],autopct='%1.1f%%')
plt.tight_layout()
plt.title('农业各类产品产量')
plt.savefig('农业各类产品产量.png')
plt.show()'''

df = pd.read_excel(r'D:\PycharmProjects\工具包\mat\data2.xlsx',sheet_name='组件1')
font_prop = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
# 绘制折线图
plt.figure(figsize=(10, 5))
plt.plot(df['年份'], df['快递业务量'], marker='o', linestyle='-', color='b', label='折线图')
# 添加标签和标题
plt.xlabel('年份',fontproperties=font_prop)
plt.ylabel('快递业务量',fontproperties=font_prop)
plt.title('快递业务量变化折线图',fontproperties=font_prop)
# 显示图例
plt.legend()
plt.savefig('快递业务量.png')
# 显示图表
plt.show()