import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from cStringIO import StringIO
import base64

html = '''
<html>
    <body>
        <img src="data:image/png;base64,{}" />
    </body>
</html>
'''

def data():
    df = pd.DataFrame(
        {'y':np.random.randn(10), 'z':np.random.randn(10)},
        index=pd.period_range('1-2000',periods=10),
    )
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    df.plot(ax=ax)

    io = StringIO()
    fig.savefig(io, format='png')
    data = base64.encodestring(io.getvalue())

    return html.format(data)



def pd_data():
    df = pd.DataFrame(
        {'y':np.random.randn(10), 'z':np.random.randn(10)},
        index=pd.period_range('1-2000',periods=10),
    )

    import pandas_highcharts
    from pandas_highcharts.core import serialize
    from pandas.compat import StringIO
    dat = """ts;A;B;C
    2015-01-01 00:00:00;27451873;29956800;113
    2015-01-01 01:00:00;20259882;17906600;76
    2015-01-01 02:00:00;11592256;12311600;48
    2015-01-01 03:00:00;11795562;11750100;50
    2015-01-01 04:00:00;9396718;10203900;43
    2015-01-01 05:00:00;14902826;14341100;53"""
    df = pd.read_csv(StringIO(dat), sep=';', index_col='ts', parse_dates='ts')

    # Basic line plot
    chart = serialize(df, render_to="my-chart", title="My Chart")
    # Basic column plot
    chart = serialize(df, render_to="my-chart", title="Test", kind="bar")
    # Basic column plot
    chart = serialize(df, render_to="my-chart", title="Test", kind="barh")
    # Plot C on secondary axis
    chart = serialize(df, render_to="my-chart", title="Test", secondary_y = ["C"])
    # Plot on a 1000x700 div
    chart = serialize(df, render_to="my-chart", title="Test", figsize = (1000, 700))

    return html.format(chart)
