import time
from plyer import notification

if __name__ == "__main__":
	while True:
		notification.notify(
			title = "ALERT!",
			message = "Take a break",
			timeout = 10,
			app_name = "Notifier"
			#app_icon = ""
		)
		time.sleep(60) #will run after every 1 minute