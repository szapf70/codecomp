# https://www.codewars.com/kata/537e18b6147aa838f600001b/train/python
# Text align justify

class aline():
    def __init__(self,max_len):
        self.words = []
        self.acc_words_len = 0
        self.max_len = max_len

    def can_recieve(self, word):
        return (self.acc_words_len + len(self.words) + len(word)) <= self.max_len
    
    def recieve(self,word):
        self.words.append(word)
        self.acc_words_len += len(word)
        return
    
    def publish(self):
        if len(self.words) == 1:
            return self.words[0]
        
        spaces = self.max_len - self.acc_words_len
        bspace = spaces//(len(self.words)-1)
        rest = spaces%(len(self.words)-1)
        p_str = ""
        for w in self.words[:-1]:
            p_str += w
            p_str += (" " * bspace)
            if rest:
                p_str += " "
                rest -= 1
        p_str += self.words[-1]
        return p_str

    def publish_last(self):
        return " ".join(self.words)



def justify(text, width):
    if text == "": return ""
    words = text.split()
    lines = []

    while words:
        act_line = aline(width)
        while words and act_line.can_recieve(words[0]):
            act_line.recieve(words.pop(0))
        lines.append(act_line)    

    res = []

    for l in lines[:-1]:
        res.append(l.publish())
    res.append(lines[-1].publish_last())
    return "\n".join(res)

text = """\
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor."""

print(justify(text,13))