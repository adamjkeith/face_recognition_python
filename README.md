# face_recognition_python
A simple facial recogniton software using python. Includes example as a voting system. 

Prepare computer to use program:
- install python 10, python 11 will not work.
- install visual studio community edition and install "Desktop Development with C++".
- click on the file path on the open folder with this file in and type cmd, this will open the folder in cmd.
- run "pip install -r modules.txt", this will install all the relevent modules


How to use the program:

!!IMPORTANT!! On first use:
- run the face_reg.py file, this will save a photo in the faces folder. If there is no image in there then the face_rec file will error. The face reg will require the user to press SPACE to take the photo and then will ask for a name.

On every other use:
- run the start.py file

I havent commented all the code as I got bored, this is how the program works:
- Asks the user if they want to vote.
- Takes a photo of the user (this will not have a pop up).
- If there is a photo of the user in the faces file then it will output ID Verified and will ask the user to press enter to exit.
- If there is NO photo of the user in the faces file it will ask if the user wants to register a new face.
- If the user wants to register a face, a pop up will appear which will require the user to press the space bar to take the photo, the user will be asked their name and the photo will be saved to the faces folder. The program will then restart.
- If the user does not want to register the program will restart.
