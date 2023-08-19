students = [
    {"name": "f madani", "job": "backend developer", "code": 1051},
    {"name": "n madani", "job": "backend developer", "code": 1052},
    {"name": "b fazeli", "job": "full stack developer", "code": 1053},
    {"name": "a soleimani", "job": "db admin", "code": 1054},
    {"name": "r parhizkar", "job": "frontend developer", "code": 1055},
    {"name": "m ghaznavi", "job": "ui / ux", "code": 1056},
    {"name": "k ghorbani", "job": "project manager", "code": 1057},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Calibri, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: red;
  color: white;
}
</style>
</head>
<body>

<h1>Class D Students</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Job</th>
    <th>Code</th>
  </tr>
  
"""

for i in students:
    html += f"""
  <tr>
    <td>{i['name']}</td>
    <td>{i['job']}</td>
    <td>{i['code']}</td>
  </tr>
    """

html += """
</table>
</body>
</html>
"""

open("Table.html", "w").write(html)
print("Done")
