# anime-minimal
#### Video Demo:  <URL HERE>
#### Description: Minimal anime website with anime related things, like search, rankings, recommended animes, a page with anime information, and user notes

# Website
Website about anime related things, using Flask, Bootstrap, Python, HTML and SCSS. [Jikan API](https://docs.api.jikan.moe/) was used to get information about animes

## Home Page 
In the home page, there are animes that might catch the user attention, like an anime recommendation, in four columns, one with the top animes (considered the best between all anime), most popular animes (by members), top airing animes (considered the best among airing anime) and top upcoming animes (considered the most anticipated animes). A pagination for each column was not implement to keep it as a simple anime recommendation with 20 animes

## Ranking 
The ranking page show animes by rank, calculated based mostly in score. The information is put in a table with 5 columns (rank, name, episodes, status, score) with each anime linked to a page with more information about it. There were doubts about which information should be displayed in the rankings along rank, name and score. In the end, it was chosen to add a column for the status, so the user knows if the anime is finished, and another column for the number of episodes, so the user can have an idea about how long it would take to finish that anime/season. The other informations that were considered to put in the table was rating, season and year, but they were excluded for being considered less important

The pagination was trick to implement, it was difficult to have a clear view of how to do it and, even when you saw it, connecting the url to a change in page using the query parameters with the API was strange thing at first, but at the end it was easy to recognize how simple it was to implement a change in page using the API

## Search 
It is a page to help the user find the anime he wishes. You can filter the animes by type(TV, Movie, OVA, etc), score(1-10), status(Airing, Finished or Upcoming), producer(studio), rating(appropriate age) and genres, and you can organize the results by ordering them by number of episodes, rank, score or title(alphabetically) in ascending or descending order using the advanced search, or you can just search the anime by name, or by name and with filters. The design of the advanced search is lacking, because no matter how many times it changed, the design was never good enough, so I just left it with a simple design, and the same went for the columns in genres

## Animes 
Show the results of the search in table like it is displayed in the rankings. If you click in the anime title, you go to a page where you can see more information about it

## Anime
The anime page shows more information about an anime chosen by the user, using the id of the anime to search for the information. There is basic things like rank, score, synopsis, type, episodes, status, season, year, etc. Now, there were some that were not chosen to be put in the page, like alternative titles and links to others site with other kinds of information about the same anime, because the page is supposed to be minimal, with jsut the important pieces of information, so some discarded information are hidden at the page. The dropdown in openings and endings is to hide them because of the difference in the number of songs in different animes, making the initial view more uniform

## Register, Login and Log Out 
Basic things found in a site. Based in the finance problem set. To register it requires a username and password, and a confirmation, where the user will be asked to reapeat the password. The usernames are unique, so each username is linked to only one account. The login requires a username and a password, and the log out cleans the session

## Notes 
Some notes the user can make by opening the page, writing in the box and clicking enter. They are linked to the user, so each user has different notes, and each note serves as a parameter for a anime search. So, if I write the name of an anime and, after that, click in the note, it will lead to a page where you can see the results of the search based in the content of the note. The login is required here, so, if you try to access while not logged in, you will be redirected to the home page 
