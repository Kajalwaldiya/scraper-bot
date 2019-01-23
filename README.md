SCRAPER - BOT - WELEAKINFO - FREE CHECKER - SINGLETHREADED
 
SETUP AND RUN
1. git clone https://github.com/Kajalwaldiya/scraper-bot.git
2. create a virtualenv for python3 and activate it.
	a. sudo apt-get install virtualenv
	b. virtualenv -p python3 env_name
	c. source env_name/bin/activate
3. cd scraper-bot 
4. install dependencies
	pip install -r requirements.txt
5. install chromedriver
	
	prerequisites
	sudo apt-get update
	sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4

	sudo apt-get install default-jdk 

	install chrome driver
	wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	sudo mv chromedriver /usr/bin/chromedriver
	sudo chown root:root /usr/bin/chromedriver
	sudo chmod +x /usr/bin/chromedriver

	install required jar files
	wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
	wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
	unzip testng-6.8.7.jar.zip

5. run app
	python manage.py runserver
6. open link : localhost:8000/bot_app in browser