# https://www.codewars.com/kata/537e18b6147aa838f600001b/train/python
# Text align justify

def justify(text, width):
    if text == "": return ""
    words = text.split()
    
    res = []
    buf = []
    
    while words:
        if len(buf) > 0:
            buf.append(" ")
            
    pass # your code here



t = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose injected humour and the like."

print(justify(t))