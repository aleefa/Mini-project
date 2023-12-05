from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.neighbors import KNeighborsClassifier

fullword=[]
dclass=[]
import csv
# import these modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# choose some words to be stemmed
# words = ["program", "programs", "programmer", "programming", "programmers"]
#
# for w in words:
# 	print(w, " : ", ps.stem(w))


file = open(r'C:\Users\Aleefa\Desktop\New folder\career_navigator\career_app\example.csv',encoding='utf-8')

type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
#print(header)
result_row=[]
num=['0','1','2','3','4','5','6','7','8','9']
rows = []
i=0
for row in csvreader:
    if i!=0:

        rows.append([row[0].lower(),row[1].lower().replace("-"," ")])


    i=i+1
#print(rows)

ii=0
for i in rows:


    example_sent = i[1]


    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(example_sent)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            lis=[]
            my_string = w
            only_characters = ""

            for char in my_string:
                if char.isalpha():
                    if char!="-" and char!="-" and char not in num:
                        only_characters += char
                    else:
                        lis.append(only_characters)
                        only_characters = ""
                elif char==" ":
                    lis.append(only_characters)
                    only_characters=""
            else:
                lis.append(only_characters)
            #print(only_characters)
            # Output: "HelloWorld"
            for ww in lis:
                if len(ww)>=3:
                    w=ps.stem(w)
                    if w not in fullword:
                        fullword.append(w)
                    filtered_sentence.append(w)

    #print(word_tokens)
    print(i[0],"---->",' '.join(filtered_sentence))
    rr=[i[0],' '.join(filtered_sentence)]
    if i[0] not in dclass:
        dclass.append(i[0])
    result_row.append(rr)


import csv

# Define the data to be written to the CSV file


# Define the file name and location
filename = 'example.csv'

# Open the file in write mode
with open(filename, 'w', newline='',encoding='utf-8') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows(result_row)

# Print a message to confirm that the file has been written
print('The file "{filename}" has been written successfully!')



print(fullword)
print(dclass)
print(len(fullword))
print(len(dclass))


x=[]
y=[]
for i in result_row:
    y.append(dclass.index(i[0]))
    row=i[1].split(" ")
    xrow=[]
    for j in fullword:
        if j in row:
            xrow.append(1)
        else:
            xrow.append(0)
    x.append(xrow)

print((x[0]))
print(len(x))


import numpy as np
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test= train_test_split(x,y, test_size=0.20)
model = KNeighborsClassifier(n_neighbors=1)

model.fit(x, y)



# model.fit(X_train, y_train)

# y=model.predict(X_test)
# y2=model.predict(X_train)
#
# from sklearn.metrics import accuracy_score
# score =accuracy_score(y, y_test)
# print(score)
#
# score2 =accuracy_score(y2, y_train)
# print(score2)
#
# from sklearn.metrics import classification_report,confusion_matrix
#
# cm = confusion_matrix(y_test, y)
# print("confusion_matrix")
# print(cm)
#
# print("\nCR by library method=\n",
#       classification_report(y_test, y))
#

def predict(txt):

    checkwd=[]
    word_tokens = word_tokenize(txt.lower())

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            lis = []
            my_string = w
            only_characters = ""

            for char in my_string:
                if char.isalpha():
                    if char != "-" and char != "-" and char not in num:
                        only_characters += char
                    else:
                        lis.append(only_characters)
                        only_characters = ""
                elif char == " ":
                    lis.append(only_characters)
                    only_characters = ""
            else:
                lis.append(only_characters)
            # print(only_characters)
            # Output: "HelloWorld"
            for ww in lis:
                if len(ww) >= 3:
                    w = ps.stem(w)
                    checkwd.append(w)

    xrow = []
    for j in fullword:
        if j in checkwd:
            xrow.append(1)
        else:
            xrow.append(0)
    print(xrow,"=======================")
    s=sum(xrow)
    y2 = model.predict([xrow])
    print(s)
    if s<=2:
        return "Invalid Resume"
    return dclass[y2[0]]



