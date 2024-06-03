import imaplib

def check_all_mailboxes(username, password):
    try:
        # Connect to the IMAP server
        imap_server = imaplib.IMAP4('https://212.182.24.27:443')

        # Login to the server
        imap_server.login(username, password)

        # Get a list of all mailboxes (folders)
        status, mailboxes = imap_server.list()
        if status == 'OK':
            total_messages = 0
            for mailbox in mailboxes:
                # Extract the mailbox name
                mailbox_name = mailbox.decode().split(' "/" ')[1]

                # Select the mailbox
                imap_server.select(mailbox_name)

                # Fetch the number of messages in the mailbox
                status, response = imap_server.status(mailbox_name, '(MESSAGES)')
                if status == 'OK':
                    messages_count = int(response[0].split()[2].strip(')'))
                    total_messages += messages_count
                    print(f"Number of messages in {mailbox_name}: {messages_count}")

            print(f"Total number of messages in all mailboxes: {total_messages}")

        # Logout from the server
        imap_server.logout()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Provide your IMAP server credentials
    username = "pasinf2017@infumcs.edu"
    password = "P4SInf2017"

    check_all_mailboxes(username, password)
