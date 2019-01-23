SCRAPER - BOT - WELEAKINFO - FREE CHECKER - SINGLETHREADED
 
SETUP AND RUN
1. git clone https://github.com/Kajalwaldiya/scraper-bot.git
2. create a virtualenv for python3 and activate it.
	1. sudo apt-get install virtualenv
	2. virtualenv -p python3 env_name
	3. source env_name/bin/activate
3. cd scraper-bot 
4. install dependencies
	pip install -r requirements.txt
5. install chromedriver
	
	prerequisites
	1. sudo apt-get update
	2. sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4

	3. sudo apt-get install default-jdk 

	install chrome driver
	1. wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
	2. unzip chromedriver_linux64.zip
	3. sudo mv chromedriver /usr/bin/chromedriver
	4. sudo chown root:root /usr/bin/chromedriver
	5. sudo chmod +x /usr/bin/chromedriver

	install required jar files
	1. wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
	2. wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
	3. unzip testng-6.8.7.jar.zip

5. run app
	python manage.py runserver
6. open link : localhost:8000/bot_app in browser
7. output is stored in output.txt file in project root directory

SCOPE
1. I used selenium for web scraping.
2. 