import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        txt=""
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text = page.extract_text()
            txt=txt+text+" "
        return txt
# res=read_pdf("DOC-20210825-WA0027_.pdf")
#
# print(predict('''HUDA MP
# Front End Developer - React Native
# Experienced React Native developer with a strong track record of creating cross-platform mobile applications. Proﬁcient in JavaScript and mobile app
# development.My expertise is in creating iOS and Android applications using React Native along with strong knowledge of Firebase, Maps, Push
# Notiﬁcations, REST APIs, gRPC calls, and unit testing with Jest, Enzyme, and the Testing Library.
# hudamp76@gmail.com
# +91 9995341205
# Darul Ihsan House, Chennamangallur PO, Mukkam,
# Calicut,Kerala 673602, Calicut, India
# WORK EXPERIENCE
# Software Developer
# HTC Global Services •
# 02/2021 - Present
# ,
#
# Bangalore, Karnataka
# Developed Applications in both IOS and Android using React Native
# framework
# Worked on GRPC,Unit testing using jest testing, Firebase
# integration,Updating locations, Maps integration
# Writing unit test cases for each module using jest testing
# Coordinating with QA team for ﬁxing bugs
# Developing Flutter application
# Integrating Data wedge scanning with React native application
# Software Developer
# Adox Solutions
# 09/2018 - 02/2021
# ,
#
# Calicut, Kerala
# Developed and designed the ﬂow of Application from the provided
# design prototypes and integrating it with functionalities.
# Worked on both Mobile Applications with React Native and Web
# Applications
# Integrated Firebase, Maps API in React Native Application
# Hands on experience on developing web applications using
# codeigniter and core PHP.
# Developing APIs
# Interacted with client for better understanding and quality
# application
# Developed clean code and Ensuring quality and performance of the
# applications
# Deployed Application in Play store and AppStore
# EDUCATION
# BTECH in Information Technology
# University of Calicut
# 08/1014 - 06/2018
# ,
#
# Calicut, Kerala
# Completed Bachelor’s in
# technology (Information
# Technology) with CGPA 7.0
# SKILLS
# JavaScript
# React Native
# Redux
# Gradle
# HTML
# CSS
# Firebase
# UI/UX Design
# Third-party Libraries
# Navigation
# RESTful API Integration
# PHP
# CodeIgniter
# jQuery
# Jest
# Enzyme
# PROJECTS
# Meijer-IMS Backroom
# IMS Backroom location management application in which users can create
# container address, create address for containers, map the container and
# address. It provides scanning of barcodes of container label,address label
# and prduct(item labels) to get the details. Users can update the container
# and items mapped to it accordingly from the application. It also contains
# SSO authentication.
# HeartsApp
# HeartsApp is a Meditation and Relaxation application which provides users
# 24/7 meditation with trainer anywhere from the world. It enables you to
# reﬂect upon our inner transformation during meditation. Features include
# ﬁrebase integration, GRPC call, Push Notiﬁcations, locating trainers,
# updating location using Google Maps API
# ALMAS RESTAURENT
# Almas Restaurant is a food delivery application based in Saudi Arabia. This
# Brings all kind of food from all around the world to single application. This
# app allows customers to view menus and place order. Features include
# Google MAP location tracking, Firebase integration, Mobile number login
# with OTP, Google Maps Integration.
# Anarc HRMS
# Anarc is a HRMS application for Employees of Anarc builders and
# architectures. There will be three logins for the application, Admin,
# subadmin and employee. Employees can enter the timing of duty, site
# details, apply for leave, download project plan from the application.
# LANGUAGES
# English
# Full Professional Proﬁciency
# Hindi
# Professional Working Proﬁciency
# Malayalam
# Native or Bilingual Proﬁciency
# SKILLS
# Analytical Thinking
# Planning
# Time Management
# Problem Management
# Communication
# Organizational Skills
# Achievements/Tasks
# Achievements/Tasks
# Courses  '''))