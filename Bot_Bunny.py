import tweepy
import time
import random
import sys

print('This is bot bunny')

Consumer_Key=''
Consumer_Secret=''
Access_Key=''
Access_Secret=''

Auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
Auth.set_access_token(Access_Key, Access_Secret)
api=tweepy.API(Auth)



FILE_NAME = "last_seen_id.txt"
FILE_NAME_BB = "BB_Songs.txt"


#Get out of loop function
out=True
def exit():
    if(out):
        keyboard=input('Done? ')
        if(keyboard!=None):
            sys.exit(0)

def retrieve_songs(file):
    array = []
    with open(file) as file:
        array = file.readlines()
    return array

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...')
    BB_Songs=retrieve_songs(FILE_NAME_BB)

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text)

        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if  'dia' in mention.full_text.lower():
            print('Found plebeyos!')
            print('responding back...')
            song = random.randint(0, len(BB_Songs))
            print('entrando?')
            print(len(BB_Songs))
            yo = api.get_user(mention.author.screen_name)
            api.send_direct_message(yo.id,mention.author.screen_name+' tu cancion del dia de Bad Bunny es -> '+BB_Songs[song])
            print('song sent!')


while True:
    reply_to_tweets()
    #exit()            #Function to stop the program
    time.sleep(5)
