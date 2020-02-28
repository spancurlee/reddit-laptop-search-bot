# reddit-laptop-search-bot
Description: Searches /r/LaptopDeals for submissions containing certain specifications and sets notifications for new submission.

Instructions:

  1. Before running the program, the user must enter their reddit account's username, password, client id, and client secret in "config.py". The client id and client secret can be obtained by going to https://www.reddit.com/prefs/apps and creating an app.
  2. To start the program, run "main.py". After starting the program, the user can enter the laptop specifications they desire (e.g. 6GB Ram, Intel i5 Processor, etc.).
  3. The program will then go through submissions on /r/LaptopDeals and find submissions that contain the given specs and send them in a list to the reddit account's inbox. The list will contain the submission title, a link to the post, and a link to purchase the laptop online.
  4. The user can then choose whether he or she wants to set notifactions for new submissions that contain the desired specs. If yes, then the bot will search for new submissions and send them them to the user's reddit inbox one every hour.
