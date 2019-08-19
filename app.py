import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Best Guess at Temperature Recently"
mytitle = "Recent Temperature Highs (Fahrenheit)"
x_values = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y1_values = [90, 88, 92, 96, 94, 94, 89]
y2_values = [32, 29, 24, 22, 24, 20, 19]
y3_values = [-20, -15, -19, -32, -26, -23, -35]
color1 = '#fc9403'
color2 = '#0307fc'
color3 = '#9003fc'
name1 = 'Maryland'
name2 = 'Australia'
name3 = 'Antarctica'
tabtitle = 'Temperatures'
sourceurl = 'https://www.baseball-reference.com'
githublink = 'https://github.com/austinlasseter/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
