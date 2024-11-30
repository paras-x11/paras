contacts = [
    {
        'A': [
            {
                'Aman':{
                    'phone': '1234567890',
                    'email': 'aman@gmail.com'
                },
                'Ajay':{
                    'phone': '9876543210',
                    'email': ['ajay@gmail.com',[1,2,3,4],'ajay0@gmail.com']
                }
            }
        ],
        'B': [
            {
                'Bob':{
                    'phone': '0987654321',
                    'email': 'bob@gmail.com'
                },
                'Bruce':{
                    'phone': '5555555555',
                    'email': ['bruce@gmail.com','bruce0@gmail.com']
                }
            }
        ],
        'C': [
            {
                'Charlie':{
                    'phone': '4444444444',
                    'email': 'charlie@gmail.com'
                },
                'Chris':{
                    'phone': '6666666666',
                    'email': ['chris@gmail.com','chris0@gmail.com']
                }
            }
        ]
    }
]

print(contacts[0]['A'][0]['Ajay']['email'][1][2])


# print(contacts[0]['A'][0]['Ajay']['email'][1])
# print(contacts[0]['B'])
# print(contacts[0]['C'])

