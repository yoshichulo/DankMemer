#!/usr/bin/env python3
import os
import requests
import argparse
import time
import urllib.request

from bs4 import BeautifulSoup

def ask_for_memes(output, subreddits):
    ''' Function that checks the subreddits that actually exist. If it exists, it downloads the newest memes. Else, it show an error message '''
    for sub in subreddits:
        url = "https://old.reddit.com/r/" + sub + "/new/"
        response = requests.get(url, headers={'User-Agent': 'DankMemer/v1.0 (by github.com/yoshichulo)'}, allow_redirects=False)
        if response.status_code == 200:
            parse_subreddit(output, sub, response)
        else:
            print("[WARNING] {} Subreddit was ignored (does it exist?)".format(sub))

def parse_subreddit(output, sub, r):
    ''' Function responsable of parsing the different subreddits and download their respective images '''
    print('[!] Downloading memes from r/{}...'.format(sub))
    folder_dir = output + '/' + sub
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)

    soup = BeautifulSoup(r.content, "html.parser")
    memes_div = soup.find_all("div", {"class": "thing"})
    for meme_div in memes_div:
        # On this version, only gets memes from Reddit page. Will add support for other pages like tinyimg in the future.
        if ('https://i.redd.it/' in meme_div['data-url']):
            urllib.request.urlretrieve(meme_div['data-url'], folder_dir + '/' + meme_div['data-url'].replace('https://i.redd.it/', ''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', dest='output', type=str, help="Folder you want to output the memes", default="./DankMemerMemes")
    parser.add_argument('-s', '--subreddits', dest='subreddits', type=str, help="Name of the Subreddits you want to get memes from (if you want more than 1, just sepparate them by a comma, for example: memes,dankmemes)", required=True)
    args = parser.parse_args()

    output = args.output
    subreddits = args.subreddits
    subreddits = list(subreddits.replace(' ', '').split(','))
    
    # Checks if the output directory exists. If not, it creates it.
    if not os.path.exists(output):
        os.makedirs(output)

    ask_for_memes(output, subreddits)




