with open("emails.txt", "r") as file:
    emails = file.readlines()

# Strip newline characters and add a comma at the end of each email
emails = [email.strip() + "," for email in emails]

with open("emails.txt", "w") as file:
    file.write("\n".join(emails))
