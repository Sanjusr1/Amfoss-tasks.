## POKEMON RESCUE:
In this we need to edit the exsiting code and add a new code which includes a pop up window .
And to do that we need to first clone that repo to our local device and then create a poke virtual environment then install all the requirements needed .
when we run the given python code we can see a semi build app with some functions or some parts missing ,so in this task we will complete the code and update the app .
 
### STAGE 1:
This stage was a bit time consuming as it requires us to fetch poke api's from google and we need to display some specific features such as name abilities ,it's image and some important stats about that pokemon
And all this info has to pop up in the search window when we enter the name of that pokemon , for this I had to go through the QPixmap which is a Qt class (used to load , display and manage images ) for the image to display .
Then comes the part of adding background image to the search window , we can add that without disturbing the rest buttons with the help of setGeometry and QLabel .

### STAGE 2:

