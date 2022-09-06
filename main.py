import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd 
import matplotlib.pyplot as plt 
from flask import Flask,render_template,request,jsonify,redirect,session,abort

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup
import os

server =Flask(__name__)

bot= ChatBot('ChatBot')

trainer = ListTrainer(bot)

for file in os.listdir('./data/'):

    chats = open('./data/' + file, 'r').readlines()

    trainer.train(chats)
@server.route("/ask", methods=['POST'])
def ask():

    message = str(request.form['messageText'])

    bot_response = bot.get_response(message)

    while True:

        if bot_response.confidence > 0.1:

            bot_response = str(bot_response)      
            print(bot_response)
            return jsonify({'status':'OK','answer':bot_response})
 
        elif message == ("bye"):

            bot_response='Hope to see you soon'

            print(bot_response)
            return jsonify({'status':'OK','answer':bot_response})

            break

        else:
        
            try:
                url  = "https://en.wikipedia.org/wiki/"+ message
                page = get(url).text
                soup = BeautifulSoup(page,"html.parser")
                p    = soup.find_all("p")
                return jsonify({'status':'OK','answer':p[1].text})

            except IndexError as error:

                bot_response = 'Sorry i have no idea about that.'
            
                print(bot_response)
                return jsonify({'status':'OK','answer':bot_response})


data1=pd.read_csv('hiv-death-rates-by-age.csv')
data2=pd.read_csv('share-of-children-under-five-years-old-with-hiv.csv')
data3=pd.read_csv('share-of-population-infected-with-hiv-ihme.csv')
data4=pd.read_csv('share-of-women-among-the-population-living-with-hiv.csv')

test = data1['Entity'].unique()
options_d = [{'label': t, 'value': t} for t in test]
yrs=data1["Year"].unique()
yl=[]
for i in yrs:
    yl.append(int(i))


   
   




fig = px.pie(data4, values='Womehiv', names='Year')
app = dash.Dash(__name__, server=server, url_base_pathname='/dash/',external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div(id='d1', className='ban', children=[
                html.Img(id='img', className='', children=[],
                    src='assets/hiv_logo.png', alt=''),
                    html.H1(id='', className='h1', children='Hiv & AIDS'),
                    html.H3(id='', className='h3', children='(Human Immunodeficiency Virus & Acquired immunodeficiency syndrome)'),
                    html.Hr(id='hr', className='', children=[])
            ])
           ], lg='12')
    ]),
    dbc.Row([
        dbc.Col([html.H1(id='h11', className='', children='World AIDS Day : 1st December'),
   
        ], lg='12',style={'textAlign':'center'})
    ]),
