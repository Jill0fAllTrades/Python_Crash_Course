
glossary = {
    'dictionary': 'a collection of key-value pairs',
    'list': 'collection of items in a particular order',
    'method': 'an action python can perform on a piece of data (a function)',
    'string': 'a series of characters. anything within quotes.',
    'comprehensions': 'combines a for loop and creation of new list element',
    'key-value pair': 'a key is connected to a value within a dictionary',
    'conditional tests': 'expressions that can be evaluated only as True' +
    ' or False',
    'Tuple': 'an unchangeable list',
    
    }
     
for term, definition in glossary.items():  
        print(term.title() + ":" + "\n")
        print("\t" + definition + "\n")
        
#TODO add 5 more python terms to glossary and check if they print
