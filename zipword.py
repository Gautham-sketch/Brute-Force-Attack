import zipfile
import time

folder_path = input("Path to file :- ")
zipf = zipfile.ZipFile(folder_path)
global result
result = 0
global tried
tried = 0
c=0

if not zipf:
    print('The zipped file/folder is not password protected ! You can successfully open it !')

else :
    startTime = time.time()
    wordListFile = open('wordlist.txt', 'r', errors='ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')

    if result == 1:
        for i in range(len(words)):
            word = words[i]
            password = word.encode('utf-8').strip()
            c = c+1
            print('Trying to decode password by : {} '.format(word))

            try:
                with zipfile.ZipFile(folder_path, 'r') as zf:
                    zf.extractall(pwd=password)
                    print("Success! The password is: "+ word)
                    endTime = time.time()
                    duration = endTime - startTime
                    print("Congratulations! Password found in " + str(duration) + "seconds!")
                    print("In " + str(c) + "times")
                    result = 1
                    break
            except:
                pass

    if result == 0:
        print("Sorry, password not found. A total of " + str(c) + "+ possible combinations tried in " + str(duration) + "seconds. Password is not of 4 characters.")