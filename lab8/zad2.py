import imaplib

def check_inbox(username, password):
    try:
        # Connect to the IMAP server
        imap_server = imaplib.IMAP4('https://212.182.24.27:443')

        # Login to the server
        imap_server.login(username, password)

        # Select the Inbox folder
        imap_server.select('INBOX')

        # Fetch the number of messages in the Inbox
        status, response = imap_server.status('INBOX', '(MESSAGES)')
        if status == 'OK':
            messages_count = int(response[0].split()[2].strip(')'))
            print(f"Number of messages in Inbox: {messages_count}")

        # Logout from the server
        imap_server.logout()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Provide your IMAP server credentials
    username = "pasinf2017@infumcs.edu"
    password = "P4SInf2017"

    check_inbox(username, password)
