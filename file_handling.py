"""All concept of file handling with python"""


#if the file is not exit
f = open("sample.txt","w")
f.write("My name is nirmal")
f.close()


t = open("Sample2.txt","w")
t.write("right now I am learing about file handling")
t.write("\n for the learing about backend developer and Data science ")
t.close()

#case2: if the file is already exit

#write a line in same file with out any replace 
t= open('sample.txt',"a")
t.write("\nThis topic is very intersteing ")
t.close()

#write a lines
l=['Hello\n','my\n','name\n','is\n','nirmal\n']
f=open("sample.txt",'w')
f.writelines(l)
f.close()



#reading from files
#>- using read()
f=open('sample.txt','r')
r=f.read()
print(r)
f.close()


#reading upto n chars
f=open('sample.txt','r')
r=f.read(15)
print(r)
f.close()

#readline() > to read line by line
f=open('sample.txt','r')
print(f.readline(),end='')
print(f.readline(),end='')
f.close()


#(vvi)) reading entire using readline
f= open("sample.txt",'r')
while True:
    data=f.readline()
    if data=='':
        break
    else:
        print(data,end='')
f.close()


# '''### Using Context Manager (With)

# - It's a good idea to close a file after usage as it will free up the resources
# - If we dont close it, garbage collector would close it
# - with keyword closes the file as soon as the usage is over'''
#with
with open('sample2.txt','a') as g:
    g.writelines("she is the one\n")


#try f.read() now
with open("sample2.txt",'r') as y:
    print(y.read())

#moving within a file -> 10 char then 10 char
with open('sample2.txt','r')as f:
    print(f.read(12))
    print(f.read(12))


#benefit? -> to laod a big file in meneory
big_l=["nirmal Rawal" for i in range(1000)]
with open("bigfile.txt",'w')as f:
    f.writelines(big_l)


with open("bigfile.txt",'r')as f:
    chink_size=10
    while len(f.read(chink_size))>0:
        print(f.read(chink_size),end= '###')
        f.read(chink_size)


#seek and tell function :
#bascially tell function tell up what print next line and seek function tell us or work as a cursur what and from where we will print next line
with open("sample2.txt",'r') as f:
    print(f.read(15))
    print(f.tell())
    print(f.seek(0))
    print(f.read(15))
    print(f.tell())
    
# #seek during write
with open('sample.txt','w')as f:
    f.write("Ujjwal")
    f.seek(4)
    f.write('hemangi')



# ### Problems with working in text mode

# - can't work with binary files like images
# - not good for other data types like int/float/list/tuples


# #working with binary file
with open('ii.HEIC','rb')as f:
    with open('yy.HEIC','wb')as i:
        i.write(f.read())

        

# - not good for other data types like int/float/list/tuples
d={
    'name':'nirmal',
    'age':21,
    'gender':'male'
}

with open('sample.txt','w')as f:
    f.write(str(d))


"""Serialization and Deserialization

Seraillization: Serialization is the process of converting the python data types to JSON format

Deserialization: Deserialization is the proecss of converting the JSON to python data types
"""
#Serialization 
import json
d={
    'name':'nirmal',
    'age':21,
    'gender':'male'
}
with open("demo.json",'w')as f:
    json.dump(d,f,indent=4)


#Deserialization
import json
with open('demo.json','r') as g:
    d =json.load(g)
    print(d)
    print(type(d))


#Serialize and deserialize tuple
import json
t=(1,2,4,5,3)
with open("demo.json",'w')as j:
    json.dump(t,j)


#Serialize and deserialize a nested dict
# import json
r ={
    "student":"Ujjwal",
    "marks":[12,32,3,2,4,2]
}

with open("demo.json",'w')as i:
    json.dump(r,i)




#Serialzing and Deserializing custom objects

class Person:
    def __init__(self,fname,lname,age,gender) -> None:
        self.fname= fname
        self.lname= lname
        self.age=age
        self.gender=gender

# #format to printed in 
# #Nirmal rawal age -->21 gender --> male

person=Person("Nirmal","Rawal",21,"male")
import json
def show_data(person):
    if isinstance(person,Person):
        return "{} {} age -->{} gender --> {}".format(person.fname,person.lname,person.age,person.gender)
    
with open("demo.json","w")as f:
    json.dump(person,f,default=show_data)



# # As a dict
class Person:
    def __init__(self,fname,lname,age,gender) -> None:
        self.fname= fname
        self.lname= lname
        self.age=age
        self.gender=gender
import json
person=Person("Nirmal","Rawal",21,"male")

def show_object(person):
  if isinstance(person,Person):
    return {'name':person.fname + ' ' + person.lname,'age':person.age,'gender':person.gender}

with open('dict.json','w') as f:
  json.dump(person,f,default=show_object,indent=4)

import json
with open("dict.json","r")as f:
   d=json.load(f)
   print(d)
   print(type(d))



#VVI topic for datascience 
"""         PICKLING   
Pickling is the porcess whereby a python object hierarchy is converted into a byte stream, and Unplicking is the inverse operations, whereby a byte stream ( from a binary file or bytes-like object) is cnverted vack into an object hieracrchy.

"""

class Student:
    def __init__(self, name, rollNo,father_name):
      self.name= name
      self.roolno= rollNo
      self.father=father_name

    def display_info(self):
      print("Hello my studnet name is ",self.name,"his roolno is",self.roolno, "and his father name is ",self.father)
      
p=Student("ram",5,"ram hari nayaran")

#pickel dumb
import pickle
with open("student.pkl",'wb')as f:
   pickle.dump(p,f)


#pickel load
import pickle
with open("student.pkl","rb") as f:
   p=pickle.load(f)

p.display_info()


"""PICKEL VS JSON:
Pickel let the user to store the data in binary format. 
JSON let the user to store the data in human readable text format.
"""