html.Br(id='', className='', children=[]),
    dbc.Row([
        dbc.Col([

             
             dbc.Row( [
                dbc.Col([
            
            html.Div(id='', className='pts', children=[html.H3(id='', className='sym', children='Myth'),
            html.Ul(id='', className='', children=[
                html.Li(id='', className='', children=["HIV can spread as a result of touching,hugging, shaking hands, or kissing someone who has it"
                    
                ]),
                 html.Li(id='', className='', children=["HIV can spread via infected water or food"
                    
                ]),
                 html.Li(id='', className='', children=["HIV is transmissible via infected insects and pets"
                    
                ]),
                 html.Li(id='', className='', children=["If a couple has HIV, they do not need to protect themselves"
                    
                ]),
                 html.Li(id='', className='', children=["Blood transfusions raise the risk of HIV"
                    
                ]),
                 html.Li(id='', className='', children=["HIV does not spread through oral sex"
                    
                ]),
                 html.Li(id='', className='', children=["Hiv Means Life Over"
                    
                ])
                
            ])
            ])],lg='12')])




           
            
       
        
        
        
        
        
        ], lg='3'),



        dbc.Col([
dbc.Row([
    dbc.Col([html.Div(id='', className='', children=[html.H1(id='', className='tit', children='What is HIV?'),
    
dcc.Markdown(id='', className='', children='''
HIV (human immunodeficiency virus) is a virus that attacks cells that help the body fight infection, making a person more vulnerable to other infections and diseases. It is spread by contact with certain bodily fluids of a person with HIV, most commonly during unprotected sex (sex without a condom or HIV medicine to prevent or treat HIV), or through sharing injection drug equipment.

If left untreated, HIV can lead to the disease AIDS (acquired immunodeficiency syndrome).

The human body can’t get rid of HIV and no effective HIV cure exists. So, once you have HIV, you have it for life.

First identified in 1981, HIV is the cause of one of humanity’s deadliest and most persistent epidemics.
''')

]) ], lg='6'),
    dbc.Col([html.Div(id='', className='', children=[
        html.H1(id='', className='tit', children='What is AIDS?'),
    
dcc.Markdown(id='', className='tt', children='''
    
AIDS is the late stage of HIV infection that occurs when the body’s immune system is badly damaged because of the virus. In the U.S., most people with HIV do not develop AIDS because taking HIV medicine every day as prescribed stops the progression of the disease.

A person with HIV is considered to have progressed to AIDS when:

the number of their CD4 cells falls below 200 cells per cubic millimeter of blood (200 cells/mm3). (In someone with a healthy immune system, CD4 counts are between 500 and 1,600 cells/mm3.) OR
they develop one or more opportunistic infections regardless of their CD4 count.
Without HIV medicine, people with AIDS typically survive about 3 years. Once someone has a dangerous opportunistic illness, life expectancy without treatment falls to about 1 year. HIV medicine can still help people at this stage of HIV infection, and it can even be lifesaving. But people who start ART soon after they get HIV experience more benefits—that’s why HIV testing is so important.''')
    ]) ], lg='6')



]
)

        ], lg='9'),
        
]),

