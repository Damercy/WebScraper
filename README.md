# WebScraper
A basic webscraper to scrape NSE livestocks data at an interval of 15 minutes. Created using python. Used Selenium and Chromedriver to scrape the data into a .xls file.


![actualNSE][tolink]

### How to run
---
After cloning the repo, do the following steps:-
1. [Download] the chromedriver based on your chrome version. 
   (Currently tested on Version 79.0.3945.130 (Official Build) (64-bit))
2. After extracting the .zip file, change the directory in the webscraper_2.0.py file where chromedriver.exe has been extracted to.
   Alternatively, you can extract the chromedriver to the downloaded directory path of this repo.
   ``` python
       ...
       chrome_path = r"D:\Work\Yash\Webscraper 2.0\chromedriver.exe"  #Change this path accordingly
       driver = webdriver.Chrome(chrome_path)
    
    ```
3. Finally, run the webscraper_2.0.py!

You'll find a .xls file being created at an interval of 15 minutes. 

![xls-file][filelink]
> Exit the script to stop the program.

It was a fun thing to build. I hope you liked it! :)

## Thanks for tuning in!

[tolink]: https://github.com/Damercy/WebScraper/blob/master/Screenshots/NSEScreenshot.JPG 'NSE homepage'
[filelink]: https://github.com/Damercy/WebScraper/blob/master/Screenshots/OutputScreenshot.JPG 'The .xls file'
[Download]: https://chromedriver.chromium.org/downloads
