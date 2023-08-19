header = input("Type header : ")
par = input("Type paragraph : ")

html = f"""
<h1>{header}</h1>
<p>{par}</p>
"""

open("Index.html", "w").write(html)
print('Index.html created')
