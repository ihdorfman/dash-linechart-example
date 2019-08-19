import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Recent Temps From Various Places Last Seven Days"
mytitle = "Recent Temperature Highs (Fahrenheit)"
x_values = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y1_values = [90, 84, 88, 84, 90, 91, 95]
y2_values = [54, 55, 57, 61, 61, 59, 63]
y3_values = [-72, -62, -69, -90, -90, -96, -78]
color1 = '#fc9403'
color2 = '#0307fc'
color3 = '#9003fc'
name1 = 'Maryland'
name2 = 'Melbourne, Australia'
name3 = 'Antarctica'
tabtitle = 'Temperatures'
sourceurl = 'https://www.timeanddate.com/weather/antarctica/south-pole/historic'
githublink = 'https://github.com/ihdorfman/dash-linechart-example'

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
