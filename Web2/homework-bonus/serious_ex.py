from urllib.request import urlopen
import json
import mlab
from questions import Questions

mlab.connect()

url = "https://opentdb.com/api.php?amount=50"
conn = urlopen(url)

### Fetch the content into a string
raw_data = conn.read()
page_content = raw_data.decode("utf8")
# print(type(page_content))

### Convert it into a dict
d1 = json.loads(page_content)
results = d1["results"]
for result in results:
    for i in range (len(results)):       
        result = Questions(category = results[i]["category"], types = results[i]["type"], 
        difficulty = results[i]["difficulty"], question = results[i]["question"], correct_answer = results[i]["correct_answer"], 
        incorrect_answers = results[i]["incorrect_answers"])
        result.save()



