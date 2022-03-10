# def sentence_count(text):
#     dot = text.count(".")
#     comma = text.count(",")
#     question = text.count("?")
#     exclamation = text.count("!")
#     count = dot + comma +question + exclamation
#     return count
# text="What is your name? My name is Noufal. sdghjs, dgchs! dhfjnk."
# print(sentence_count(text))

# def word_count(sentence):
#     return len(sentence.split())

# def repeatedNumber(list):
#     counter = 0
#     number= list[0]
#     for numbers in list:
#         numberCount = list.count(numbers)
#         if numberCount > counter :
#             counter = numberCount
#             number = numbers
#     return number
# list=[1,2,3,4,5,4]
# print(repeatedNumber(list))

# from statistics import mode
# def repeated_numbers(list):
#     most_repeated= mode(list)
#     list.remove(most_repeated)
#     secondMostRepeated = mode(list)
#     return most_repeated,secondMostRepeated
# list=[1,1,2,2,2,3,4,5]
# print(repeated_numbers(list))

# def string_finding(items):
#     string = []
#     for item in items:
#         if type(item) == str:
#             string.append(item)
#     return string
# items = [1,'sdfsdf','d',3]
# print(string_finding(items))



# import os

# import requests

# from bs4 import BeautifulSoup

# def get_all_photos(base_url="https://www.gettyimages.in/photos/aamir-khan-actor"):
#     images = []
#     resp = requests.get(base_url)
#     soup = BeautifulSoup(resp.content, features="html.parser")
#     div = soup.find("div", {"class" : "GalleryItems-module__searchContent___CYdil"})
#     for images in div.find_all("a"):
#         image = images.image
#         url = images['href']
#         images.append((image, url))
#     return images


        
import string
def freq(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

def panagram(word):
    alphabets="qwertyuiopasdfghjklzxcvbnm"
    for letters in alphabets:
        if letters not in word:
            return False
    return True


def average(s):
    sum = 0
    if len(s) == 0:
        return None
    for i in s:
        sum = sum+i
    return sum/len(s)
    



