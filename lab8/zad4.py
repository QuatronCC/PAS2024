import imaplib
import email

def check_unread_messages(username, password):
    try:
        # Connect to the IMAP server
        imap_server = imaplib.IMAP4('https://212.182.24.27:443')

        # Login to the server
        imap_server.login(username, password)

        # Select the Inbox folder
        imap_server.select('INBOX')

        # Search for unread messages
        status, message_ids = imap_server.search(None, 'UNSEEN')
        if status == 'OK':
            message_ids_list = message_ids[0].split()
            if len(message_ids_list) == 0:
                print("No unread messages found.")
            else:
                for message_id in message_ids_list:
                    # Fetch the message content
                    status, message_data = imap_server.fetch(message_id, '(RFC822)')
                    if status == 'OK':
                        raw_email = message_data[0][1]
                        email_message = email.message_from_bytes(raw_email)
                        print(f"Subject: {email_message['Subject']}")
                        print(f"From: {email_message['From']}")
                        print(f"To: {email_message['To']}")
                        print(f"Date: {email_message['Date']}")
                        print("\nBody:")
                        if email_message.is_multipart():
                            for part in email_message.walk():
                                content_type = part.get_content_type()
                                if content_type == 'text/plain':
                                    print(part.get_payload(decode=True).decode('utf-8'))
                        else:
                            print(email_message.get_payload(decode=True).decode('utf-8'))

                        # Mark the message as read
                        imap_server.store(message_id, '+FLAGS', '\\Seen')

        # Logout from the server
        imap_server.logout()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Provide your IMAP server credentials
    username = "pasinf2017@infumcs.edu"
    password = "P4SInf2017"

    check_unread_messages(username, password)
