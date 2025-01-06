Project Overview:
This project involves scraping data from www.worldometers.info in two phases:

Phase 1: Collect statistical data for each country, including Population, World Share, and Land Area, available at this link: https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/.

Phase 2: Using the list of countries from Phase 1 (sorted by population), gather Coronavirus data for each country, including Cases, Deaths, and Recovered statistics, available at this link: https://www.worldometers.info/coronavirus/country/india/ (Example: India).

Finally, merge all the collected data and export it to an Excel or CSV file.

Project Outcome:
Using libraries such as BeautifulSoup, Requests, and Pandas, I fetched statistical data for the first phase of the project. I created two lists: one for column titles and the other for each country's corresponding data. For gathering Coronavirus information in Phase 2, I used a for loop to iterate over the list of country names generated in the first phase. Since the titles of the data need to be fetched only once, I created a block of code with a flag called run_once, ensuring that it executes only once, even though it is inside the loop for country names.

I then saved the Coronavirus data into a 2D list, creating a complete collection of the data. Finally, I merged the results from both phases and returned both the headers and the merged data.
