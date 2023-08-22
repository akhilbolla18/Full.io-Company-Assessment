import requests
import re
from bs4 import BeautifulSoup


def extract_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        social_links = []
        emails = []
        contacts = []

        # Find social media links
        social_media_patterns = [r'(https?://(www\.)?facebook\.com/\S+)',
                                 r'(https?://(www\.)?linkedin\.com/company/\S+)']
        for pattern in social_media_patterns:
            matches = re.findall(pattern, str(soup))
            social_links.extend([match[0] for match in matches])

        # Find emails
        email_pattern = r'[\w\.-]+@[\w\.-]+'
        emails = re.findall(email_pattern, str(soup))

        # Find contact numbers
        contact_pattern = r'(\+\d{1,2}\s?\d{3}\s?\d{3}\s?\d{4})'
        contacts = re.findall(contact_pattern, str(soup))

        return social_links, emails, contacts
    else:
        return [], [], []


# Get user input
url = input("Enter the website URL: ")

social_links, emails, contacts = extract_info(url)

print("Social links:")
for link in social_links:
    print(link)

print("\nEmails:")
for email in emails:
    print(email)

print("\nContacts:")
for contact in contacts:
    print(contact)
