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
  } else {
            window.parent.document.getElementById('project-copyright').style.display = 'block';
  }
}

window.onload = checkScreenWidth;
window.onresize = checkScreenWidth;