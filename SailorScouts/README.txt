Sailor Scouts App

This small app was created using Python and the Django framework.

The overall goal of the app is to run with all the basic CRUD functionalities ( cread, read, update, delete ) in a relatively pleasing UI enviroment. Despite not having any Javascript linked into my app, there are still a few small animations acheived through css alone. 


I started with the process of setting up the Django app, and creating the basic template and model of my site.

Rather than only utilizing Djangos block content function, I created my own custom blocks. This ensured that the speficic content I wanted to pull would be passed into the correct column on the page. 

I then moved into creating the views for the various different crud functions. Learning and inputing the correct Django syntax, I was able to create temporarily stored variables by passing in different key data points of each scout ( in most cases, the instances id or pk ). This allowed me to only have one page for each view ( rather than static html pages for each entry ). 

Lastly, I made sure that after each crud function had completed, the user was redirected back to an appropriate page ( either the home, or scout list pages ).

Note:
-	This app will not function on its own, as it is a small piece of a larger project. This upload is simply for portfolio reference purposes.

-	There may be updates to this project over time. Any additional edits will be added to the end of this file.

Thanks for reading, and I hope you enjoy taking a look at this project!!

Charissa D. / LoafyLilu
