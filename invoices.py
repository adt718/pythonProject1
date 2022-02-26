import os


root = os.path.dirname(__file__)
if root=="":root="."
template_html = root + '/template.html'


# replace date, name, item, price
from datetime import datetime
date = datetime.now().strftime('%Y年%m月%d日')

import pandas as pd
df = pd.read_csv("data.csv",
                 encoding='utf-8',
                 header=None,
                 names=["name","item","price"])

for i in range(df.shape[0]):
    # read template
    with open(template_html, "rt", encoding='utf-8') as f:
        text = f.read()
        No = str(i + 1)
        name = df.iloc[i]["name"]
        item = df.iloc[i]["item"]
        price = df.iloc[i]["price"]
        text = text.replace("__NAME__", name)
        text = text.replace("品物", item)
        text = text.replace("__PRICE__", str(price))
        text = text.replace('__DATE__', date)

        # prefile
        temp_file = root + '/No{}_{}_{}.html'.format(No,name,date)
        with open(temp_file, "wt", encoding="utf-8") as f:
            f.write(text)