dbc.Row( [
    dbc.Col([dbc.Row( [
                dbc.Col([
            html.Br(id='', className='', children=[]),
            html.Div(id='', className='pts', children=[html.H3(id='', className='sym', children='Hiv Source'),
            html.Ul(id='', className='', children=[
                html.Li(id='', className='', children=["blood"
                    
                ]),
                 html.Li(id='', className='', children=["semen"
                    
                ]),
                 html.Li(id='', className='', children=["vaginal and rectal fluids"
                    
                ]),
                 html.Li(id='', className='', children=["breast milk"
                    
               
                    
                ])
                
            ])])])])   ,
            dbc.Row( [
                dbc.Col([
            html.Br(id='', className='', children=[]),
            html.Div(id='', className='pts', children=[html.H3(id='', className='sym', children='Prevention'),
            html.Ul(id='', className='', children=[
                html.Li(id='', className='', children=["Get tested for HIV and talked to your partner also"
                    
                ]),
                 html.Li(id='', className='', children=["Choose less risky sexual behaviors"
                    
                ]),
                 html.Li(id='', className='', children=["Use condoms every time you have sex"
                    
                ]),
                 html.Li(id='', className='', children=["Limit your number of sexual partners"
                    
               
                    
                ]),
                html.Li(id='', className='', children=["Talk to your health care provider about pre-exposure prophylaxis (PrEP)"
                    
               
                    
                ]),
                html.Li(id='', className='', children=["Do not inject drugs"
                    
               
                    
                ]),
                 html.Li(id='', className='', children=["Sex Education"
                    
               
                    
                ])
                
            ])])])])   ,
html.Br(id='', className='', children=[]),], lg='3'),
    dbc.Col([dbc.Row([
    dbc.Col([html.Div(id='', className='', children=[html.H1(id='', className='tit', children='How HIV spreads?'),
    html.Ul(id='', className='', children=[
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='By Having sex :'),
        html.Span(" You may become infected if you have vaginal, anal or oral sex with an infected partner whose blood, semen or vaginal secretions enter your body. The virus can enter your body through mouth sores or small tears that sometimes develop in the rectum or vagina during sexual activity.Your risk of HIV increases if you have multiple sexual partners.")


            
        ]),
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='By sharing needles. :'),
        html.Span(" Sharing contaminated IV drug paraphernalia (needles and syringes) puts you at high risk of HIV and other infectious diseases, such as hepatitis.")


            
        ]),
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='From blood transfusions :'),
        html.Span("  In some cases, the virus may be transmitted through blood transfusions. American hospitals and blood banks now screen the blood supply for HIV antibodies, so this risk is very small.")


            
        ]),
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='During pregnancy or delivery or through breast-feeding :'),
        html.Span(" Infected mothers can pass the virus on to their babies. Mothers who are HIV-positive and get treatment for the infection during pregnancy can significantly lower the risk to their babies.")


            
        ])
        
    ])


]) ], lg='6'),
   dbc.Col([html.Div(id='', className='', children=[html.H1(id='', className='tit', children='Risk factors'),
    html.Ul(id='', className='', children=[
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='Wasting syndrome :'),
        html.Span(" Untreated HIV/AIDS can cause significant weight loss, often accompanied by diarrhea, chronic weakness and fever.")


            
        ]),
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='Pneumocystis pneumonia (PCP) :'),
        html.Span(" This fungal infection can cause severe illness. Although it's declined significantly with current treatments for HIV/AIDS, in the U.S. PCP is still the most common cause of pneumonia in people infected with HIV.")


            
        ]),
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='Tuberculosis (TB) :'),
        html.Span("  TB is the most common opportunistic infection associated with HIV. It's a leading cause of death among people with AIDS.")


            
        ]),
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='Lymphoma :'),
        html.Span(" This cancer starts in the white blood cells. The most common early sign is painless swelling of the lymph nodes in your neck, armpit or groin. it's common to HIV/AIDS")


            
        ]),
        html.Li(id='', className='', children=[html.H4(id='', className='bld', children='Neurological complications :'),
        html.Span(" HIV can cause neurological symptoms such as confusion, forgetfulness, depression, anxiety and difficulty walking. HIV-associated neurocognitive disorders (HAND) can range from mild symptoms of behavioral changes and reduced mental functioning to severe dementia causing weakness and inability to function.")


            
        ]),
         html.Li(id='', className='', children=[html.H4(id='', className='bld', children='Liver disease:'),
        html.Span(" Liver disease is also a major complication, especially in people who also have hepatitis B or hepatitis C.")


            
        ])
        
    ])


]) ], lg='6'),

]
)

   ], lg='9'),
]),



dbc.Row( [
    dbc.Col([
        html.H4(id='', className='', children='Survey Report 1990 - 2020 ')
    ], lg='12',className="head")
]),

dbc.Row( [
    dbc.Col([
 html.Div([
html.H1(id='', className='tit', children='Death Couse of HIv/Aids from 1990-2020'),
       
          dcc.Dropdown(id='drop1', 
              options=options_d,
              value='India'
              #placeholder=''
          )
        

      
    ]),

    dcc.Graph(id='grp'),

    dcc.Slider(id='s1',
        min=1990, max=2019,
        step=1,
        value=2019,
        marks={i: '{}'.format(i) for i in range(1990,2024,2)}
    ),

    

    ], lg='6'),
     dbc.Col([
 html.Div([
html.H1(id='', className='tit', children='HIV Infected Children under (5 years)'),
       
          dcc.Dropdown(id='drop2', 
              options=options_d,
              value='India'
              #placeholder=''
          )
        

      
    ]),

    dcc.Graph(id='grp2'),

    dcc.Slider(id='s2',
        min=1990, max=2019,
        step=1,
        value=2019,
        marks={i: '{}'.format(i) for i in range(1990,2024,2)}
    ),


    

    ], lg='6'),
]),
dbc.Row( [
    dbc.Col([
 html.Div([
html.H1(id='', className='tit', children='Share-of-Women-among-the-Population-living-with-HIV')
       
        
        

      
    ]),

    dcc.Graph(id='grp3',figure=fig)

   

    

    ], lg='6'),
     dbc.Col([
 html.Div([
html.H1(id='', className='tit', children='Total-of-Population-Infected-With-HIV'),
       
          dcc.Dropdown(id='drop4', 
              options=options_d,
              value='India'
              #placeholder=''
          )
        

      
    ]),

    dcc.Graph(id='grp4'),

    
    

    

    ], lg='6'),
]),
dbc.Row( [
    dbc.Col([
        html.H3(id='', className='', children='Symptoms'),
        html.H4(id='', className='subtitle', children='The symptoms of HIV and AIDS vary, depending on the phase of infection.')
    ], lg='12',className="head")
]),

