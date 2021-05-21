import os


os.makedirs("output", exist_ok=True)

with open("./output/index.html", mode="w") as f:
    f.write("<html><body>yo</body></html>")
