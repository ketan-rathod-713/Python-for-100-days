import pandas as p

dict = {
    "col1" : [1,2,3,4],
    "col2" : [1,2,3,4]
}

df = p.DataFrame(dict)
df.to_csv("newfile.csv")
file = p.read_csv("newfile.csv")
print(file)