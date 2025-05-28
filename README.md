# AFL-Tables-Scraper
The purpose of this system is to scrape the AFL Tables data repository's interface (https://afltables.com/afl/afl_index.html) and allow users to access data programattically. AFL Tables is a widely used data repository that stores all key data points about any given match played in history (for matches pre-1965, this is typically only goal scorers and scorelines). 


## Context
The AFL Table's website provides an excellent suppy of data. However, all team average statistics are overriden after each round to account for any new matches played. At the time of writing, all data is relevant up to round 11 of the 2025 AFL season. This means that if a user wanted to search for statistical averages (for example, the team that averaged the most handballs) up until round 10, a user would either have to manually collate the data up until round 10 themselves or calculate a new average without the results from the round 11 match. Additionally, the user could make use of a service such as the Wayback Machine to find snapshots of data at any given time provided a snapshot exists. Whilst these methods of accounting for the new match that the user wants to ignore are not intrinsically difficult, the work required can become far more difficult when the search is more fine tuned. For example, if a user wanted to find the team that averaged the most handballs between round 5, 2023 and round 5, 2024, they would be forced into manually collating the data from those matches themselves. 

**A representation of this problem is displayed below:**
