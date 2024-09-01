QR_EQUIVALENT = {
    "S2":"Q7",
    "S1":"Q22",
    "A":"Q50",
    "B":"Q45",
    "C":"Q38",
    "D":"Q33"
}

pins_data = {
    # STOP
    0:[
        {"PIN":"NW_FW", "STATE":0},
        {"PIN":"NW_BW", "STATE":0},

        {"PIN":"NE_FW", "STATE":0},
        {"PIN":"NE_BW", "STATE":0},

        {"PIN":"SW_FW", "STATE":0},
        {"PIN":"SW_BW", "STATE":0},

        {"PIN":"SE_FW", "STATE":0},
        {"PIN":"SE_BW", "STATE":0},
    ],
    # FORWARD
    1:[
        {"PIN":"NW_FW", "STATE":1},
        {"PIN":"NW_BW", "STATE":0},

        {"PIN":"NE_FW", "STATE":1},
        {"PIN":"NE_BW", "STATE":0},

        {"PIN":"SW_FW", "STATE":1},
        {"PIN":"SW_BW", "STATE":0},

        {"PIN":"SE_FW", "STATE":1},
        {"PIN":"SE_BW", "STATE":0},
    ],
    # BACKWARD
    2:[
        {"PIN":"NW_FW", "STATE":0},
        {"PIN":"NW_BW", "STATE":1},

        {"PIN":"NE_FW", "STATE":0},
        {"PIN":"NE_BW", "STATE":1},

        {"PIN":"SW_FW", "STATE":0},
        {"PIN":"SW_BW", "STATE":1},

        {"PIN":"SE_FW", "STATE":0},
        {"PIN":"SE_BW", "STATE":1},
    ],
    # LEFT
    3:[
        {"PIN":"NW_FW", "STATE":0},
        {"PIN":"NW_BW", "STATE":1},

        {"PIN":"NE_FW", "STATE":1},
        {"PIN":"NE_BW", "STATE":0},

        {"PIN":"SW_FW", "STATE":1},
        {"PIN":"SW_BW", "STATE":0},

        {"PIN":"SE_FW", "STATE":0},
        {"PIN":"SE_BW", "STATE":1},
    ],
    # RIGHT
    4:[
        {"PIN":"NW_FW", "STATE":1},
        {"PIN":"NW_BW", "STATE":0},

        {"PIN":"NE_FW", "STATE":0},
        {"PIN":"NE_BW", "STATE":1},

        {"PIN":"SW_FW", "STATE":0},
        {"PIN":"SW_BW", "STATE":1},

        {"PIN":"SE_FW", "STATE":1},
        {"PIN":"SE_BW", "STATE":0},
    ],
    # TURNING LEFT
    5:[
        {"PIN":"NW_FW", "STATE":0},
        {"PIN":"NW_BW", "STATE":1},

        {"PIN":"NE_FW", "STATE":1},
        {"PIN":"NE_BW", "STATE":0},

        {"PIN":"SW_FW", "STATE":0},
        {"PIN":"SW_BW", "STATE":1},

        {"PIN":"SE_FW", "STATE":1},
        {"PIN":"SE_BW", "STATE":0},
    ],
    # TURNING RIGHT
    6:[
        {"PIN":"NW_FW", "STATE":1},
        {"PIN":"NW_BW", "STATE":0},

        {"PIN":"NE_FW", "STATE":0},
        {"PIN":"NE_BW", "STATE":1},

        {"PIN":"SW_FW", "STATE":1},
        {"PIN":"SW_BW", "STATE":0},

        {"PIN":"SE_FW", "STATE":0},
        {"PIN":"SE_BW", "STATE":1},
    ]
}

pwms_data= {
    0: [
        {"PIN":"NW_PWM","PWM":0},
        {"PIN":"NE_PWM","PWM":0},
        {"PIN":"SW_PWM","PWM":0},
        {"PIN":"SE_PWM","PWM":0}
    ],
    1: [
        {"PIN":"NW_PWM","PWM":225},
        {"PIN":"NE_PWM","PWM":225},
        {"PIN":"SW_PWM","PWM":225},
        {"PIN":"SE_PWM","PWM":225}
    ]
} 

destination_data = [
        {
            "area_name":"S2",
            "horizontal_coordinate":2250.0,
            "vertical_coordinate":0
        },
        {
            "area_name":"S1",
            "horizontal_coordinate":2250,
            "vertical_coordinate":3000
        },
        {
            "area_name":"A",
            "horizontal_coordinate":3726.0,
            "vertical_coordinate":1500.0
        },
        {
            "area_name":"B",
            "horizontal_coordinate":2988.0,
            "vertical_coordinate":1500.0,
        },
        {
            "area_name":"C",
            "horizontal_coordinate":1511.0,
            "vertical_coordinate":1500.0
        },
        {
            "area_name":"D",
            "horizontal_coordinate":733.0,
            "vertical_coordinate":1500.0
        },
        {
            "area_name":"1",
            "horizontal_coordinate":0,
            "vertical_coordinate":0
        },
        {
            "area_name":"2",
            "horizontal_coordinate":0,
            "vertical_coordinate":3000.0
        },
        {
            "area_name":"3",
            "horizontal_coordinate":4500.0,
            "vertical_coordinate":3000.0
        },
        {
            "area_name":"4",
            "horizontal_coordinate":4500.0,
            "vertical_coordinate":0
        }
]

default_protocol = { 
    "stop": [
        {
            "move": 0,
            "pwms": [
                {"PIN":"NW_PWM","PWM":0},
                {"PIN":"NE_PWM","PWM":0},
                {"PIN":"SW_PWM","PWM":0},
                {"PIN":"SE_PWM","PWM":0}
            ],
            "tip": "pass:default",
            "condition": True,
            "completed": False,
            "process": False
        }
    ],
    "forward": [
        {
            "move": 1,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip": "pass:default",
            "condition": True,
            "completed": False,
            "process": False
        }
    ],
    "obstacle_pass": [
        {
            "move": 4,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip":"distance:default",
            "condition":{
                "pin":"d14",
                "state":1
            },
            "completed": False,
            "process": False
        },
        {
            "move": 4,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip":"sleep:default",
            "condition":3.5,
            "completed": False,
            "process": False
        },
        {
            "move": 1,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip":"distance:default",
            "condition":{
                "pin":"d13",
                "state":0
            },
            "completed": False,
            "process": False
        },
        {
            "move": 1,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip":"distance:default",
            "condition":{
                "pin":"d13",
                "state":1
            },
            "completed": False,
            "process": False
        },
        {
            "move": 1,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip":"sleep:default",
            "condition":1.5,
            "completed": False,
            "process": False
        },
        {
            "move": 3,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip":"distance:default",
            "condition":{
                "pin":"d15",
                "state":0
            },
            "completed": False,
            "process": False
        },
        {
            "move": 3,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip": "line_status:or",
            "condition":{
                "index":[3,4,5],
                "bp":50
            },
            "completed": False,
            "process": False
        },
        {
            "move": 1,
            "pwms": [
                {"PIN":"NW_PWM","PWM":225},
                {"PIN":"NE_PWM","PWM":225},
                {"PIN":"SW_PWM","PWM":225},
                {"PIN":"SE_PWM","PWM":225}
            ],
            "tip":"pass:default",
            "condition":True,
            "completed": False,
            "process": False
        }
    ] 
}
