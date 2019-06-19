import os
source = '~/Downloads/scrapyproject/pythonprojects-master/scrapytut/crawledoutput.csv'


def install_function():
    os.system('sudo apt install python3.7')
    os.system('sudo apt install python3-venv')
    os.system('python3 -m venv my-newproject-env')
    os.system('. my-newproject-env/bin/activate')
    os.system('sudo apt-get install wget')
    os.system('pip3 install scrapy')
    os.system('sudo wget  -P ~/Downloads/ "https://github.com/dhinesh22/pythonprojects/archive/master.zip"')
    os.system('unzip ~/Downloads/master.zip -d ~/Downloads/scrapyproject')
    os.chdir('scrapyproject/pythonprojects-master/scrapytut')
    os.system('scrapy crawl scrapytut -o crawledoutput.csv')
    var = input("Please enter the destination folder for the output: ")
    destination = var
    os.system("mv %s %s" % (source, destination))
    print("The crawledoutput.csv file was successfully moved to the desired folder")
install_function()
