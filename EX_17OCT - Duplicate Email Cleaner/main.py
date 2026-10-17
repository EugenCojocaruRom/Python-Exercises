#Print header and separator
print("<-- Duplicate Email Cleaner -->")
print("-------------------------------")

#Have a list of emails
emails = [
    "Anna@Example.com",
    "  bob@example.com",
    "anna@example.com ",
    "carol@Example.com",
    "BOB@example.com",
    "dave@example.com",
    "carol@example.com",
    "eve@example.com  ",
    "frank@gmail.com",
    "grace@yahoo.com",
    " heidi@gmail.com",
    "Frank@Gmail.com"
]

#Clean the emails
clean_emails = [email.strip().lower() for email in emails]
#Create empty list to store the unique emails
#unique_emails = list(dict.fromkeys(clean_emails))
unique_emails = []
#Loop over the clean emails list
for email in clean_emails:
    #Check that the email is not already in the list
    if email not in unique_emails:
        #Add the email to the list
        unique_emails.append(email)

#Print header
print(" == Unique emails ==")
#Loop over the unique emails list and list them
for i, email in enumerate(unique_emails, start=1):
    print(f" {i}. {email}")

#Print header
print("\n == Report ==")
print(f" -> Initial number of emails: {len(emails)}")
print(f" -> Number of unique emails: {len(unique_emails)}")
print(f" -> Number of duplicate emails: {len(emails) - len(unique_emails)}")

#Count the unique emails per domain
domain_counts = {}
#Loop over the unique emails list
for email in unique_emails:
    #Split the emails at the "@" sign, so the domain is at index 1
    domain = email.split("@")[1]
    #Use get(domain, 0) to return 0 the first time we see a domain
    domain_counts[domain] = domain_counts.get(domain, 0) + 1

#Print header
print("\n == Emails per domain ==")
for domain, count in sorted(domain_counts.items(), key=lambda item: item[1], reverse=True):
    print(f" {domain}: {count}")