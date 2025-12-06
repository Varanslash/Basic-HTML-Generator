# HTML Generator

flag0 = False
flag1 = False
flag2 = False

print("Basic HTML Code Generator")

while flag0 == False:
    java = input("Javascript(y/n)> ")
    if java == "y":
        flag2 = True
        flag0 = True
    elif java == "n":
        flag2 = False
        flag0 = True
        script = "let variablething;"
    else:
        print("Invalid!")

head = input("Heading> ")
while flag1 == False:
    heading = input("Heading Type (h1 - h6)> ")
    if heading in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        headtype = heading
        flag1 = True
    else:
        print("Invalid heading type!")
body = input("Body> ")

while flag2 == True:
    script = input("JS Script> ")
    flag2 = False

finalcode = f"""<!DOCTYPE html>
<html>
<head>
    <{headtype}>{head}</{headtype}>
</head>
<body>
    <p>{body}</p>
</body>
<script>
    {script}
</script>
</html>"""

print(finalcode)