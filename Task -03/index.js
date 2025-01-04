const sounds = {
    "w": "sound1", 
    "a": "sound2",  
    "s": "sound3", 
    "d": "sound4",  
    "j": "sound5",  
    "k": "sound6",  
    "l": "sound7",  
  };
  
  function playSound(soundId) {
    const sound = document.getElementById(soundId);
    sound.play();
  }
  
  const buttons = document.querySelectorAll(".drum");
  buttons.forEach(button => {
    button.addEventListener("click", function() {
      const buttonClass = this.classList[0];
      playSound(sounds[buttonClass]);
    });
  });
  
  document.addEventListener("keypress", function(event) {
    const key = event.key.toLowerCase();
    if (sounds[key]) {
      playSound(sounds[key]);
    }
  });
