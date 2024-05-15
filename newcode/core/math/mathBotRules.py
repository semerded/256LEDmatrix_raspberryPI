rules = [
    [  # 1ste
        {  # makkelijk
            "operand": [
                "+"
            ],
            "maxSolution": 10,
            "maxNumber": 9
        },
        {  # gemiddeld
            "operand": [
                "+", "+", "-"
            ],
            "maxSolution": 15,
            "maxNumber": 9
        },
        {  # moeilijk
            "operand": [
                "+", "-"
            ],
            "maxSolution": 20,
            "maxNumber": 19
        }
    ],
    [  # 2de
        {
            "operand": [
                "+", "-"
            ],
            "maxSolution": 100,
            "maxNumber": 50
        },
        {
            "operand": [
                "+", "+", "-", "-", "maaltafel"
            ],
            "maxSolution": 100,
            "maxNumber": 50
        },
        {
            "operand": [
                "+", "-", "maaltafel"
            ],
            "maxSolution": 100,
            "maxNumber": 99
        }
    ],
    [ # 3de
        {
            "operand": [
                "+", "-", "maaltafel"
            ],
            "maxSolution": 500,
            "maxNumber": 400
        },
        {
            "operand": [
                "+", "-", "maaltafel"
            ],
            "maxSolution": 1000,
            "maxNumber": 600
        },
        {
            "operand": [
                "+", "-", "maaltafel", "maaltafel"
            ],
            "maxSolution": 1000,
            "maxNumber": 999
        }
    ],
    [ # 4de
        {
            "operand": [
                "+", "+", "-", "-", "*", "/"
            ],
            "maxSolution": 10000,
            "maxNumber": 5000
        },
        {
            "operand": [
                "+", "+", "-", "-", "*", "/"
            ],
            "maxSolution": 50000,
            "maxNumber": 30000
        },
        {
            "operand": [
                "+", "-", "*", "/"
            ],
            "maxSolution": 100000,
            "maxNumber": 99999
        }
    ],
    [ # 5de 
        {
            "operand": [
                "+", "-", "*", "/"
            ],
            "maxSolution": 100000,
            "maxNumber": 99999
        },
        {
            "operand": [
                "+", "+", "-", "-", "*", "*", "/", "/", "%" 
            ],
            "maxSolution": 1000000,

            "maxNumber": 500000
        },
        {
            "operand": [
                "+", "-", "*", "/", "%"
            ],
            "maxSolution": 1000000,

            "maxNumber": 999999
        }
    ],
    [ # 6de 
        {
            "operand": [
                "+", "+", "-", "-", "*", "*", "/", "/", "%" 
            ],
            "maxSolution": 1000000,
            "maxNumber": 500000
        },
        {
            "operand": [
                "+", "-", "*", "/", "%"
            ],
            "maxSolution": 10000000,

            "maxNumber": 5000000
        },
        {
            "operand": [
                "+", "-", "*", "/", "%"
            ],
            "maxSolution": 10000000,

            "maxNumber": 9999999
        }
    ]

]
