import time

def countdown_timer(seconds):
    """
    Countdown timer that counts down from a given number of seconds.

    Parameters:
    seconds (int): The number of seconds for the countdown.

    Returns:
    None
    """
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    # Example usage
    countdown_seconds = 10  # Number of seconds for the countdown
    countdown_timer(countdown_seconds)
