import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import pickle
import io
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(layout="wide",page_title="Carbon Footprint Calculator", page_icon="favicon.ico")

css="""
<style>
    body {
        
        background-image: url("https://cdn.dribbble.com/userupload/10094949/file/original-cfb063ae0f42b92b58d8b37642fa67d4.jpg?resize=5739x3227");        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        height: 100vh;
        }
    p {
    color: black;
    font-family: "Google Sans",Roboto,Arial,sans-serif;
    font-size: 20px;
    
    }
    div[data-testid="StyledLinkIconContainer"]> a, div[data-testid="StyledLinkIconContainer"]> a > svg {background-color: rgba(255, 255, 255,0); stroke: rgba(0, 0, 0, 0);}
    #popup {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, 50%);
            padding: 10px;
            background-color: #fff;
            border: 1px solid #ccc;
            z-index: 1000;
        }
    .button-17, div[data-testid  = "column"] > div > div> div > div > div > button{
          align-items: center;
          appearance: none;
          background-color: #fff;
          border-radius: 24px;
          border-style: none;
          box-shadow: rgba(0, 0, 0, .2) 0 3px 5px -1px,rgba(0, 0, 0, .14) 0 6px 10px 0,rgba(0, 0, 0, .12) 0 1px 18px 0;
          box-sizing: border-box;
          color: #3c4043;
          cursor: pointer;
          display: inline-flex;
          fill: currentcolor;
          font-family: "Google Sans",Roboto,Arial,sans-serif;
          font-size: 14px;
          font-weight: 500;
          height: 48px;
          justify-content: center;
          letter-spacing: .25px;
          line-height: normal;
          max-width: 100%;
          overflow: visible;
          padding: 2px 24px;
          position: relative;
          text-align: center;
          text-transform: none;
          transition: box-shadow 280ms cubic-bezier(.4, 0, .2, 1),opacity 15ms linear 30ms,transform 270ms cubic-bezier(0, 0, .2, 1) 0ms;
          user-select: none;
          -webkit-user-select: none;
          touch-action: manipulation;
          width: auto;
          will-change: transform,opacity;
          z-index: 0;
          margin: 0 auto;
          
        }    
        .button-17, div[data-testid  = "column"] > div > div> div > div > div > button:hover {
          background: #F6F9FE;
          color: #174ea6;
        }
        
        .button-17, div[data-testid  = "column"] > div > div> div > div > div > button:active {
          box-shadow: 0 4px 4px 0 rgb(60 64 67 / 30%), 0 8px 12px 6px rgb(60 64 67 / 15%);
          outline: none;
        }
        
        .button-17, div[data-testid  = "column"] > div > div> div > div > div > button:focus {
          outline: none;
          border: 2px solid #4285f4;
        }
    .DidYouKnow_root {
         box-shadow: rgba(77, 131, 132, 0.1) 0px 0px 0.5px 1px, rgba(0, 0, 0, 0.024) 0px 0.5px 0.9px, rgba(0, 0, 0, 0.035) 0px 1.4px 2.5px, rgba(0, 0, 0, 0.04) 0px 3.3px 6px, rgba(0, 0, 0, 0.06) 0px 11px 20px;
         cursor: pointer;
         padding: 1rem 20px;
         background: rgb(255, 255, 255);
         border-radius: 2rem;
         margin: 1.75em 0px;
         max-width: 1100px;
         overflow: hidden;
    }
    
    
    .TextNew {
         font-size: 1.5rem;
         line-height: 1.5;
    }
    
    .DidYouKnow_title {
         color: rgb(49, 91, 85);
         margin: 0px;
         user-select: none;
    }
    
    .DidYouKnow_content {
         color: rgb(14, 17, 23);
         margin-top: 0.5rem;
         padding: 0px 1.5rem;
    } 
    h1,h2,h3,h4 {
        color:rgb(14, 17, 23);
        color: inherit; 
        text-decoration: none; 
        cursor: default; 
    }
    
    button[data-testid = "baseButton-primary"]{width: 100%;}
    button[data-testid = "baseButton-secondary"]{width: 100%;}
    div[data-testid = "stApp"]{background: None; color: black;}
    div[id^=tabs-bui][id$=-tabpanel-0] > div> div > div > div > div[class = "stMarkdown"] {padding: 20px; border-radius: 2rem; background: rgba(255,255,255,0.7);}
    div[id^=tabs-bui][id$=-tabpanel-1] > div > div > div > div > div[class = "st-ae"] {padding: 20px; border-radius: 2rem; background: rgba(255,255,255,0.7);}
    div[id^=tabs-bui][id$=-tabpanel-2] > div > div > div > div > div[class = "st-ae"] {padding: 20px; border-radius: 2rem; background: rgba(255,255,255,0.7);}
    div[id^=tabs-bui][id$=-tabpanel-2] > div > div > div > div > div > div[id^=tabs-bui][id$=-tabpanel-0] > div> div > div > div > div[class = "stMarkdown"]{background: rgba(255,255,255,0);}
    div[data-testid  = "column"] > div > div> div > div > div > div >p {text-align: center;}
    div[data-testid  = "stButton"] {text-align: center;}
    div[data-testid  = "column"] > div > div> div > div > div > button > div > p {color: black;}
    div[data-testid  = "column"] > div > div> div > div > div > button[kind = "secondary"] > div > p {font-size: 25px; margin-bottom: 5px}
    svg[xmlns = "http://www.w3.org/2000/svg"]{stroke: rgba(0, 0, 0, 0.6);}
    div[data-testid = "stButton"] > button > div > p {color: white; font-size: 15px;}
    header[data-testid = "stHeader"]{background: rgba(255,255,255,0);}
    div[data-testid = "stDecoration"]{background: rgba(255,255,255,0);}
    div[data-baseweb = "tab-border"] {display: none;}
    
    div[id^=tabs-bui][id$=-tabpanel-0] > div > div > div > div > div[data-testid = "column"] > div > div> div > div > div > button[kind = "primary"] > div > p
     {
    font-size: 20px;
    font-weight: bold;
    }
    div[id^=tabs-bui][id$=-tabpanel-2] > div > div > div > div > div[data-testid = "column"] > div > div> div > div > div > button[kind = "secondary"] > div > p
     {
    font-size: 60px;
    margin-bottom: 15px;
    }
    div[data-baseweb="tooltip"] > div {background-color: rgb(255, 255, 255); border-radius: 2rem; padding: 10px;}

    div[id^=tabs-bui][id$=-tabpanel-4] > div > div > div > div > div > div > div> div > div > div > button[kind = "secondary"] 
     {
     background: #6fa861;
    }
    div[id^=tabs-bui][id$=-tabpanel-4] > div > div > div > div > div > div > div> div > div > div > button[kind = "secondary"] > div > p  
     {
     color: rgb(255, 255, 255);
    }
    .icon2 {
        background: url('https://i.imgur.com/dMDFyZF.png');
        height: 40px;
        width: 40px;
        background-repeat: no-repeat;
        display: block;
    }
    div[data-testid = "stMarkdownContainer"] > p > a {color: rgb(0, 0, 0); text-decoration: none; border: 0px; font-size: 20px; }
    div[data-testid = "stMarkdownContainer"] > p > a:hover:active {border: 1px solid; border-color: rgb(0, 255, 0);}
    div[data-testid = "stMarkdownContainer"] > p {text-align: center;}
    div[id^=tabs-bui][id$=-tabpanel-0] > div > div > div > div > div , div[id^=tabs-bui][id$=-tabpanel-0] > div > div > div > div > div > div {text-align: center; display: block;}
</style>
"""



