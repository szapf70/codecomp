# https://www.codewars.com/kata/53988ee02c2414dbad000baa/train/python
# Pretty date

def to_pretty(seconds):
    if not seconds: return "just now"
    ep = [(604800, "a","week"),(86400,"a", "day"),(3600,"an","hour"),(60,"a","minute"),(1,"a", "second")]
    for e in ep:
        if seconds >= e[0]:
            tc = seconds // e[0]
            if tc == 1:
                return f"{e[1]} {e[2]} ago"
            else:
                return f"{tc} {e[2]}{'s'} ago"





print(to_pretty(60), 'just now')

print(to_pretty(1), 'just now')
print(to_pretty(300), '5 minutes ago')
print(to_pretty(3600), 'an hour ago')