def organize_contacts(contact_list):
    #Track seen emails and phones to avoid duplicates
    seen_emails = set()
    seen_phones = set()

    cleaned_contacts = []

    for contact in contact_list:
        #Standardize and validate email
        email = contact.get("email", "").strip().lower()
        if not ("@" in email and "." in email and " " not in email):
            continue

        #Clean and validate phone number (digits only)
        raw_phone = contact.get("phone", "")
        clean_phone = "".join(char for char in raw_phone if char.isdigit())
        if len(clean_phone) != 10:
            continue

        # Check for duplicate emails or phone numbers
        if email in seen_emails or clean_phone in seen_phones:
            continue

        #Mark as seen and add to cleaned list
        seen_emails.add(email)
        seen_phones.add(clean_phone)

        cleaned_contacts.append({
            "name": contact.get("name", "").strip(),
            "email": email,
            "phone": clean_phone
        })

    return cleaned_contacts


#Example test run
if __name__ == "__main__":
    test_contacts = [
        {"name": "John Doe", "email": "John@Email.com", "phone": "123-456-7890"},
        {"name": "Jane Smith", "email": "invalid_email.com", "phone": "(123) 456-7890"},  # Invalid email
        {"name": "Bob Taylor", "email": "bob@test.com", "phone": "123-45"},  # Invalid phone (< 10 digits)
        {"name": "John Duplicate", "email": "john@email.com", "phone": "999-888-7777"},  # Duplicate email
        {"name": "Alice Brown", "email": "alice@test.com", "phone": "1234567890"},  # Duplicate phone
        {"name": "Mary Jane", "email": "mary@example.com", "phone": "555.666.7777"}  # Valid
    ]

    print(organize_contacts(test_contacts))