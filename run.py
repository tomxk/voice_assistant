import os
import config
import datetime
import webbrowser
from functions.main_functions import speak, get_audio
from functions.simple_functions import get_time, get_today_date
from functions.weather_functions import get_temperature, get_weather
from functions.network_functions import (search_youtube, search_google, search_wikipedia,
                                        play_first_youtube, play_nth_youtube, send_email,
                                        create_email)


if __name__ == '__main__':

    speak('Hej Tomek!')

    while True:
        text = get_audio()

        if text != None:
            if 'hej' in text:
                speak('Tak?')

                while True:
                    text = get_audio()
                    if text != None:

                        # Greetings
                        if 'cześć' in text or 'witaj' in text or 'hej' in text or 'dzień dobry' in text:
                            speak('Cześć, co u ciebie?')

                        # Questions
                        elif 'co u ciebie' in text or 'co tam' in text or 'co słychać' in text:
                            speak('W porządku! A u ciebie?')

                        # Other questions
                        elif 'a u ciebie' in text or 'a tam' in text:
                            speak('W porządku!')
                            speak('Co jeszcze mogę dla ciebie zrobić?')

                        # Thanks
                        elif 'dzięki' in text or 'dziękuję' in text:
                            speak('Nie ma za co')


                # TIME AND DATE

                        # Time
                        elif 'która godzina' in text or 'jaki czas' in text:
                            speak(get_time())
                            speak('Co jeszcze mogę dla ciebie zrobić?')

                        # Date Today
                        elif 'który dzisiaj' in text or 'jaka data' in text:
                            speak(get_today_date())
                            speak('Co jeszcze mogę dla ciebie zrobić?')


                # WEATHER

                         # Get current temperature
                        elif 'temperatura' in text or 'temperaturę' in text:
                            speak(get_temperature(config.city))
                            speak('Co jeszcze mogę dla ciebie zrobić?')

                         # Get current temperature
                        elif 'jaka' in text and 'pogoda' in text:
                            speak(get_weather(config.city))
                            speak('Co jeszcze mogę dla ciebie zrobić?')


                # OPEN APPS - ONLY FOR LINUX UBUNTU USERS

                        # OPEN LIBREOFFICE WRITER IF EXISTS
                        elif 'otwórz word' in text:
                            os.system('libreoffice --writer')

                        # OPEN LIBREOFFICE CALC IF EXISTS
                        elif 'otwórz excel' in text:
                            os.system('libreoffice --calc')

                        # OPEN LIBREOFFICE DRAW IF EXISTS
                        elif 'otwórz powerpoint' in text:
                            os.system('libreoffice --draw')

                        # OPEN GIMP IF EXISTS
                        elif 'otwórz gimp' in text:
                            os.system('gimp')

                        # OPEN SUBLIME TEXT IF EXISTS
                        elif 'otwórz edytor' in text:
                            os.system('subl')

                        # OPEN GOOGLE CHROME IF EXISTS
                        elif 'otwórz chrome' in text:
                            os.system('google-chrome')


                # OPEN NETWORK SITES

                        # Open Google
                        elif 'otwórz google' in text or 'włącz google' in text:
                            webbrowser.open('https://www.google.com/', new=2)
                            speak('Co jeszcze mogę dla ciebie zrobić?')

                        # Open Youtube
                        elif 'otwórz youtube' in text or 'włącz youtube' in text:
                            webbrowser.open('https://www.youtube.com/', new=2)
                            speak('Co jeszcze mogę dla ciebie zrobić?')

                        # Open Gmail
                        elif 'otwórz gmail' in text or 'włącz gmail' in text:
                            webbrowser.open('https://www.gmail.com/', new=2)
                            speak('Co jeszcze mogę dla ciebie zrobić?')

                        # Open Facebook
                        elif 'otwórz facebook' in text or 'włącz facebook' in text:
                            webbrowser.open('https://www.facebook.com/', new=2)
                            speak('Co jeszcze mogę dla ciebie zrobić?')


                # SEARCH NETWORK SITES

                        # Search Youtube for smth
                        elif 'znajdź' in text and 'youtube' in text or 'znajdź' in text and 'youtubie' in text or 'szukaj' in text and 'youtube' in text or 'szukaj' in text and 'youtubie' in text:
                            search_youtube(text)

                            speak('Chcesz coś włączyć?')
                            decision = get_audio()

                            if decision != None:

                                if 'tak' in decision or 'proszę' in decision or 'włącz' in decision:
                                    speak('Który film?')
                                    number_video = get_audio()

                                    if 'pierwszy' in number_video:
                                        play_nth_youtube(text, 0)
                                    elif 'drugi' in number_video:
                                        play_nth_youtube(text, 1)
                                    elif 'trzeci' in number_video:
                                        play_nth_youtube(text, 2)
                                    elif 'czwarty' in number_video:
                                        play_nth_youtube(text, 3)
                                    elif 'piąty' in number_video:
                                        play_nth_youtube(text, 4)
                                    elif 'szósty' in number_video:
                                        play_nth_youtube(text, 5)
                                    elif 'siódmy' in number_video:
                                        play_nth_youtube(text, 6)
                                    elif 'ósmy' in number_video:
                                        play_nth_youtube(text, 7)
                                    elif 'dziewiąty' in number_video:
                                        play_nth_youtube(text, 8)
                                    elif 'dziesiąty' in number_video:
                                        play_nth_youtube(text, 9)

                            else:
                                speak('Co jeszcze mogę dla ciebie zrobić?')


                        # Search Google for smth
                        elif 'znajdź' in text and 'google' in text or 'szukaj' in text and 'google' in text:
                            search_google(text)
                            speak('Co jeszcze mogę dla ciebie zrobić?')


                        # Search Wikipedia for smth
                        elif 'znajdź' in text and 'wikipedia' in text or 'znajdź' in text and 'wikipedii' in text or 'szukaj' in text and 'wikipedia' in text or 'szukaj' in text and 'wikipedii' in text:
                            search_wikipedia(text)
                            speak('Co jeszcze mogę dla ciebie zrobić?')


                # PLAY YOUTUBE SONG

                        # Play 1st result Youtube search
                        elif 'puść' in text or 'włącz' in text:
                            play_first_youtube(text)


                # MAIL

                        # Send mail
                        elif 'wyślij mail' in text or 'wyślij email' in text:
                            speak('Do kogo wysłać?')
                            receiver = input('Odbiorca: ')
                            speak('Podaj temat.')
                            subject = get_audio()
                            speak('Podaj treść maila.')
                            message = get_audio()

                            email = create_email(login=config.login, receiver=receiver,
                                                  subject=subject, message=message)

                            speak('Czy na pewno wysłać?')
                            decision = get_audio()

                            if 'tak' in decision or 'proszę' in decision or 'wyślij' in decision:
                                send_email(login=config.login, password=config.password,
                                            receiver=receiver, content=email)
                                speak('Wysłano.')
                                speak('Co jeszcze mogę dla ciebie zrobić?')
                            else:
                                speak('Co mam teraz zrobić?')


                        # Sleep
                        elif 'śpij' in text or 'idź spać' in text:
                            print('sleep')
                            break

                        # If don't understand
                        else:
                            speak('Nie rozumiem, czy możesz powtórzyć?')


                    # Default timeout is 5 sec so if there is no speeach recognized
                    # after 5 sec assistant is going to sleep
                    # TIMEOUT IS SET FOR 15 SEC IN main_functions.py
                    else:
                        print('sleep')
                        break