def script():
    open_script = """
        <script>
            
            window.parent.document.getElementById('button-17').addEventListener('click', showPopup);
            window.parent.document.getElementById('button-17').addEventListener('click', changeText);
            window.parent.document.getElementById('popup').addEventListener('click', hidePopup);
            
            function showPopup() {
                window.parent.document.getElementById('popup').style.display = 'block';
                window.parent.document.getElementById('button-17').style.display = 'none';
            };
            function hidePopup() {
                window.parent.document.getElementById('popup').style.display = 'none';
                window.parent.document.getElementById('button-17').style.display = 'block';
            };
            var texts = [
                "Each year, human activities release over 40 billion tCO₂ into the atmosphere.",
                "The production of one kilogram of beef is associated with approximately 26 kgCO₂ emissions.",
                "The transportation sector accounts for nearly 25% of global CO₂ emissions, with the aviation industry being a major contributor.",
                "Deforestation contributes to about 10% of global carbon emissions, releasing stored carbon in trees into the atmosphere",
                "Some carbon offset projects, like reforestation initiatives, can sequester up to 20 tCO₂ per acre over several decades.",
                "Driving an electric vehicle can reduce an individual's carbon footprint by around 50% compared to a conventional gasoline-powered car.",
                "Approximately 3 kgCO₂ is produced when using 1GB of data, and watching an HD-quality movie on Netflix causes approximately 4.5 kgCO₂ emissions.",
            ];
        
            function changeText() {
                var randomIndex = Math.floor(Math.random() * texts.length);
                var newText = texts[randomIndex];
        
                window.parent.document.getElementById('popupText').innerHTML = newText;
            };
            
            if (!window.parent.document.querySelector('[class^=icon2]')) {
                var newDiv = document.createElement('span');
                        
                newDiv.className  = 'icon2';
        
                var button = window.parent.document.querySelector('div[id^=tabs-bui][id$=-tabpanel-4] > div > div > div > div > div > div > div> div > div > div > button[kind = "secondary"] > div');
        
                button.appendChild(newDiv);
            };
        </script>
        
    """
    html(open_script, width=0, height=0)


