import pandas as pd
import plotly.express as px
df=pd.read_csv("line_chart.csv")
fig=px.line(df,x="year",y="per Capita income",color="country",title="Per Capita Income")
fig.show()

