import os

def main():
    while True:
        if any('LeagueClient.exe' in s for s in os.popen('tasklist').readlines()):
            os.system('taskkill /f /im LeagueClient.exe')

main()