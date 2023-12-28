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
	"Globally, buildings are responsible for approximately 36% of total energy use and 39% of CO₂ emissions.",
    "The annual global carbon footprint from the fashion industry is estimated to be around 3.3 billion tons of CO₂.",
    "As of 2021, the average global temperature has increased by approximately 1.2 degrees Celsius compared to pre-industrial levels.",
    "The Amazon rainforest, often referred to as the 'lungs of the Earth,' produces around 20% of the world's oxygen.",
    "In 2019, renewable energy accounted for about 26.2% of global electricity production.",
	"Worldwide, over 90 million barrels of crude oil are consumed each day, contributing to CO₂ emissions.",
    "The global use of coal for electricity generation surpasses 9,000 million metric tons annually.",
    "Approximately 1.3 billion tons of food are wasted globally each year, leading to significant carbon emissions.",
    "The aviation industry is responsible for more than 2% of global CO₂ emissions.",
    "In 2020, global carbon dioxide emissions decreased by around 5.8% due to the COVID-19 pandemic.",
    "The production of one ton of cement releases about 1 ton of CO₂ into the atmosphere.",
    "Over 1.5 billion new smartphones are manufactured each year, contributing to electronic waste and carbon emissions.",
    "The burning of fossil fuels for energy production accounts for over 70% of global greenhouse gas emissions.",
    "Annually, deforestation results in the loss of around 7 million hectares of forest, releasing stored carbon.",
    "The Paris Agreement aims to limit global warming to well below 2 degrees Celsius above pre-industrial levels.",
    "Roughly 25% of the world's population relies on biomass (wood, charcoal) for cooking, contributing to indoor air pollution and carbon emissions.",
    "The ocean absorbs about 30% of the CO₂ released into the atmosphere, leading to ocean acidification.",
    "Every year, over 8 million metric tons of plastic enter the oceans, contributing to marine pollution and environmental harm.",
    "The construction industry is responsible for nearly 40% of global energy-related CO₂ emissions.",
    "The average American generates over 16 metric tons of carbon dioxide emissions annually."
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

if (!window.parent.document.querySelector('[class^=icon3]')) {
    var newDiv2 = document.createElement('span');
            
    newDiv2.className  = 'icon3';

    var button2 = window.parent.document.querySelector('div[id^=tabs-bui][id$=-tabpanel-2] > div > div > div > div > div > div > div> div > div > div > button[kind = "secondary"] > div');

    button2.appendChild(newDiv2);
};
                        
function checkScreenWidth() {
  var screenWidth = window.innerWidth || window.parent.document.documentElement.clientWidth || window.parent.document.body.clientWidth;

  if (screenWidth <= 600) {
            window.parent.document.getElementById('project-copyright').style.display = 'none';
			Array.from(window.parent.document.querySelectorAll('button[data-baseweb="tab"] > div > p')).forEach(button => button.style.fontSize = '10px');
  } else {
            window.parent.document.getElementById('project-copyright').style.display = 'block';
  }
}

window.onload = checkScreenWidth;
window.onresize = checkScreenWidth;
