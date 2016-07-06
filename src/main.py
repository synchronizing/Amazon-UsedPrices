from bs4 import BeautifulSoup
from progress.bar import Bar
import requests
import sys
import re

def lookUp(search):
    url = "http://www.amazon.com/s?field-keywords=" + search
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
    soup = BeautifulSoup(response.content, "html.parser")
    title_html = soup.select("#result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-small > a > h2")
    price_html = soup.find_all("span", class_="a-size-base a-color-price a-text-bold")

    title = ""
    price = ""
    error = False

    try:
        title = str(re.search('data-attribute="(.*)">', str(title_html)).group(1))
        price = str(re.search('a-text-bold">(.*)</span>]', str(price_html)).group(1))
    except AttributeError:
        error = True

    exist = True

    if len(price) > 6:
        price = price[:price.index("</span>")]
    elif len(price) == 0:
        price = "unkn"
        title = title.replace("BM&amp;F: ", "")
        if title == "": exist = False
    try:
        if exist == True:
            try:
                price = float(price[1:])
            except ValueError:
                price = float("0.00")
    except AttributeError:
        error = True

    return [price, title, error]

arguments = sys.argv
if(arguments[1] == "-f"):
    bookfile = open(sys.argv[2])
    books = [line.rstrip('\n\r') for line in bookfile]
    output = open("output.txt", 'w')
    bar = Bar('Processing', max=len(books))

    errors = 0

    for i in books:
            bar.next()
            print("\tProcessing: " + i)

            info = lookUp(i)

            if(info[2] == True):
                output.write("Error. Could not find " +  i + "\n")
                errors += 1
            else:
                output.write(str(info[0]) + "\t" + str(info[1]) + "\n")

    print("Finished with " + str(errors) + " error(s). Saved to output.txt.")
    bar.finish()


elif(arguments[1] == "-d"):
    print("Type 'exit' to exit.\n")
    if(len(arguments) == 3):
        n = arguments[2]
    else:
        n = raw_input("Input: ")
    while True:
        if n == "exit":
            break
        else:
            info = lookUp(n)
            if(info[2] == True):
                print("Error. Could not find your search input.\n")
            else:
                print(str(info[0]) + "\t" + str(info[1]) + "\n")
        n = raw_input("Input: ")
else:
    print("Error: Please either input from file, or direct ISBN input." +
          "\n\t" + "Input from file:\t file.py -f ./input.txt" +
          "\n\t" + "Input directly:\t\t file.py -d 9780385495646")
    sys.exit()
