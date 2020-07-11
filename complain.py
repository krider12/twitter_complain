#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
import twitter
import json

def test():
    print 'running test'
    try:
        a = os.popen(" /usr/bin/speedtest-cli --json").read()
        print 'ran'
        #split the 3 line result (ping,down,up)
        # lines = a.split('\n')
        print a
        j1=json.loads(a)
        p=  j1['ping']
        d=  round(j1['download']/1024**2,2)
        u=  round(j1['upload']/1024**2,2)
    except  ValueError:
        #if speedtest could not connect set the speeds to 0
        print('JSON wasn\'t set due to network issues.')
        p = 100
        d = 0
        u = 0
    
    ts = time.time()
    date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    print date,p, d, u
    #save the data to file for local network plotting
    out_file = open('data.csv', 'a')
    writer = csv.writer(out_file)
    writer.writerow((ts*1000,date,p,d,u))
    out_file.close()
    #connect to twitter
    #accss token: 1265961980139048960-IlmIegfubRu59FYrsfPhwUwteeg5XI
    # access token secret: 46TRLG8BP3FHAs5OhVkN72olsrRe8zhU3iSNgEFfJSOJn
    # API key: 81WMOjHBWngXWMW5DeKVb5Dl4

    # API secret key: FjiI0j3gxm9H230OeCzvCg3vyfB2HsDH7PX6xyx60pWGYbdS3P
    TOKEN="1265961980139048960-IlmIegfubRu59FYrsfPhwUwteeg5XI"
    TOKEN_KEY="46TRLG8BP3FHAs5OhVkN72olsrRe8zhU3iSNgEFfJSOJn"
    CON_SEC="81WMOjHBWngXWMW5DeKVb5Dl4"
    CON_SEC_KEY="FjiI0j3gxm9H230OeCzvCg3vyfB2HsDH7PX6xyx60pWGYbdS3P"
    my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
    twit = twitter.Twitter(auth=my_auth)
    #try to tweet if speedtest couldnt even connet. Probably wont work if the internet is down
    if "Cannot" in a:
        try:
            tweet="Hey @bsnlbroadband @BSNLCorporate why is my internet down? I pay for BBG Speed ULD 991 CS78, with 8Mbps down in Faridabad, Haryana. #BSNLwoes #BSNL"
            twit.statuses.update(status=tweet)
        except:
            pass
    # tweet if down speed is less than whatever I set. Here it is 8Mbps.
    elif d<5 :
        print "trying to tweet"
        try:
            # Write the twitter message. Make sure it's less than 140 characters long.
            #You can post more than one tweet each time. Make sure not to break twitter API terms.
   
            tweet="The speed now is {0} Mbps\n Upload:{1} & Ping={2}ms @SagarikaM2".format(d,u,p)
            #tweet2=
            #tw
            twit.statuses.update(status=tweet)
            #twit.statuses.update(status=tweet2)
            #twit.statuses.update(status=t
        except Exception,e:
            print str(e)
            pass
	

if __name__ == '__main__':
    while True:
    
        test()
        time.sleep(2*60)
    # print 'completed'

