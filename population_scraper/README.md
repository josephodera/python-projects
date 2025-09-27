#  Countries by Population Scraper

This project scrapes the **latest population data** of countries and regions from [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population), cleans it, and saves it into both **CSV** and **Excel** formats for easy analysis.

---

##  What it does
- Fetches population data directly from Wikipedia.  
- Cleans the table (removes messy values, fixes columns, formats percentages).  
- Saves the results into:
  - `countries_by_population_clean.csv`  
  - `countries_by_population_clean.xlsx` (with bold column headers ).  

---

##  Technologies Used
- [Python 3](https://www.python.org/)  
- [pandas](https://pandas.pydata.org/) – data handling  
- [requests](https://docs.python-requests.org/) – fetching the web page  
- [lxml](https://lxml.de/) – HTML parsing for pandas  
- [XlsxWriter](https://xlsxwriter.readthedocs.io/) – formatting Excel output  

---

##  How to Run

1. **Clone this repo** or download the code.  
   ```bash
   git clone https://github.com/josephodera/countries-population-scraper.git
   cd countries-population-scraper



