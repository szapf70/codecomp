# https://www.codewars.com/kata/60245d013b9cda0008f4da8e/train/python
# US Postal Codes

codes = ["Alabama, AL",
"Alaska, AK",
"Arizona, AZ",
"Arkansas, AR",
"California, CA",
"Colorado, CO",
"Connecticut, CT",
"Delaware, DE",
"Florida, FL",
"Georgia, GA",
"Hawaii, HI",
"Idaho, ID",
"Illinois, IL",
"Indiana, IN",
"Iowa, IA",
"Kansas, KS",
"Kentucky, KY",
"Louisiana, LA",
"Maine, ME",
"Maryland, MD",
"Massachusetts, MA",
"Michigan, MI",
"Minnesota, MN",
"Mississippi, MS",
"Missouri, MO",
"Montana, MT",
"Nebraska, NE",
"Nevada, NV",
"New Hampshire, NH",
"New Jersey, NJ",
"New Mexico, NM",
"New York, NY",
"North Carolina, NC",
"North Dakota, ND",
"Ohio, OH",
"Oklahoma, OK",
"Oregon, OR",
"Pennsylvania, PA",
"Rhode Island, RI",
"South Carolina, SC",
"South Dakota, SD",
"Tennessee, TN",
"Texas, TX",
"Utah, UT",
"Vermont, VT",
"Virginia, VA",
"Washington, WA",
"West Virginia, WV",
"Wisconsin, WI",
"Wyoming, WY",
"District of Columbia, DC",
"American Samoa, AS",
"Guam, GU",
"Northern Mariana Islands, MP",
"Puerto Rico, PR",
"U.S. Virgin Islands, VI"]

def abbr(s):
    c="62dAL559AK662AZ744AR934CA763COa41CT765DE695FL6a0GA5b3HI4bfID7d3IL6b2IN3d8IA5e5KS7feKY8fdLA4ecME808MDd3aMA7f0MI918MNb3bMS82bMO704MT807NE5f7NVcd7NH9d4NJ9c7NM7cfNYddcNCbcfND407OH81cOK61eORc78PAc1dRIe70SCc4fSD992TN54dTX43aUT79fVT899VAaeeWAdd2WV9dbWI7acWY122DCc4dAS3c2GU17bMPb0cPR131VI"    
    for i in range(0,len(c),5):
        if c[i:i+3]==hex(sum([ord(l)+ord(s[0])*2 for l in s]))[2:5]:return c[i+3:i+5]


print(abbr("Alaska"))