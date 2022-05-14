# **ENIGMA**
<h1 id="top"><a href="https://gamelink.com">ENIGMA CODE BREAKER</a></h1>

## Contents
<ul>
    <li>
        <a href="#Introduction"><strong>Introduction</strong></a>
    </li>
    <li>
        <a href="#UX"><strong>UX</strong></a>               
    </li>
    <li>
        <a href="#Technologies"><strong>Technologies</strong></a>
    </li>
    <li>
        <a href="#Features"><strong>Features</strong></a>
    </li>
    <li>
        <a href="#Testing"><strong>Testing</strong></a>   
    </li>
    <li>
        <a href="#Deployment"><strong>Deployment</strong></a>
    </li>
    <li>
       <a href="#Credits"><strong>Credits</strong></a> 
    </li>
    <li>
        <a href="#Screenshots"><strong>Screenshots</strong></a>
    </li>
    <li>
        <a href="#References"><strong>References</strong></a>
    </li>
</ul>
<hr>
# Introduction

ENIGMA - Code Breaking Game, is a Python terminal game that runs on Heroku.

This game is losely based on the board game of [Mastermind]( https://en.wikipedia.org/wiki/Mastermind_(board_game)) from the 1970s.

### Demo
A live version of the game can be found <a href="https://gamedemo.com/">**HERE**</a><br><br>
<img src="assets/documents/readme-images/demo.gif"><br><br>
<a href="#top">Back to the top.</a>


## How To Play

In ENIGMA, users play to crack the secret code randomly chosen by the computer.  Users are given hints generated by the computer after every attempt to try to logically deduce what the correct secret code is.  

*   The secret code is 4 unique numbers between 1 - 9.

* The player has 10 attempts to guess the secret code.  The correct guess must be all 4 correct numbers in the correct order.

* After every attempt (unless successful) the player is given a code hint.  REEN represents how many numbers were correct and in the correct position.  YELLOW represents how many numbers were correct but in the incorrect position & RED represents how many numbers are not in the ENIGMA code.  

* The code hint of GREENs and YELLOW do not match the order of the player's numbers in their guess to make the game more challenging.

>
>**For example:**
>
>       ENIGMA code is 1234
>
>       guess is: 1356
>
>       ENIGMA hint will be: RED RED GREEN YELLOW
>
>       This represents 1 is GREEN and 3 is YELLOW and 5 & 6 are RED


## User Experience (UX)

### User Stories

Target Audience – Anyone who wants to play an online command-line interface strategy game for a fun challenge.

As a User I want to:
* play the game clearly across different devices
* understand how to play the game
* play a game that is not timed
* know how many attempts I have left
* know when I have entered something in an incorrect format and understand why
* have fun and be challenged
* have the choice to easily play again or quit

### User Experience in this Game
This game takes the users' stories mentioned above into consideration to create a positive UX.

## Features

**Title Section:**

* [Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/#:~:text=pyfiglet%20takes%20ASCII%20text%20and,pyfiglet%20module%20%3A%20pip%20install%20pyfiglet) was installed and import pyfiglet was used to generate ASCII art for the title and subtitle of the game.

* banner3-D was used for the title of the game 

* For the subtitle the font used was digital.

* A message to the user to enter their name is seen first. This alerts the user on how to start playing the game.

* Text is run over the screen to explain the first