def click_element(element):
    open_script = f"<script type = 'text/javascript'>window.parent.document.querySelector('[id^=tabs-bui][id$=-{element}]').click();</script>"
    html(open_script, width=0, height=0)

left, middle, right = st.columns([2,3.5,2])
main, comps , result = middle.tabs([" ", " ", " "])

main.markdown("""
# 🌳About Carbon Footprint

A carbon footprint measures the total greenhouse gas emissions linked to an individual, organization, event, or product. It's a crucial metric for gauging our impact on the environment and climate change.

# 🌳Why It Matters

####  🍃Climate Impact
Reducing your carbon footprint directly contributes to global efforts against climate change, mitigating extreme weather and rising temperatures.

#### 🍃Resource Conservation
Cutting carbon often means using fewer natural resources, and promoting sustainability in water, energy, and raw materials.

#### 🍃Health and Well-being
Lowering emissions supports healthier lifestyle choices, improving air quality and physical well-being.

#### 🍃Sustainable Practices
Measuring and managing your carbon footprint encourages eco-friendly choices, fostering a more sustainable society.

#### 🍃Responsibility
Acknowledging and addressing your carbon impact demonstrates social and environmental responsibility.

""")

_,but,_ = main.columns([1,2,1])
if but.button("Calculate Your Carbon Footprint!", type="primary"):
    click_element('tab-1')

tab1, tab2, tab3, tab4, tab5 = comps.tabs(["👴 Personal","🚗 Travel","🗑️ Waste","⚡ Energy","💸 Consumption"])
tab_result,_ = result.tabs([" "," "])

