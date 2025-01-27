## POKEMON RESCUE:
In this we need to edit the exsiting code and add a new code which includes a pop up window .

And to do that we need to first clone that repo to our local device and then create a poke virtual environment then install all the requirements needed .

when we run the given python code we can see a semi build app with some functions or some parts missing ,so in this task we will complete the code and update the app .
 
### STAGE 1:
This stage was a bit time consuming as it requires us to fetch poke api's from google and we need to display some specific features such as name abilities ,it's image and some important stats about that pokemon

And all this info has to pop up in the search window when we enter the name of that pokemon , for this I had to go through the QPixmap which is a Qt class (used to load , display and manage images ) for the image to display .

Then comes the part of adding background image to the search window , we can add that without disturbing the rest buttons with the help of setGeometry and QLabel .

### STAGE 2:
In before parts we have already added some buttons and capture is one of those buttons and the speciality of this button is that when we click this we will capture the pokemon we have searched and stores them in a file named captured 

For this we have to create a separate file named captured and add the path of that file to the search window , then add some functionalities like a pop up box if the pokemon got successfully captured , or an error message if a certain pokemon got already captured.

### STAGE 3:
In this we have to display all the captured pokemon on a new window that is similar to search_window from before with it's name and image 

To do that we have to create a new window and add it's path to search_window.py file , in that new window we can add some basic buttons like "next" and "previous" using QPushButton and QLabel , then add a function in which when we click on display it has to show the images which are stored in capture file , to do this we have to add the path of capture file to displaywindow and with the help of QPixmap , the image will display on the new window 

#### MY REVIEW:
Completing a semi-coded app was a new thing to me , during this task I had to learn many new things and even though it took time to do all this, it turned out to be nice ,and the outcome was as expected . 
