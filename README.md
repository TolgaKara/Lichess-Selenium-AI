# Lichess-Selenium-AI
## Summary
I am really proud of this project. I am not very strong at chess and I wanted to write a python Script to be strong in chess, to win against my Friends.

## How to setup
1. Create an Folder
2. Put the Script from Github into the Folder
3. Download Dataset of [Chess Games](https://www.kaggle.com/datasnaek/chess) from Kaggle
4. Download [Chromedriver](http://chromedriver.chromium.org/)
5. Put Chromedriver and the Chess Game Dataset into the Folder
6. Create an black and white CSV which is devided from the Chess Game Dataset by victory == white or black
7. Now you can start the programm and you get an Instruction into the Console 

## TODO
[x] Download Chess Dataset from Kaggle

[x] Download Chromedriver

[x] Split Kaggle CSV to white-player and black-player

[x] Get Suggestion after Game get played

[ ] More Data or instead of CSV-Data using API

[ ] Creating Connection to Stockfish API and get Suggestion

## Lesson Learned
* Clean Code is important
* Planning before Coding
* Write more Pythonic Code
* increased understanding of List Comprehension

## Problems
* It is not prepared for all moves variety because of lack of data
* bad representation of the Suggestion