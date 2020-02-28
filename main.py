##############################################################################
#
# Imports

import inputs
import search_reddit
import message
import time

##############################################################################
#
# Script

if __name__ == '__main__':
    user_specs = inputs.get_laptop_specs()
    links = search_reddit.search_submissions(user_specs)

    if len(links) != 0:
    	message.send_message(user_specs,links)
    else:
    	print("Unable to find any laptops that fit the specifications")

    while True:
        enable_notifications = str(input("\nWould you like to enable notifications for new submissions that match your specifications (yes/no)?: "))
        if enable_notifications.lower() ==  "yes":
            while True:
                notification_links = search_reddit.search_submissions(user_specs,True)
                if len(notification_links) != 0:
                    print("A new laptop has been found")
                    message.send_message(user_specs,notification_links)
                else:
                    print("No new submissions that fit the specifications -- checking again in 1 hour")
                    time.sleep(3600)
        elif enable_notifications.lower() == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please enter either 'yes' or 'no'")

