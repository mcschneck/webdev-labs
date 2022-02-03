/* 
  See Smashing Magazine Tutorial:
  https://www.smashingmagazine.com/2021/11/dyslexia-friendly-mode-website/
*/

const initPage = () => {
  //see if button is pressed, if so, add the class name to the body tag
  const pressed = window.localStorage.hetItem("dyslexic") === 'true';
  if (pressed) {
    document.body.classList.add("dyslexia-mode");
  }

  //toggle aria-pressed attribute
  if (pressed) {
    document.getElementById("#dyslexia-toggle").setAttribute('aria-pressed', 'true');
  }

  //add event listener to button
  document.getElementById("dyslexia-toggle").addEventListener('click', toggleDyslexiaMode)

  
}
const toggleDyslexiaMode = ev => {
  let pressed = ev.currentTargert.getAttribute('aria-pressed') === 'true';

  //toggle buttons current status
  ev.currentTargert.setAttribute('aria-pressed', String(pressed));

  //toggle the dyslexia mode class
  document.body.classList.toggle('dyslexia-mode');

  //persist the setting to local storage
  window.localStorage.setItem('dyslexic', String(pressed));
};

//invoke initPage functions
initPage();