def component():
    tab1col1, tab1col2 = tab1.columns(2)
    height = tab1col1.number_input("Height",0,251, value=None, placeholder="160", help="in cm")
    weight = tab1col2.number_input("Weight", 0, 250, value=None, placeholder="75", help="in kg")
    if (weight is None) or (weight == 0) : weight = 1
    if (height is None) or (height == 0) : height = 1
    calculation = weight / (height/100)**2
    body_type = "underweight" if (calculation < 18.5) else \
                 "normal" if ((calculation >=18.5) and (calculation < 25 )) else \
                 "overweight" if ((calculation >= 25) and (calculation < 30)) else "obese"
    sex = tab1.selectbox('Gender', ["female", "male"])
    diet = tab1.selectbox('Diet', ['omnivore', 'pescatarian', 'vegetarian', 'vegan'], help="""
                                                                                              Omnivore: Eats both plants and animals.\n
                                                                                              Pescatarian: Consumes plants and seafood, but no other meat\n
                                                                                              Vegetarian: Diet excludes meat but includes plant-based foods.\n
                                                                                              Vegan: Avoids all animal products, including meat, dairy, and eggs.""")
    social = tab1.selectbox('Social Activity', ['never', 'often', 'sometimes'], help="How often do you go out?")

    transport = tab2.selectbox('Transportation', ['public', 'private', 'walk/bicycle'],
                               help="Which transportation method do you prefer the most?")
    if transport == "private":
        vehicle_type = tab2.selectbox('Vehicle Type', ['petrol', 'diesel', 'hybrid', 'lpg', 'electric'],
                                      help="What type of fuel do you use in your car?")
    else:
        vehicle_type = "None"

    if transport == "walk/bicycle":
        vehicle_km = 0
    else:
        vehicle_km = tab2.slider('What is the monthly distance traveled by the vehicle in kilometers?', 0, 5000, 0, disabled=False)

    air_travel = tab2.selectbox('Frequency of Traveling by Air', ['never', 'rarely', 'frequently', 'very frequently'], help= """
                                                                                                                             Never: I don't travel by plane.\n
                                                                                                                             Rarely: Around 1-4 Hours.\n
                                                                                                                             Frequently: Around 5 - 10 Hours.\n
                                                                                                                             Very Frequently: Around 10+ Hours. """)

    waste_bag = tab3.selectbox('What is the size of your waste bag?', ['small', 'medium', 'large', 'extra large'])
    waste_count = tab3.slider('How many waste bags do you trash out in a week?', 0, 10, 0)
    recycle = tab3.multiselect('Do you recycle any materials below?', ['Plastic', 'Paper', 'Metal', 'Glass'])

    heating_energy = tab4.selectbox('What power source do you use for heating?', ['natural gas', 'electricity', 'wood', 'coal'])

    for_cooking = tab4.multiselect('What cooking systems do you use?', ['microwave', 'oven', 'grill', 'airfryer', 'stove'])
    energy_efficiency = tab4.selectbox('Do you consider the energy efficiency of electronic devices?', ['No', 'Yes', 'Sometimes' ])
    daily_tv_pc = tab4.slider('How many hours a day do you spend in front of your PC/TV?', 0, 24, 0)
    internet_daily = tab4.slider('What is your daily internet usage in hours?', 0, 24, 0)

    shower = tab5.selectbox('How often do you take a shower?', ['daily', 'twice a day', 'more frequently', 'less frequently'])
    grocery_bill = tab5.slider('Monthly grocery spending in $', 0, 500, 0)
    clothes_monthly = tab5.slider('How many clothes do you buy monthly?', 0, 30, 0)

    data = {'Body Type': body_type,
            "Sex": sex,
            'Diet': diet,
            "How Often Shower": shower,
            "Heating Energy Source": heating_energy,
            "Transport": transport,
            "Social Activity": social,
            'Monthly Grocery Bill': grocery_bill,
            "Frequency of Traveling by Air": air_travel,
            "Vehicle Monthly Distance Km": vehicle_km,
            "Waste Bag Size": waste_bag,
            "Waste Bag Weekly Count": waste_count,
            "How Long TV PC Daily Hour": daily_tv_pc,
            "Vehicle Type": vehicle_type,
            "How Many New Clothes Monthly": clothes_monthly,
            "How Long Internet Daily Hour": internet_daily,
            "Energy efficiency": energy_efficiency
            }
    data.update({f"Cooking_with_{x}": y for x, y in
                 dict(zip(for_cooking, np.ones(len(for_cooking)))).items()})
    data.update({f"Do You Recyle_{x}": y for x, y in
                 dict(zip(recycle, np.ones(len(recycle)))).items()})


    return pd.DataFrame(data, index=[0])


df = component()

data = df.copy()

data["Body Type"] = data["Body Type"].map({'underweight':0, 'normal':1, 'overweight':2, 'obese':3})
data["Sex"] = data["Sex"].map({'female':0, 'male':1})
data = pd.get_dummies(data, columns=["Diet","Heating Energy Source","Transport","Vehicle Type"], dtype=int)
data["How Often Shower"] = data["How Often Shower"].map({'less frequently':0, 'daily':1, "twice a day":2, "more frequently":3})
data["Social Activity"] = data["Social Activity"].map({'never':0, 'sometimes':1, "often":2})
data["Frequency of Traveling by Air"] = data["Frequency of Traveling by Air"].map({'never':0, 'rarely':1, "frequently":2, "very frequently":3})
data["Waste Bag Size"] = data["Waste Bag Size"].map({'small':0, 'medium':1, "large":2,  "extra large":3})
data["Energy efficiency"] = data["Energy efficiency"].map({'No':0, 'Sometimes':1, "Yes":2})

