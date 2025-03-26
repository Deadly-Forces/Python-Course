import time
import datetime
import pygame
import os  # Import os module to check file existence

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Mini Projects/samsung_s7_dance_party.mp3"
    
    # Check if the sound file exists
    if not os.path.exists(sound_file):
        print(f"Error: Sound file '{sound_file}' not found.")
        return

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake UP!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            print("Press Ctrl+C to stop the alarm.")
            try:
                while True:
                    if not pygame.mixer.music.get_busy():
                        break  # Exit loop when music stops
                    time.sleep(1)  # Allow the music to play
            except KeyboardInterrupt:
                print("Alarm stopped.")
                pygame.mixer.music.stop()
            finally:
                is_running = False  # Ensure the main loop exits
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm in format HH:MM:SS: ")
    set_alarm(alarm_time)
