import pandas as pd
import numpy as np
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.express as ex
import plotly.graph_objects as go

### Import the datq
df=pd.read_pickle('rawdata_master.pkl')
#print(df.head(5))

## fetch only the required columns
#print(df.columns.tolist())
cols=['username','time','comments_count','likes_count','follower_count','following_count','media_count','mean_likes','mean_comments',
'avg_likes_20post','avg_comments_20post','Engagement_score_20post']

df1=df[cols]
external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css']

app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
server=app.server

app.layout=html.Div([
    html.Div([
        html.H1("Influencer Performance Dashboard",style={'color':'white','fontSize':30})
    ],style={'backgroundColor':'black','textAlign':'center'}),

    html.Div([
        dcc.Dropdown(id="user_id",
                     options=[{'label':i,'value':i} for i in df1.username.unique()],
                     multi=False,
                     value=df.username.unique()[0]
                     )
    ],style={'textAlign':'left','marginLeft':'40%','marginRight':'40%'}),

    html.Br(),

    html.Div([
        html.Div([
            html.P("Followers",style={'color':'black','fontSize':20}),html.H6(id='followers')
        ],className='two columns',style={'textAlign':'center'}),

        html.Div([
            html.P("Following",style={'color':'black','fontSize':20}),html.H6(id="following")
        ],className='two columns',style={'textAlign':'center'}),

        html.Div([
            html.P("Mean Likes",style={'color':'black','fontSize':20}),html.H6(id="likes")
        ],className='two columns',style={'textAlign':'center'}),

        html.Div([
            html.P("Mean Comments",style={'color':'black','fontSize':20}),html.H6(id="comments")
        ],className='two columns',style={'textAlign':'center'}),

        html.Div([
            html.P("Media Count",style={'color':'black','fontSize':20}),html.H6(id="media")
        ],className='two columns',style={'textAlign':'center'}),

        html.Div([
            html.P("Enagagement Rate (%)",style={'color':'black','fontSize':20}),html.H6(id="er")
        ],className='two columns',style={'textAlign':'center'})
    ],className='row',style={'color':'gray'}),

    html.Br(),

    html.Div([
        dcc.Graph(id='graph1')
    ]),
    
    html.Br(),

    html.Div([
        dcc.Graph(id='graph2')
    ])
],style={'marginLeft':'10%','marginRight':'10%'})

@app.callback(
    [Output(component_id='followers',component_property='children'),
     Output(component_id='following',component_property='children'),
     Output(component_id='likes',component_property='children'),
     Output(component_id='comments',component_property='children'),
     Output(component_id='media',component_property='children'),
     Output(component_id='er',component_property='children'),
     Output(component_id='graph1',component_property='figure'),
     Output(component_id='graph2',component_property='figure')],
    [Input(component_id='user_id',component_property='value')]
)


def update_graph(select_user):
    df2=df.copy()
    df2=df2.sort_values(['username','time'],ascending=[True,True])
    tempdf=df2[(df2['username']==select_user) & (df2['row_number']<=20)]
    #print(tempdf.columns)
    ## plot the likes count for the latest 20 post 
    if select_user is None:
        return ex.area(data_frame=df2[(df2['row_number']<=20) & (df2['username']=='4_da_luv_of_food')],x='time',y='likes_count',template='plotly_dark',title="Likes count of last 20 post of 4_da_luv_of_food")

    fig1=ex.area(data_frame=tempdf[tempdf['row_number']<=20],x='time',y='likes_count',template='plotly_dark',title="Likes count of last 20 post of {}".format(select_user))
    fig1.update_traces(mode="markers+lines")
    fig1.update_layout(title_x=0.5)
    fig2=ex.area(data_frame=tempdf[tempdf['row_number']<=20],x='time',y='comments_count',template='plotly_dark',title="Comments count of last 20 post of {}".format(select_user),color_discrete_sequence=['white'])
    fig2.update_traces(mode="markers+lines",fillcolor="white")
    fig2.update_layout(title_x=0.5)

    follower=tempdf['follower_count'].unique()[0]
    following=tempdf['following_count'].unique()[0]
    ml=tempdf['mean_likes'].unique()[0]
    mc=tempdf['mean_comments'].unique()[0]
    mec=tempdf['media_count'].unique()[0]
    es=round(tempdf['Engagement_score_20post'].unique()[0],2)

    return follower,following,ml,mc,mec,es,fig1,fig2


if __name__=='__main__':
    app.run_server(port=4050,host='0.0.0.0')