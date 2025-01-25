## PIXELATED PROBLEM SOLVER

 In this task we were told to write a code in which it can take input from a  png file that contains a simple arthimatic expression and run it and give output for that expression 

And to do that we need to have some important libraries intaslled such as,
  
pillow (PIL) this is used for image processing , and in this task it acts as preprocesser by extracting accuracy from the given image, this includes in conversion of grayscale , noise reductio, resizes the image , enhance contrast ,threshold the image and finally sharpens the image .
  
 Then comes pytesseract and Tesseraact libraries,
 
Tesseract's primary purpose is to extract text from images. It converts text present in images into machine-readable text that can be further processed or used in applications. 
      Here the role of ocr is that it is a software tool that converts different types of documents into editable and searchable data by recognizing the text eith in the images.                 
       pytesseract is a Python wrapper for the Tesseract OCR engine .  (Optical Character Recognition), it makes Tesseract easily accessible in python projects without needing to handle command-line interactions.
       
 For these things to run we need to create an python vertual environment , i.e venv and add all the above mentioned required libraries .  
                   
  After setting up the python environment write a code in which it has to contain some functions for reading an image , preprossing an image and sepatare function for checking the arthmetic enquation then gives the output according to that .
                          
           
