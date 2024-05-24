# https://www.codewars.com/kata/57946a671ace7f940a000031/train/python 
# Thinking & Testing #38: What's the "?"

def test_it(arr):
    colors = set()
    shapes = set()
    for p in arr:
        if p != "?":
            c,s = p.split()
            colors.add(c)
            shapes.add(s)
    
    for c in colors:
        for s in shapes:
            if f"{c} {s}" not in arr:
                return f"{c} {s}"
    
    
"""
sample_test_cases = [
    ('Two color and two shape',
     
     ['Red Square', 'Green Triangle', 'Red Triangle', '?'],
     'Green Square'
    ),

    ('Three color and three shape',
     
     ['Red Square', 'Red Circle', 'Green Triangle', 'Green Circle', 'Blue Circle', '?', 'Blue Triangle', 'Blue Square', 'Green Square'],
     'Red Triangle'
    ),

    ('Two color and three shape',
     
     ['Red Square', 'Red Circle', 'Green Triangle', 'Green Circle', '?', 'Green Square'],
     'Red Triangle'
    ),
]

"""    