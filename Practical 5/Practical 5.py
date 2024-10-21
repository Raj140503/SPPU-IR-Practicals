# Practical 5 - Write a program to parse XML text, generate Web graph and compute topic specific page.

import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse(r"C:\Users\rajpa\OneDrive\Desktop\IR\Practical 5\Myxml.xml")

    print (doc.nodeName)
    print (doc.firstChild.tagName)
    expertise = doc.getElementsByTagName("expertise")
    print ("%d expertise:" % expertise.length)
    for skill in expertise:
        print (skill.getAttribute("name"))
    newexpertise = doc.createElement("expertise")
    newexpertise.setAttribute("name", "BigData")
    doc.firstChild.appendChild(newexpertise)
    print (" ")

    expertise = doc.getElementsByTagName("expertise")
    print ("%d expertise:" % expertise.length)
    for skill in expertise:
        print (skill.getAttribute("name"))

if __name__ == "__main__":
    main();

'''
#document
employee
4 expertise:
SQl
Python
Testing
Business

5 expertise:
SQl
Python
Testing
Business
BigData
'''