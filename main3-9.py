import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

"""
タイトル設定st.title
"""
st.title('Streamlit 超入門')

"""
文字挿入st.write
"""
st.write('DataFrame')

#データセット
df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

"""
#動的表（ソートとかできる）
"""
st.dataframe(df.style.highlight_max(axis=0))

"""
静的表
"""
st.table(df.style.highlight_max(axis=0))

"""
文字挿入
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)

st.dataframe(df2)

"""
折れ線グラフ
"""
st.line_chart(df2)

"""
折れ線グラフ色有
"""
st.area_chart(df2)

"""
棒グラフ
"""
st.bar_chart(df2)

#新宿の緯度経度
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

st.dataframe(df3)


"""
マップ
"""
st.map(df3)



"""
画像読み込み
"""
img = Image.open('image.jpg')

st.image(img, caption='test',use_column_width=True)







