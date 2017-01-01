# import requests
# from bs4 import BeautifulSoup

#word = input('What word do you want to run Soundex on?')
# raw = requests.get("http://www.merriam-webster.com/dictionary/" + word).text 
# soup = BeautifulSoup(raw, 'lxml')
# definitions = soup.find('ol', {'class': 'definition-list'}).contents
# for definition in definitions:
#     print(definition.text)

dict1 = dict()
dict1 = {'b': '1', 'f': '1', 'p': '1', 'v': '1', 'c': '2', 'g': '2', 'j': '2', 'k': '2','q': '2',
    's': '2', 'x': '2', 'z': '2', 'd': '3', 't': '3', 'l': '4', 'm': '5', 'n': '5', 'r': '6'}

removes = ['a', 'e', 'i', 'o', 'u', 'h', 'w']

def prep(line):
    l = list(line)
    l = [item.lower() for item in l]
    l = [l[0]] + soundex(l[1:len(l)-1])
    return ''.join(l)

def soundex(l):
    for char in l[:]:
        if char in removes:
            l.remove(char)
    for char in l:
        if char in dict1:
            l[l.index(char)] = dict1[char]
    l = [item for pos,item in enumerate(l) if l.index(item)==pos ]
    return l
    


def main():
    myword = input("what word ")
    m = prep(myword)
    file = open('dict.txt', 'r')
    for line in file:
        if m == prep(line):
            print(line)
        

main()



