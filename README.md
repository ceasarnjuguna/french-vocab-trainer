**Flashy**

Flashy is a vocabulary learning tool built using Python and the tkinter library. The program reads a CSV file containing French words and their English translations, and displays them on a UI where the user can practice their vocabulary. The user can flip the card to see the English translation, mark the word as learned or not learned, and move on to the next word.

**Usage**
To run the program, simply run the flashy.py file in your Python environment:

python flashy.py

The program will display a French word and its English translation on a UI. Click on the "Right" button if you knew the word, or the "Wrong" button if you didn't. The program will keep track of your progress and adjust the words you see accordingly.

**Files**
This project consists of the following files:

flashy.py: Contains the code for the Flashy program.
data/french_words.csv: Contains the French words and their English translations in CSV format.
images/card_front.png: The image of the front of the card.
images/card_back.png: The image of the back of the card.
images/right.png: The image for the "Right" button.
images/wrong.png: The image for the "Wrong" button.
Requirements
This project requires the following Python libraries:

tkinter
pandas
random
You can install these libraries using pip:

pip install tkinter pandas random

**Configuration**
Before running the program, make sure you have the following files in the correct directories:

data/french_words.csv
images/card_front.png
images/card_back.png
images/right.png
images/wrong.png
You can customize the UI and the buttons by replacing the image files in the images directory.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**
This project was inspired by a challenge from the 100 Days of Code course on Udemy.