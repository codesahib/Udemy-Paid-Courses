import urllib3
import requests
import re
import time
import random
import sys
import argparse
import colorama
import json
from bs4 import BeautifulSoup
from pathlib import Path
from __banner.banner import banner
from __colors__.colors import *
from __functions.functions import *
from __constants.constants import CHECKOUT, total_sites, site_range
from urllib.parse import urlsplit, parse_qs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

func_list = [
    lambda page : discudemy(page),
    lambda page : udemy_freebies(page),
    lambda page : udemy_coupons_me(page),
    lambda page : real_disc(page),
    lambda page : tricksinfo(page),
    lambda page : freewebcart(page),
    lambda page : course_mania(page),
    lambda page : jojocoupons(page),
    lambda page : onlinetutorials(page),
]

def getRealUrl(url):
    path = url.split(".com/")[1]
    return "https://www.udemy.com/" + path


def get_course_coupon(url):
    query = urlsplit(url).query
    params = parse_qs(query)
    try:
        params = {k: v[0] for k, v in params.items()}
        return params['couponCode']
    except:
        return ''

def process(list_st, dd, limit, site_index): # Only 'list_st' is used
    print('\n')
    for index, stru in enumerate(list_st, start=1):
        sp1 = stru.split('||')
        x = re.search(".*www\.udemy\.com.*couponCode=.*",sp1[1])
        # print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + str(index), fy + sp1[0])
        # print(stru)
        if x:
            results[sp1[0]] = sp1[1]
    
    # print('\n' + fc + sd + '----' + fm + sb + '>>' + fb + ' To load more input "m" OR to subscribe any course from above input "y": ', end='')
    # input_2 = input()
    # if input_2 == 'm':
    #     if dd != limit-1:
    #         return total_sites[site_index + 1]
    # else:
    #     exit()

def main():
    # ***** Argument Generator *****
    parser = argparse.ArgumentParser(description='', conflict_handler="resolve")
    general = parser.add_argument_group("General")
    general.add_argument(
        '-h', '--help',\
        action='help',\
        help="Shows the help.")
    general.add_argument(
        '-v', '--verbose',\
        action='store_true',\
        help="Turn on debug messages")
    general.add_argument(
        '-p', '--pages',\
        type=int,\
        help="Number of pages to traverse from each site.")
    general.add_argument(
        '-s', '--sites',\
        type=int,\
        help="Number of results to get from each site.")
    # *******************
    global results, results_list
    results = {}
    results_list = []

    try:
        args = parser.parse_args()
        
        time.sleep(0.8)
        # print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fw + 'Websites Available: ')
        bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color not in bad_colors]
        # for site in total_sites:
        #     print(random.choice(colors) + site)
        
        try:
            if args.pages:
                limit = args.pages
            else:
                limit = 1
        except:
            pass

        try:
            if args.sites:
                sites = args.sites
            else:
                sites = 2
        except:
            pass
        
        if args.verbose is True:
            print("Number of sites = " + str(sites))
            print("Number of pages to traverse from each site = " + str(limit))

        global d # This indicates the page number on a website
        global s # This indicates sites visited
        s = 1
        for site_index, site in enumerate(total_sites):
            if s > sites:
                if args.verbose is True:
                    print("No of sites exceeded. Limit = " + str(sites))
                break
            if args.verbose is True:
                print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb + ' ' + site + ' ' + fm + sb + '<<' + fc + sd + '-------\n')
            d = 1 # Each new site should start with first page
            while d <= limit:
                if site == 'Discudemy':
                    list_st = discudemy(d)
                if site == 'Udemy Freebies':
                    list_st = udemy_freebies(d)
                if site == 'Udemy Coupons':
                    list_st = udemy_coupons_me(d)
                if site == 'Real Discount':
                    list_st = real_disc(d)
                if site == 'Tricks Info':
                    list_st = tricksinfo(d)
                if site == 'Free Web Cart':
                    list_st = freewebcart(d)
                if site == 'Course Mania':
                    list_st = course_mania(d)
                if site == 'Help Covid':
                    list_st = helpcovid(d)
                if site == 'Jojo Coupons':
                    list_st = jojocoupons(d)
                if site == 'Learn Viral':
                    list_st = learnviral(d)
                if site == 'Online Tutorials':
                    list_st = onlinetutorials(d)
                process(list_st, d, limit, site_index) # Just to print result or store in results dict.
                d += 1
            s += 1
        # results = {
        #     "Wireshark: Packet Analysis and Ethical Hacking: Core Skills":"https://www.udemy.com/course/learn-aspnet-mvc-and-entity-framework/?couponCode=ASPNET_JUL_FREE_3"
        # }
        # print(results)
        
        head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        json_for_export = []
        for title in results:
            course_details = {}
            link = results[title]
            # Scrap the link for details, rating and creator
            r = requests.get(link, headers=head, verify=False)
            soup = BeautifulSoup(r.content, 'html.parser')
            headline = soup.find('div', 'udlite-text-md clp-lead__headline').text
            headline = headline.replace('\n','')
            creator = soup.find('div', 'instructor-links--instructor-links--3d8_F').span.text
            creator = creator.replace('\n','').replace('Created by ','')
            rating = soup.find('span','udlite-heading-sm star-rating--rating-number--3lVe8').text
            
            course_details["title"] = title
            course_details["link"] = link
            course_details["headline"] = headline
            course_details["creator"] = creator
            course_details["rating"] = rating

            json_for_export.append(course_details)

        f = open('courses.txt','w',encoding='utf-8')
        f.write(json.dumps(json_for_export))
        f.close()
        if args.verbose is True:
            print("Total Results = " + str(len(json_for_export)))
    except Exception as e :
        print(e)
        exit('\nunknown error')

if __name__ == '__main__':
    main()