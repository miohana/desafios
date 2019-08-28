###
### Author: Mikaeri Ohana
### Date: 8/27/2019
###

import sys
from bs4 import BeautifulSoup as soup
import requests
import re

subreddit_list = sys.argv[1].split(';')
MAIN_URL = 'https://old.reddit.com/r/'

def main():
        print('Starting...\n')
        crawl(subreddit_list)

def crawl(subreddits):
        for index, subreddit in enumerate(subreddit_list, 0):
                html_request = requests.get(MAIN_URL+subreddit_list[index]).text
                html_soup = soup(html_request, 'html.parser')
                body = html_soup.find('div', {'class': 'sitetable linklisting'})
                print(body)

                posts = body.findAll('div', id=re.compile('thing_t3'))

                print('Subreddit: ', subreddit)
                print(posts)

                for post in posts:
                        upvotes = post.findAll('a', {'class':'score unvoted'})
                        thread_title = post.findAll('a', {'class':'title may-blank'})
                        comments_link = post.findAll('a', {'class':'bylink comments may-blank'}).get('href')

                        print('Upvotes: ', upvotes.text)
                        print('Thread title: ', thread_title.text)
                        print('Thread comments: ' + comments_link.text)
                        print('Thread link: ' + comments_link.text)
                        print('#####################\n')
        
if __name__ == "__main__":
	main()