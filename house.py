#import the required packages/libs
from craigslist import CraigslistForSale, CraigslistHousing 
import pandas as pd
import webbrowser
import smtplib
import time
class color:
   BOLD = '\033[1m'
   END = '\033[0m'

already_checked = [] #hold the list of already emailed listings
temp = [] #store the list of urls to later be added to already_checked
email_msg = [] #store the set of listings from the search to be emailed at the end of the loops of calls

#read in existing postings
f = open("searched.txt", "r")
already_checked = f.readlines()
f.close()
# remove whitespace characters like `\n` at the end of each line
already_checked = [x.strip() for x in already_checked] 

#define the send email function, so that lists of results can be sent via email
def send_email(body, sender, recipients, subject):
    msg = 'Subject: {}\n\n{}'.format(subject, body)
    smtpserver = 'smtp.gmail.com:587'
    try:
        server = smtplib.SMTP(smtpserver)
        server.ehlo()
        server.starttls()
        server.login('thefifthfox0@gmail.com', 'computerfox')
        server.sendmail(sender, recipients, msg)
    except Exception as e:
        print(e)

#Search craigslist for cars and perform the necessary functions based on the parameters provided
def search_craigslist_for_houses(zipcode,openlinks,email,printheader):
    
    #Declare some initial variables
    msg = [] 
    
    #Pull data based on parameters
    house_1 = CraigslistHousing(site='philadelphia', category='housing', 
                         filters={'zip_code':zipcode,'search_distance':1,'min_bedrooms':2,'min_price': 0, 'max_price': 2700, 
                                  'min_ft2':1200,'cats_ok':True,'query':'parking'})
    #Print title if desired
    if printheader == True:
        header = ''
        header = str(zipcode) + ' Apartments/Houses'
        print(header)
    
    #Loop through the results
    for x in house_1.get_results():
        
        #Also only return results that are not in the already_checked list
        if (x['url'] in already_checked) == False:
            msg.append('Posted: {} Price: {} Link: {}'.format(x['datetime'], x['price'], x['url']))
            email_msg.append('Posted: {} Price: {} Link: {}'.format(x['datetime'], x['price'], x['url'])) 
            #Temporary holding of URL from the search results as a list to use as filter against the already_checked list
            temp.append(x['url'])
            
            #Open urls in webbrowser if desired
            if openlinks == True:
                webbrowser.open(x['url'])
    
    #Send email with search results if desired and search results exist
    if email == True and len(msg) > 0:
        send_email('\n'.join(msg), 'thefifthfox0@gmail.com', ['Qman2386@gmail.com'], header)
    
    #Print out the search results to the console 
    for _ in msg:
        print(_)

#Search all sites for data
start = time.clock()
search_craigslist_for_houses(19103,False,True,True)
search_craigslist_for_houses(19104,False,True,True)
end = time.clock()
print("It took approx " + color.BOLD + str(round((end-start)/60)) + " minutes " + color.END + "to run this program")

#append postings to the file
with open("searched.txt", 'a+') as file_handler:
    for item in temp:
        file_handler.write("{}\n".format(item))