sample = {'Body Type': 2,
 'Sex': 0,
 'How Often Shower': 1,
 'Social Activity': 2,
 'Monthly Grocery Bill': 230,
 'Frequency of Traveling by Air': 2,
 'Vehicle Monthly Distance Km': 210,
 'Waste Bag Size': 2,
 'Waste Bag Weekly Count': 4,
 'How Long TV PC Daily Hour': 7,
 'How Many New Clothes Monthly': 26,
 'How Long Internet Daily Hour': 1,
 'Energy efficiency': 0,
 'Do You Recyle_Paper': 0,
 'Do You Recyle_Plastic': 0,
 'Do You Recyle_Glass': 0,
 'Do You Recyle_Metal': 1,
 'Cooking_with_stove': 1,
 'Cooking_with_oven': 1,
 'Cooking_with_microwave': 0,
 'Cooking_with_grill': 0,
 'Cooking_with_airfryer': 1,
 'Diet_omnivore': 0,
 'Diet_pescatarian': 1,
 'Diet_vegan': 0,
 'Diet_vegetarian': 0,
 'Heating Energy Source_coal': 1,
 'Heating Energy Source_electricity': 0,
 'Heating Energy Source_natural gas': 0,
 'Heating Energy Source_wood': 0,
 'Transport_private': 0,
 'Transport_public': 1,
 'Transport_walk/bicycle': 0,
 'Vehicle Type_None': 1,
 'Vehicle Type_diesel': 0,
 'Vehicle Type_electric': 0,
 'Vehicle Type_hybrid': 0,
 'Vehicle Type_lpg': 0,
 'Vehicle Type_petrol': 0}

sample_df = pd.DataFrame(data=sample,index=[0])
sample_df[sample_df.columns] = 0
sample_df[data.columns] = data

ss = pickle.load(open("scale.sav","rb"))
model = pickle.load(open("model.sav","rb"))
prediction = round(np.exp(model.predict(ss.transform(sample_df))[0]))

def hesapla():
    copy_df = sample_df.copy()
    travels = copy_df[["Frequency of Traveling by Air",
                         "Vehicle Monthly Distance Km",
                         'Transport_private',
                          'Transport_public',
                          'Transport_walk/bicycle',
                          'Vehicle Type_None',
                          'Vehicle Type_diesel',
                          'Vehicle Type_electric',
                          'Vehicle Type_hybrid',
                          'Vehicle Type_lpg',
                          'Vehicle Type_petrol']]
    copy_df[list(set(copy_df.columns) - set(travels.columns))] = 0
    travel = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    energys = copy_df[[ 'Heating Energy Source_coal','How Often Shower', 'How Long TV PC Daily Hour',
                         'Heating Energy Source_electricity','How Long Internet Daily Hour',
                         'Heating Energy Source_natural gas',
                         'Cooking_with_stove',
                          'Cooking_with_oven',
                          'Cooking_with_microwave',
                          'Cooking_with_grill',
                          'Cooking_with_airfryer',
                         'Heating Energy Source_wood','Energy efficiency']]
    copy_df[list(set(copy_df.columns) - set(energys.columns))] = 0
    energy = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    wastes = copy_df[[  'Do You Recyle_Paper','How Many New Clothes Monthly',
                         'Waste Bag Size',
                         'Waste Bag Weekly Count',
                         'Do You Recyle_Plastic',
                         'Do You Recyle_Glass',
                         'Do You Recyle_Metal',
                         'Social Activity',]]
    copy_df[list(set(copy_df.columns) - set(wastes.columns))] = 0
    waste = np.exp(model.predict(ss.transform(copy_df)))

    copy_df = sample_df.copy()
    diets = copy_df[[ 'Diet_omnivore',
                     'Diet_pescatarian',
                     'Diet_vegan',
                     'Diet_vegetarian', 'Monthly Grocery Bill','Transport_private',
                     'Transport_public',
                     'Transport_walk/bicycle',
                      'Heating Energy Source_coal',
                      'Heating Energy Source_electricity',
                      'Heating Energy Source_natural gas',
                      'Heating Energy Source_wood',
                      ]]
    copy_df[list(set(copy_df.columns) - set(diets.columns))] = 0
    diet = np.exp(model.predict(ss.transform(copy_df)))
    hesap = {"Travel": travel[0], "Energy": energy[0], "Waste": waste[0], "Diet": diet[0]}

    return hesap
