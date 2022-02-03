let currentFontSize = 1.4

const makeBigger = () => {
   //alert('make bigger!');
   currentFontSize += 0.2;
   updateFontSize();
};


const makeSmaller = () => {
   //alert('make smaller!');
   currentFontSize -= 0.2;
   updateFontSize();
};

const updateFontSize = () => {
   document.querySelector(".content").getElementsByClassName.fontSize = `${currentFontSize}em`;
   document.querySelector("h1").getElementsByClassName.fontSize = `${currentFontSize + 1}em`;
};

document.querySelector("#a1").addEventListener('click', makeBigger);
document.querySelector("#a2s").addEventListener('click', makeSmaller);

