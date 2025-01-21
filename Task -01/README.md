## PART -1
 To begin with this task 
             First cloned the repo to my local device and created a folder for codes and started with the rest of the task 
      
## PART -2 
 Coming to this part there are some directories with "0x" and the spells stored in file "Spell_0y"
     and it's given that for this part x is the first perfect number i.e '6' and y is the result of the result that comes after differentiating (x²-7x) w.r.t 'x'. and i.e is 5
 and after checking them with their there respective folders and files the obtained spell is : Impedimenta

And by chross checking this with the spellbook folder the obtained code is :
             aHR0cHM6Ly9naX
            
### The commands used :
           cd : to open a directory 
           ls : to fetch files
           python compiler to run the .py file
           
## PART -3
This time we have to fetch the code out of "0y" directory and a file with "Spell_0x"
    And to find the x and y values we need to once again brushup our concepts with semi-conductors. And need to find out the first element that is needed to make semi-conductors 
   And yeah that element is Germanium !!!
and the atomic number is 32 : with this we found out the value of y i.e 2 and the value of x i.e 3           
       and with this the spell we got is  " Stupefy " along with the code :    RodWIuY29tL1RoZ

## PART -4
For this part of task we need change our branch into the branch which is taught by Professor Lupin at Hogwarts. 
And yeah that is "defenseAgainstTheDarkArts"!
after changing into this branch , we encountered a Sphinx and to pass safely we have to solve the riddle , and after solving this riddle the correct creature is "Boggart" 
And the spell used to fight this creature is "Riddikulus"
     And after spending a respectable amount of time on copying this spell from this branch to copying it to the spellbook of main branch 
     I was successful to get the code for this spell and that is : Uh1bnRzbWFuNC9U
     
### Commands used:
        git branch -a: to find all the git branches present 
        git checkout <remote branch > < new branch>: chnages to the new branch 
         
        
        
## PART - 5
  This part was the toughest among all the other parts , in this we have to go through all the commits made in this task 
 so in this task we are teleported to graveyard and we have to find ourselves back to out. and after going though all the commits which were commited by amfoss mentors 0the spell that we got is "Priori Incantatem" and the code is: aGVGaW5hbFNwZWxs
                                       
### Commands used:
          git log : to checkout all the commits that were done to the task
          git show --name-only <commit-hash> : gives the details of a specific commit 
  
  After entering all the codes into finalcode.txt we'll continue rest process.
## PART-6
The final code i.e finalcode.txt is aHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs

In this part :
             After decoding the finalcode.txt with the bash command "echo <base64 encodedString> | base64 --decode" ,the decoded code leads to a github link 

 github link : https://github.com/TheHuntsman4/TheFinalSpell

And cloned this repo to terminal and foundout the TheOneThatEndsItAll.txt and TheOneThatEndsItAll.py files

## TERMINAL COMMANDS:
    cd <dirctory_path> : changes the current directory to specified path
    ls : lists of files present in a directory 
    python xx.py: runs or prints the python text codes
    cat <specified file >: it prints the output of <specified file> to the terminal and with this u can only read the file , you can't change the file contents using this .
    mv <xx.txt> <yy.txt> : it renames the name of the text file form xx to yy
    mv <file.txt> /path/to/destination/ : it moves the file.txt to the folder given in the path 
    echo : this also used to display the text on terminal
    echo <base64enocodedstring> | base64 --decode : this is used to decode an encoded string .
## GIT COMMANDS:
      git clone: clones the repo to your local device
      git branch -a: displays all the branches present in that repo, including both local and remote branches.
      git checkout <remote branch > < new branch>: chnages to the new branch 
      git add : Adds files to the staging area, preparing them to be included in the next commit.
      git status : Displays the status of your working directory and staging area.
      git commit -m"":it keeps track of the staged changes in the repository. The -m flag allows you to include a message describing the changes
      git push :sends the committed changes to the git repo 
      



