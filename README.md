# IMDb-API

This is a flask application that allows the user to interact with the IMDb API provided by RAPID API.

This application was done with the purpose of learning APIs and understand their requests and their use. The web application works by searching a word or phrase that will be used as paramter to a search query given by a GET request thru IMDb API. It will return back a JSON response that will hold the movies that are more similar to the input entered. Then, movies found will appear with the use of FlexBox and Flex Wrap to order them correctly and display them nicely.

Each movie will show its name, year of release, and IMDb rank. 

This application uses Flask Sessions in order to save the user history search. This history search is given in the History tab provided in the Nav Bar. Additionally, there is an Information tab to see the mission and purpose of the web site.

This is a simple project with the main goal of using Flask and APIs together.

Enjoy :)
