x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
w = abs(x2 - x1) # width
h = abs(y2 - y1) # height
s = w * h # area
p = 2 * (w + h) # perimeter
print(w, h, s, p)