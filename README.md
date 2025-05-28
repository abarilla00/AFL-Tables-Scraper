# AFL-Tables-Scraper
The purpose of this system is to scrape the AFL Tables data repository's interface (https://afltables.com/afl/afl_index.html) and allow users to access data programattically. AFL Tables is a widely used data repository that stores all key data points about any given match played in history (for matches pre-1965, this is typically only goal scorers and scorelines). 


## Context
The AFL Table's website provides an excellent suppy of data. However, all team season average statistics are overriden after each round to account for any new matches played. At the time of writing, all data is relevant up to round 11 of the 2025 AFL season. This means that if a user wanted to search for statistical averages (for example, the team that averaged the most handballs) up until round 10, a user would either have to manually collate the data up until round 10 themselves or calculate a new average without the results from the round 11 match. Additionally, the user could make use of a service such as the Wayback Machine to find snapshots of data at any given time provided a snapshot exists. Whilst these methods of accounting for the new match that the user wants to ignore are not intrinsically difficult, the work required can become far more difficult when the search is more fine tuned. For example, if a user wanted to find the team that averaged the most handballs between round 2 and round 10, they would be forced into manually collating the data from those matches themselves. Further, finding statistical averages that cross over a season into the next/previous season requires even more in-depth manual collation.

A **representation of this problem** is displayed below:

![Diagram outlining the reason behind the system](/Images/Context&#32;Diagram.png)

## Project
This project aims to deliver a system that will scrape the AFL Table's interface for data automatically when requested via a user interface. This removes the need for the user to to have to manually collate data themselves. The BeautifulSoup4 library will be deployed to scrape enitre webpages and seperate the raw HTML into workable data (often in tabular form). This data will then be used to instantiate a variety of objects that will connect to eachother via ID's that are either pre-determined or retrieved from the AFL Table's URL. For example, season's have a simple ID referencing the year in which that season occured, but a given match has a unique ID generated on AFL Table's end.

A **high-level system architecture diagram for this project** is displayed below:
![System Architecture](/Images/System&#32;Diagram.png)
