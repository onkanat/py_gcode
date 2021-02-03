
txt = "G1 X100 Y100 ffff ffff fffff GGGGG F1500 M3"
color = ["G","X","Y","F","M"]

for i in color:
    txt = txt.replace(i,i.lower())
    
    
print(txt)