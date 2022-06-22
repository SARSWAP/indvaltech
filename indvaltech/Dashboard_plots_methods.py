import plotly
import plotly.express as px
from .models import *

l1 = testtable.objects.values()
print(l1)
d1 = []
d2 = []
for i in l1:
    d1.append(i["d1"])
    d2.append(i["d2"])

def plotdatadash():
    fig =px.bar(x=d1,y=d2)
    figg = plotly.io.to_html(fig,config= {'displayModeBar': False})
    return figg



def plotdatadash2():
   fig = px.line(x=d1, y=d2)
   figgs = plotly.io.to_html(fig,config= {'displayModeBar': False})
   return figgs