import app
import env


#Sensitive data is kept in untracked environment variables
username = env.USER
password = env.PASSWORD

#Instantiate the Twitterbot and call login
blenderfriender = app.TwitterBot(username, password)
blenderfriender.login()
