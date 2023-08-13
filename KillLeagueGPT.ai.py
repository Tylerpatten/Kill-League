import os

def main():
    if any('LeagueClient.exe' in s for s in os.popen('tasklist').readlines()):
        os.system('taskkill /f /im LeagueClient.exe')

main()