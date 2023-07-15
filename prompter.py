def ask_ok(prompt, retry = 4, reminder = "Please try again later"):
    while True:
        ok = input(prompt)
        if ok in ("y", "Y"):
            return True
        if ok in ("n", "N"):
            return False
        retry = retry - 1
        if retry < 0:
            raise ValueError('invalid response')
        print(reminder)
ask_ok("Continue?")