# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser



from dash import Dash, dcc, html, Output, Input  # pip install dash
import plotly.express as px
import webbrowser

# Incorporate data into app
df = px.data.medals_long()

# Build your components
app = Dash(__name__)
mytitle = dcc.Markdown(children='# App that Analyzes Olympic Medals')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot'],
                        value='Bar Plot',  # Initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
app.layout = html.Div([
    mytitle,
    dropdown,
    mygraph
], style={'width': '50%', 'margin': 'auto', 'textAlign': 'center'})

# Callback allows components to interact
@app.callback(
    Output(mygraph, component_property='figure'),
    Input(dropdown, component_property='value')
)
def update_graph(user_input):  # Function arguments come from the component property of the Input
    if user_input == 'Bar Plot':
        fig = px.bar(data_frame=df, x="nation", y="count", color="medal")
    elif user_input == 'Scatter Plot':
        fig = px.scatter(data_frame=df, x="count", y="nation", color="medal", symbol="medal")
    return fig  # Returned objects are assigned to the component property of the Output

# Run app
if __name__ == '__main__':
    url = "http://127.0.0.1:8053/"
    print(f"Dash is running on {url}")
    webbrowser.open(url)
    app.run_server(port=8053)

