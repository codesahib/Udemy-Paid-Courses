# Udemy-Paid-Courses-Grabber (Web Scrapper)
Script to grab **Udemy** paid courses having coupons automatically from different websites

## ***Requirements***

- Python 3
- Python `pip`
- Python module `requests`
- Python module `colorama`
- Python module `bs4`

## ***Module Installation***

`pip install -r requirements.txt`

## ***Features***

- Fetch courses from various sites and from within pages on each site
- Many popular sites added to grab fresh/new courses (coupons).
- Generate html page from fetched courses

## ***Usage***

1. `python run.py`

##### This will by default grab courses from 1 page across 2 sites

2. `python --help`

##### Open help

3. `python --sites SITES --pages PAGES`
E.g.
`python --sites 2 --pages 3`

##### This will grab courses from 3 page across 2 sites.