dbc.Row( [
    dbc.Col([html.H1(id='', className='tit', children='Primary infection (Acute HIV)'),
    html.Ul(id='', className='', children=[
        html.Li(id='', className='', children=['Fever' ]),
        html.Li(id='', className='', children=['Headache' ]), 
        html.Li(id='', className='', children=['Muscle aches and joint pain' ]), 
        html.Li(id='', className='', children=['Rash' ]), 
        html.Li(id='', className='', children=['Sore throat and painful mouth sores' ]), 
        html.Li(id='', className='', children=['Swollen lymph glands, mainly on the neck' ]), 
        html.Li(id='', className='', children=['Diarrhea' ]), 
        html.Li(id='', className='', children=['Weight loss' ]), 
        html.Li(id='', className='', children=['Cough' ]), 
        html.Li(id='', className='', children=['Night sweats' ]), 








            
       
    ])
    
    
    ],className="col1", lg='4'),
   dbc.Col([html.H1(id='', className='tit', children='Symptomatic HIV infection'),
    html.Ul(id='', className='', children=[
        html.Li(id='', className='', children=['Fever' ]),
        html.Li(id='', className='', children=['Fatigue' ]), 
        html.Li(id='', className='', children=['Swollen lymph nodes — often one of the first signs of HIV infection' ]), 
        html.Li(id='', className='', children=['Diarrhea' ]), 
        html.Li(id='', className='', children=['Weight loss' ]), 
        html.Li(id='', className='', children=['Oral yeast infection (thrush)' ]), 
        html.Li(id='', className='', children=['Shingles (herpes zoster)' ]), 
        html.Li(id='', className='', children=['Pneumonia' ])
     







            
       
    ])
    
    
    ],className="col1", lg='4'),
    dbc.Col([html.H1(id='', className='tit', children='Progression to AIDS'),
    html.Ul(id='', className='', children=[
        html.Li(id='', className='', children=['Sweats' ]),
        html.Li(id='', className='', children=['Chills' ]), 
        html.Li(id='', className='', children=['Recurring fever' ]), 
        html.Li(id='', className='', children=['Chronic diarrhea' ]), 
        html.Li(id='', className='', children=['Swollen lymph glands' ]), 
        html.Li(id='', className='', children=['Persistent white spots or unusual lesions on your tongue or in your mouth' ]), 
        html.Li(id='', className='', children=['Persistent, unexplained fatigue' ]), 
        html.Li(id='', className='', children=['Weight loss' ]), 
        html.Li(id='', className='', children=['Weakness' ]), 
        html.Li(id='', className='', children=['Skin rashes or bumps' ]), 








            
       
    ])
    
    
    ],className="col1", lg='4')
]),

