<h1 id="top"><a href="https://enigma-code-breaker.herokuapp.com/">ENIGMA CODE BREAKER</a></h1>

## Contents
<ul>
    <li>
        <a href="#introduction"><strong>Introduction</strong></a>
    </li>
    <li>
        <a href="#ux"><strong>UX</strong></a>               
    </li>
     <li>
        <a href="#features"><strong>Features</strong></a>
    </li>
    <li>
        <a href="#technologies"><strong>Technologies</strong></a>
    </li>
    <li>
        <a href="#testing"><strong>Testing</strong></a>   
    </li>
    <li>
        <a href="#deployment"><strong>Deployment</strong></a>
    </li>
    <li>
       <a href="#credits"><strong>Credits</strong></a> 
    </li>
    <li>
        <a href="#references"><strong>References</strong></a>
    </li>
</ul>
<hr>
<h2 id="introduction">Itroduction</h2>

ENIGMA - Code Breaking Game, is a Python terminal game that runs on Heroku.

This game is losely based on the board game of [Mastermind]( https://en.wikipedia.org/wiki/Mastermind_(board_game)) from the 1970s.

### Demo
A live version of the game can be found <a href="https://enigma-code-breaker.herokuapp.com/">**HERE**</a><br><br>
<img src="assets/screenshots/enigma-welcome-screen.png"><br><br>
<a href="#top">Back to the top.</a>


## How To Play

ENIGMA gameplay, players try to crack the ENIGMA code randomly chosen by the computer. Players are given hints generated by the computer after every attempt to try to logically deduce what the correct secret code is.  

* The ENIGMA code is 4 unique numbers between 1 - 8.

* The player has 10 attempts to guess the secret code.  The correct guess must be all 4 correct numbers in the correct order.

* After every attempt (unless you guess the ENIGMA code) the player is given a code hint. GREEN represents how many numbers were correct and in the correct position. YELLOW represents how many numbers were correct but not in the incorrect position & RED represents how many numbers are not in the ENIGMA code at all.  

* The ENIGMA hints of GREEN, YELLOW & RED do not match the order of the player's numbers in their guess to make the game more challenging.

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

<h2 id="ux">User Experience (UX)</h2>

### User Stories

Target Audience – Anyone who wants to play an online command-line interface strategy game for a fun challenge.

As a user I want to:
* play the game clearly across different devices
* understand how to play the game
* play a game that is not timed
* know how many attempts I have left
* know when I have entered something in an incorrect format and understand why
* have fun and be challenged
* have the choice to easily play again or quit

### User Experience in this Game
This game takes the users' stories mentioned above into consideration to create a positive UX.

<h2 id="features">Features</h2>

**Title Section:**

* [Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/#:~:text=pyfiglet%20takes%20ASCII%20text%20and,pyfiglet%20module%20%3A%20pip%20install%20pyfiglet) was installed and import pyfiglet was used to generate ASCII art for the title and subtitle of the game.

* The Figlet font banner3-D was used for the title of the game 

* For the subtitle the Figlet font used was digital.

* Text is run from left to right over the screen with the message "Guess all 4 numbers to crack the ENIGMA code!"

**Username Input Section:**

* A message to the user to enter their name is seen first. This alerts the user on how to start playing the game.

<img src="assets/screenshots/enigma-name-screen.png"><br><br>

* If the user enters a blank space or enters only numbers as the username an error will be shown with info on the error

<img src="assets/screenshots/enigma-blank-username.png"><br><br>

* After the user enters a correct username this is returned in green with a welcome message

<img src="assets/screenshots/enigma-name-screen.png"><br><br>

**Game Help Section:**

* The user is then presented with 2 options, view the help screen by entering H or play game by entering P

<img src="assets/screenshots/enigma-play-help-screen.png"><br><br>

* If anything is entered except P or H an error will be displayed to the user

<img src="assets/screenshots/enigma-help-error-screen.png"><br><br>

* If H is entered the help screen comes in view explaining how to play the ENIGMA game

* At the bottom of this screen there are 2 options, enter P to play the game or X to exit the help screen

<img src="assets/screenshots/enigma-help-screen.png"><br><br>

**Game Play Section:**

* If P is entered the ENIGMA game will start with the initial player guess request printed to the terminal

<img src="assets/screenshots/enigma-initial-game-screen.png"><br><br>

* Once the player has entered a vaild guess the code is evaulated against the ENIGMA code to see if any of the numbers match

* If any of the numbers match a hint will be shown to the user to indicate if it's either in the ENIGMA code and if it's in the correct postion by using the colour codes<br><br>
GREEN: One of the numbers is in the ENIGMA code and in the correct position<br><br>
YELLOW: One of the numbers is in the ENIGMA code but is not in the correct position<br><br>
RED: One of the numbers is not in the ENIGMA code at all<br><br>

<img src="assets/screenshots/enigma-code-hint.png"><br><br>

* If the user enters a blank space or a letters as the guess an error will be shown explaining why it's not a vaild guess 

<img src="assets/screenshots/enigma-letters-error.png"><br><br>

* If the user enters more than 4 mubers as the guess an error will be shown explaining why it's not a vaild guess 

<img src="assets/screenshots/enigma-to-many-numbers-error.png"><br><br>

* If the user is good enough to crack the ENIGMA code you will be presented with the WIN screen 

* At the bottom of the screen there is an option to play a new game by entering Y or exit the game by entering N

<img src="assets/screenshots/enigma-win-screen.png"><br><br>

* If the users attempts reach 0 then the  lose screen will be presented and the ENGIMA code will be revealed

* At the bottom of the screen there is an option to play a new game by entering Y or exit the game by entering N

<img src="assets/screenshots/enigma-lose-screen.png"><br><br>

* Should the user select to exit the game a goodbye message is displayed and the game is quit

<img src="assets/screenshots/goodbye-screen.png"><br><br>

<a href="#top">Back to the top.</a>

<h2 id="deployment">Deployment</h2>

The site was deployed via [Heroku]( https://id.heroku.com/login), and the live link can be found here: [ENIGMA – Code Breaker](https://enigma-code-breaker.herokuapp.com/) 

This project was developed utilising the [Code Institute Template]( https://github.com/Code-Institute-Org/python-essentials-template).  Some of the deployment steps below are specifically required for the new CI template and may not be applicable to older versions, or different projects.

Before deploying to Heroku pip3 freeze > requirements.txt was used to add pyfiglet and termcolor imports for deployment.

1.	Log in to [Heroku]( https://id.heroku.com/login) or create an account if required.
2.	Then, click the button labelled **New** from the dashboard in the top right corner and from the drop-down menu select **Create New App**.
3.	You must enter a unique app name, (I used mastermind-code-breaker).
4.	Next, select your region, (I chose Europe as I am in Ireland).
5.	Click on the **Create App** button.
6.	The next page you will see is the project’s Deploy Tab.  Click on the **Settings Tab** and scroll down to **Config Vars**.
7.	Click **Reveal Config Vars** and enter **port** into the **Key** box and **8000** into the **Value** box and click the **Add** button.
8.	Next, scroll down to the Buildpack section click **Add Buildpack** select **python** and click **Save Changes**.
9.	Repeat step 8 to add **node.js**.
o	**Note:** The Buildpacks must be in the correct order. If not click and drag them to move into the correct order.
10.	Scroll to the top of the page and now choose the **Deploy** tab.
11.	Select **Github** as the deployment method.
12.	Confirm you want to connect to GitHub.
13.	Search for the repository name and click the connect button.
14.	Scroll to the bottom of the deploy page and select preferred deployment type:

* Click either **Enable Automatic Deploys** for automatic deployment when you push updates to Github.

* Select the correct branch for deployment from the drop-down menu and click **Deploy Branch** for manual deployment.

<h2 id="technologies">Technologies</h2>

Throughout the planning, design, testing and deployment of the ENIGMA game , I have used a number of technologies:

### Languages
<ol>
    <li><a href="https://en.wikipedia.org/wiki/HTML5" target="_blank">HTML</a>
        <ul><li>The main structure of the website</li></ul>
    </li>
    <li><a href="https://en.wikipedia.org/wiki/CSS" target="_blank">CSS</a>
        <ul><li>For the design of the site</li></ul>
    </li>
    <li><a href="https://en.wikipedia.org/wiki/JavaScript" target="_blank">JavaScript</a>
        <ul><li>Within the template supplied by code institute</li></ul>
    </li>
    <li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank">Python</a>
        <ul><li>For hosting a local server during for testing</li>
        <li>For the gameplay logic</li></ul>
    </li>
    <li><a href="https://www.markdownguide.org/" target="_blank">Markdown</a>
        <ul><li>For the content and structure of the README.md</li></ul>
    </li>
</ol>   

### Version Control
<ol>
    <li><a href="https://github.com/" target="_blank">Git & Github</a>
        <ul><li>For the hosting and version control of the game</li></ul>
    </li>
    <li><a href="https://www.gitpod.io/" target="_blank">Gitpod</a>
        <ul><li>The development environment used for writing the code for the game</li></ul>
    </li>
</ol>


### Applications    
<ol>
   <li><a href="https://lucid.app/" target="_blank">Lucid Chart</a>
        <ul><li>For the creation of the flowchart</li></ul>
    </li>
    <li><a href="https://visualstudio.microsoft.com/" target="_blank">Visual Studio (Desktop)</a>
        <ul><li>For testing out ideas without interfering with code for website</li></ul>
    </li>
    <li><a href="https://slack.com/intl/en-gb/" target="_blank">Slack (Desktop)</a>
        <ul><li>For communicating with peers and troubleshooting problems with the different environments used during the course and coding.</li></ul>
    </li>
</ol>
    
### Frameworks, Libraries and Programs
<ol> 
    <li><a href="https://docs.python.org/3/library/time.html">Python time library</a>
        <ul>Used to delay the next line of text in the python terminal</ul>
    </li>
    <li><a href="https://pypi.org/project/termcolor/">Python termcolor library</a>
        <ul>Used to add colour to the text in the python terminal</ul>
    </li>
    <li><a href="https://favicon.io/" target="_blank">Favicon.io</a>
        <ul><li>Used to create the tab icon from an original PNG file</li></ul>
    </li> 
    <li><a href="http://pep8online.com/checkresult" target="_blank">PEP8 ONLINE</a>
        <ul><li>To test and search for errors in the Python code</li></ul>
    </li>
    <li><a href="https://wave.webaim.org/" target="_blank">WAVE Web Accessibility Evaluation Tool</a>
        <ul><li>To ensure compliance with accessibility</li></ul>
    </li>
    <li><a href="https://developers.google.com/web/tools/lighthouse" target="_blank">Lighthouse</a> Performance Tool
        <ul><li>To ensure high performance and quick loading times of the website</li></ul>
    </li>
</ol><br>  
<a href="#top">Back to the top.</a>





