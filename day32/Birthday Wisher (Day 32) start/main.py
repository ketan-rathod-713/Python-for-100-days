import smtplib

# here we have to specify the location of email providers smtp sever and it's different for every email server providers

my_email = "ketanrtd1@gmail.com"
password = "9664738910"

connection = smtplib.SMTP("smtp.gmail.com")
# way of securing our connection to our email server, if someone intercept then that message will be encrypted
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,to_addrs="ketanrtd713@gmail.com",msg="hello")
connection.close()