def chart():
    p = hesapla()
    bbox_props = dict(boxstyle="round", facecolor="white", edgecolor="white", alpha=0.7)

    plt.figure(figsize=(10, 10))
    patches, texts = plt.pie(x=p.values(),
                             labels=p.keys(),
                             explode=[0.03] * 4,
                             labeldistance=0.75,
                             colors=["#29ad9f", "#1dc8b8", "#99d9d9", "#b4e3dd" ], shadow=True,
                             textprops={'fontsize': 20, 'weight': 'bold', "color": "#000000ad"})
    for text in texts:
        text.set_horizontalalignment('center')
        text.set_fontfamily(["cursive"])

    data = io.BytesIO()
    plt.savefig(data, transparent=True)

    background = Image.open("default.png")
    draw = ImageDraw.Draw(background)
    font1 = ImageFont.truetype(font="ArchivoBlack-Regular.ttf", size=50)
    font = ImageFont.truetype(font="arialuni.ttf", size=50)
    draw.text(xy=(320, 50), text=f"  How big is your\nCarbon Footprint?", font=font1, fill="#039e8e", stroke_width=1, stroke_fill="#039e8e")
    draw.text(xy=(370, 250), text=f"Monthly Emission \n\n   {prediction:.0f} kgCO₂e", font=font, fill="#039e8e", stroke_width=1, stroke_fill="#039e8e")
    data_back = io.BytesIO()
    background.save(data_back, "PNG")
    background = Image.open(data_back).convert('RGBA')
    piechart = Image.open(data)
    ayak = Image.open("ayak.png").resize((370, 370))
    bg_width, bg_height = piechart.size
    ov_width, ov_height = ayak.size
    x = (bg_width - ov_width) // 2
    y = (bg_height - ov_height) // 2
    piechart.paste(ayak, (x, y), ayak.convert('RGBA'))
    background.paste(piechart, (40, 200), piechart.convert('RGBA'))
    data2 = io.BytesIO()
    background.save(data2, "PNG")
    background = Image.open(data2).resize((700, 700))
    data3 = io.BytesIO()
    background.save(data3, "PNG")
    return data3

column1,column2 = tab1.columns(2)
_,resultbutton,_ = tab5.columns([1,1,1])
if resultbutton.button(" ", type = "secondary"):
    tab_result.image(chart(), use_column_width="never")
    click_element('tab-2')

pop = """
<button id = "button-17" class="button-17" role="button"> ❔ Did You Know</button>

<div id="popup" class="DidYouKnow_root">
<p class="DidYouKnow_title TextNew" style="font-weight: 100;"> ❔ Did you know</p>
    <p id="popupText" class="DidYouKnow_content TextNew"><span>
    Each year, human activities release over 40 billion metric tons of carbon dioxide into the atmosphere, contributing to climate change.
    </span></p>
</div>
"""
_,home,_ = comps.columns([1,2,1])
_,col2,_ = comps.columns([1,2,1])
col2.markdown(pop, unsafe_allow_html=True)
if home.button("🏡"):
    click_element('tab-0')
_,resultmid,_ = result.columns([1,2,1])

tab_result.markdown(f"You owe nature <b>{round(prediction / 411.4)}</b> trees monthly. <br> <a href='https://www.egeorman.org.tr/online-bagis-co2.aspx?adet={round(prediction / 411.4)}' id = 'button-17' class='button-17' role='button'> 🌳 Proceed to offset 🌳</a>",  unsafe_allow_html=True)

if resultmid.button("🖩", key="Calculator"):
    click_element('tab-1')
script()
