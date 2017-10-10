students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in students:
    print i["first_name"],
    print i["last_name"]
    # for value in data:
    #     print value["first_name"]
    #     print value["last_name"]users = {

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for label in users:
        count = 0
        print label
        for name in users[label]:
            count += 1
            first_name = name['first_name'].upper()
            last_name = name['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(count, first_name, last_name, length)
