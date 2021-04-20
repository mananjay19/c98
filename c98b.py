def countWordFromFile():
    #fileName=input('Enter the file name')
    file=open('abc.txt','r')
    numberOfWords=0
    for line in file:
        words=line.split(',')
        numberOfWords=numberOfWords+len(words)

    print('number of words',numberOfWords)

countWordFromFile()