dbc.Row([
    dbc.Col([html.Div(id='', className='', children=[html.H1(id='', className='tit', children='When Should I get tested for HIV?'),
    
dcc.Markdown(id='mg1', className='', children='''
CDC recommends everyone between the ages of 13 and 64 get tested for HIV at least once.

###### any of the following questions, then you should get an HIV test as soon as possible:

* Are you a man who has had sex with another man?

* Have you had sex—anal or vaginal—with a partner who has HIV?

* Have you had more than one sex partner since your last HIV test?

* Have you injected drugs and shared needles, syringes, or other drug injection equipment (for example, cookers) with others?

* Have you exchanged sex for drugs or money?

* Have you been diagnosed with or treated for another sexually transmitted disease?

* Have you been diagnosed with or treated for hepatitis or tuberculosis (TB)?

* Have you had sex with someone who could answer yes to any of the above questions or someone whose sexual history you don’t know?

* If you’re pregnant, talk to your health care provider about getting tested for HIV and other ways to protect you and your child from getting HIV.

''')

]) ], lg='6'),
    dbc.Col([html.Div(id='', className='', children=[
        html.H1(id='', className='tit', children='What to do if you are hiv positive ?'),
    
dcc.Markdown(id='', className='tt', children='''
    
* see a doctor as soon as possible so you can start treatment with HIV medicine

* in the early stage of infection, you are at very high risk of transmitting HIV to others. It is important to take steps to reduce your risk of transmission

* Taking HIV medicine can reduce the amount of HIV in the blood (called viral load).

* Monitor your health and try to save yourself from infections like flu or others

Living with HIV marks a new phase of your life. But if you take your HIV medicines as prescribed, it can be as healthy, active, and fulfilling as before. Make it a priority to take care of your body and mind. Get help if you feel depressed, and stay connected to people in your life you love and who support you.
'''),
html.Div(id='', className='bgg', children=[
    

html.Label(id='', className='', children='Sex workers and migrants most at risk of HIV, we can help them through workshops, counseling, medication and sex education'),
html.Label(id='', className='', children='Even in adolescence, many children are confused in questions related to sex, due to which they do wrong or unprotected sex, they need to know about all the information related to it '),
html.Label(id='', className='', children='It is the responsibility of both teachers and parents to openly talk to children and tell them about the dangers of unsafe sex.'),
html.Label(id='', className='', children='There should also be workshops related to sex education in schools and collages.')

    ]) ])], lg='6')



]
),
html.Br(id='', className='', children=[]),
dbc.Row( [
   
    dbc.Col([html.H3(id='', className='tit', children='You can talk to us or the bot without revealing your identity'),

    
     dcc.Markdown(id='', className='', children='''
    [Talk With Bot](/bot) / talk with counsler @ 7678678686 

    [contact us for organise Workshop and Seminar in your area](/regis)
    ''')
    
    ], lg='12',className="footer"),
   
])




])
@server.route("/")
def first():
    return render_template("index2.html")

@server.route("/dash")
def MyDashApp():
    return app.index()

@server.route("/bot")
def bot_talk():
    return render_template("chat.html")    

@app.callback(Output('grp', 'figure'), 
            Input('drop1', 'value'))
def fn(input_prop):
    mask = data1["Entity"] == input_prop
    fig = px.bar(data1[mask], x="Year", y="Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Rate)"
                )
    return fig
@app.callback(Output('grp2', 'figure'), 
            Input('drop2', 'value'))
def fn2(input_prop):
    mask2 = data2["Entity"] == input_prop
    fig = px.bar(data2[mask2], x="Year", y="Prevalence - HIV/AIDS - Sex: Both - Age: Under 5 (Percent)"
                )
    return fig

@app.callback(Output('grp4', 'figure'), 
            Input('drop4', 'value'))
def fn4(input_prop):
    mask3 = data3["Entity"] == input_prop
    fig = px.bar(data3[mask3], x="Year", y="Prevalence - HIV/AIDS - Sex: Both - Age: 15-49 years (Percent)",color="Year"
                )
    return fig





if __name__=='__main__':
    server.run(debug=True,port=2001)

                
                