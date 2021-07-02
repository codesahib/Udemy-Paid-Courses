import urllib3
import requests
import re
import time
import random
import sys
import argparse
import colorama
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

def process(list_st, dd, limit, site_index):
    global d
    print('\n')
    for index, stru in enumerate(list_st, start=1):
        sp1 = stru.split('||')
        # print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + str(index), fy + sp1[0])
        print(stru)
    print('\n' + fc + sd + '----' + fm + sb + '>>' + fb + ' To load more input "m" OR to subscribe any course from above input "y": ', end='')
    input_2 = input()
    if input_2 == 'm':
        if dd != limit-1:
            return total_sites[site_index + 1]
    else:
        exit()


def main():
    # ***** Argument Generator *****
    parser = argparse.ArgumentParser(description='', conflict_handler="resolve")
    general = parser.add_argument_group("General")
    general.add_argument(
        '-h', '--help',\
        action='help',\
        help="Shows the help.")
    general.add_argument(
        '-n', '--num',\
        dest='num_results',\
        action='count',\
        help="Number of results to get from each site.")

    authentication = parser.add_argument_group("Features")
    authentication.add_argument(
        '-k', '--cron',\
        dest='cron',\
        action='store_true',\
        help="Added support to create a cron job/task")
    # *******************

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
            if args.cron:
                input_1 = 'n'
            else:
                input_1 = 'n'
        except:
            pass

        if input_1 == 'n':
            global d
            d = 1
            for site_index, site in enumerate(total_sites):
                if site == 'Learn Viral':
                    limit = 10
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Learn Viral ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = learnviral(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Discudemy':
                    limit = 1
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Discudemy ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = discudemy(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Udemy Freebies':
                    limit = 1
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Udemy Freebies ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = udemy_freebies(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Udemy Coupons':
                    limit = 1
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Udemy Coupons ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = udemy_coupons_me(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Real Discount':
                    limit = 4
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Real Discount ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = real_disc(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Tricks Info':
                    limit = 6
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Tricks Info ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = tricksinfo(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Free Web Cart':
                    limit = 7
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Free Web Cart ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = freewebcart(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Course Mania':
                    limit = 1
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Course Mania ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = course_mania(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Help Covid':
                    limit = 1
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Help Covid ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = helpcovid(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Jojo Coupons':
                    limit = 4
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Jojo Coupons ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = jojocoupons(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
                if site == 'Online Tutorials':
                    limit = 4
                    print('\n' + fc + sd + '-------' + fm + sb + '>>' + fb +' Online Tutorials ' + fm + sb + '<<' + fc + sd + '-------\n')
                    while d <= limit:
                        list_st = onlinetutorials(d)
                        site = process(list_st, d, limit, site_index)
                        d += 1
        
    except Exception as e :
        print(e)
        exit('\nunknown error')

if __name__ == '__main__':
    main()