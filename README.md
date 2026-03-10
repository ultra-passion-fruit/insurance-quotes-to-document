# Insurance Quotes to Document

This program produces a travel quotes PowerPoint with the contents tailored to the client's information.

### Functionality

1. Reads input form (.csv) with client information
2. Requests quotes from TuGo travel insurance API for the PL-SMED-21 'Visitors to Canada Medical' plan, according to input
3. Generates PowerPoint document with client travel insurance quote

### Setup

1. Click on the green "<> Code" button, then on "Download Zip". This will download all the contents from the repository into a folder on your computer.
2. Extract the contents from .zip file so you can see the folder.
3. Download the .csv file with the client information (not included) and put into the `contents` folder
4. Open the `keys.txt` file and update the file per the instructions (key and secret are on TuGo Dev portal).
5. Double click the `setup.command` file. This will create the Python environment and install all necessary dependencies.

Note: If you get an error saying The file “setup.command” could not be executed because you do not have appropriate access privileges, you will have to grant execute permissions for that file. Navigate to the current directory of the file and run `chmod +x setup.command`. This grants you execute permissions for that file.

1. That's it. 

### How to run
Prerequisites: Python 3.9.2 and up + venv 

1. Double-click the run.command file to run

2. The quotes PowerPoint will be created in the "quoted_presentations" folder. New presentations should be added to this folder.
