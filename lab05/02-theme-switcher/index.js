/*
    Hints: 
    1. Attach click event handlers to all four of the 
       buttons (#default, #ocean, #desert, and #high-contrast).
    2. Modify the className property of the body tag 
       based on the button that was clicked.
*/

const toDefaultTheme = () => {
   document.querySelector("body").className = "default";
}

const toOceanTheme = () => {
   document.querySelector("body").className = "ocean";
}

const toDesertTheme = () => {
   document.querySelector("body").className = "desert";
}

const toHighContrastTheme = () => {
   document.querySelector("body").className = "high-contrast";
}

document.querySelector("#default").addEventListener('click',toDefaultTheme);
document.querySelector("#ocean").addEventListener('click',toOceanTheme);
document.querySelector("#desert").addEventListener('click',toDesertTheme);
document.querySelector("#high-contrast").addEventListener('click',toHighContrastTheme);
