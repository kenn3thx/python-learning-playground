from example_04 import emailProcess, printMsg

def main():
    emails = ['qyd@gmail.com', 'youtube@codexplore.dev', 'liverbool@winner.com']

    for email in emails:
        [username, domain] = emailProcess(email);

        printMsg(username, domain)


if __name__ == "__main__":
    main();