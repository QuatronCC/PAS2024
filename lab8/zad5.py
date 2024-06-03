import imaplib

def delete_message(username, password, message_id):
    try:
        # Connect to the IMAP server
        imap_server = imaplib.IMAP4('https://212.182.24.27:443')

        # Login to the server
        imap_server.login(username, password)

        # Select the Inbox folder
        imap_server.select('INBOX')

        # Mark the message for deletion
        imap_server.store(message_id, '+FLAGS', '\\Deleted')

        # Permanently delete the message
        imap_server.expunge()

        print("Message deleted successfully.")

        # Logout from the server
        imap_server.logout()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Provide your IMAP server credentials
    username = "pasinf@infumcs.edu"
    password = "P4SInf2017"

    # Provide the message ID of the message to be deleted
    message_id = "1"  # Change this to the ID of the message you want to delete

    delete_message(username, password, message_id)
