from collections import namedtuple
movie = namedtuple('Movie', 'title director year')
m = movie('The Matrix', 'The Wachowskis', 1999)
n = movie('Inception', 'Christopher Nolan', 2010)
p = movie('The Godfather', 'Francis Ford Coppola', 1972)
print(m.title)  
print(n.director)  
print(p.year) 

from collections import namedtuple
book = namedtuple('Book',['title', 'author', 'year']) 
b1 = book('To Kill a Mockingbird', 'Harper Lee', 1960)
b2 = book('1984', 'George Orwell', 1949)
print(b1.title)
print(b2.author) 
print(b1.year)
print(b2.year) 
print(b1[-3]) 
print(b2[-2]) 
print(b1[-1]) 

from collections import namedtuple
import random 
import sys
dicts = {'numbers_1': [1, 2, 3], 'numbers_2': [4, 5, 6], 'numbers_3': [7, 8, 9]}
print("Size or space occupied by dictionary is: ", sys.getsizeof(dicts)) 
data = namedtuple('Data' , ['numbers_1', 'numbers_2', 'numbers_3'])
my_namedtuple = data(**dicts) 
print("Size or space occupied by namedtuple is: ", sys.getsizeof(my_namedtuple))

from collections import namedtuple
dictionary = dict({'price':500, 'no_of_pages':300, 'author':'John Doe'})
book = namedtuple('Book', ['price', 'no_of_pages', 'author']) 
print(book(**dictionary)) 
my_book = book('250','300','Jane Smith')
my_book = my_book._replace(price='250') 
print("Book Price:", my_book.price) 

from collections import Counter 
my_list = ['apple', 'apple', 'banana', 'orange', 'mango', 'banana', 'apple']  
counter = Counter(my_list) 
print(counter) 

from collections import Counter
text = "helloworld" 
counter = Counter(text)
print(counter) 

from collections import Counter
sentence = "the quick brown fox jumps over the lazy dog"
counter = Counter(sentence.split())
print(counter) 
print("The 2 most common words are:", counter.most_common(2))

from collections import defaultdict
def_dict = defaultdict(object)
def_dict['fruit'] = 'orange'
def_dict['vegetable'] = 'Carrot'
def_dict['drink'] = 'Maaza'
print(def_dict['drink'])
print(def_dict['fruit'])
print(def_dict['vegetable'])

from collections import defaultdict
def print_default():
    return 'Value Absent'
def_dict = defaultdict(print_default)
print(def_dict['Chococlate']) 

data = {'Name':'Ramya', 'Age':24, 'Place':'Chennai', 'Job':'Data Engineer', 'Company':'Accenture'}
print("This is normal dict")
for key,value in data.items():
    print(key,value)

print("---------------------------")

from collections import OrderedDict
ordered_data = OrderedDict()
ordered_data['Name'] = 'Ramya'
ordered_data['Age'] = 24
ordered_data['Place'] = 'Chennai'
ordered_data['Job'] = 'Data Engineer'
ordered_data['Company'] = 'Accenture'
print("This is an ordered dict")
for key,value in ordered_data.items():
    print(key,value) 

print("--------------------------------")

ordered_data['Place'] = 'Banglore'
for key,value in ordered_data.items():
    print(key,value) 

from collections import ChainMap
dic1 = {'chocolate':1, 'Biscuit':2, 'Ketchup':3, 'Bread':4, 'Butter':5}
dic2 = {'chennai':'Tamil', 'Delhi':'Hindi'}
dic3 = {'Job':'Software Engineer', 'location':'Banglore'}
my_chain = ChainMap(dic1,dic2,dic3)
print(my_chain.maps) 
print(list(my_chain.keys())) 
print(list(my_chain.values())) 

from collections import ChainMap
dic1 = {'red':1,'white':4}
dic2 = {'red':9,'black':8}
chain = ChainMap(dic1,dic2)
print(list(chain.keys())) 
print(list(chain.values())) 
print("original chainmap: ", chain) 
new_dic = {'blue':3, 'yellow':6}
chain = chain.new_child(new_dic)
print("chainmap after adding new dictionary is: ", chain) 
print("original chainmap: ", chain) 
chain.maps = reversed(chain.maps) 
print("reversed chainmap", str(chain)) 

from collections import UserList
L = [11,22,33,44,55,66]
user_list = UserList(L) 
print(user_list.data)

class user_list(UserList):
    def append(self,s=None):
        raise RuntimeError("Authority denied for new insertion")

my_list = user_list([11,22,33,44,55,66])
my_list.append(77) 

from collections import UserString
num = 700
user_string = UserString(num)
print(user_string.data) 

from collections import UserString
class user_string(UserString):
    def append(self, new):
        self.data = self.data + new
    
    def remove(self,s):
        self.data = self.data.replace(s, "") 

text = "Apple Orange Mango Banana Watermelon Pineapple Carrot Potato"
fruits = user_string(text)
for i in ['Carrot','Potato']:
    fruits.remove(i)  
print(fruits) 
