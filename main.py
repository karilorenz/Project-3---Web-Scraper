from bs4 import BeautifulSoup
import requests

# Enter search term, send as q get variable in parameters to url ( https://www.bing.com/search?q= )
search = input("Enter search term:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

# Build soup so can parse content, get text pass to html.parser (parser want to use)
soup = BeautifulSoup(r.text, "html.parser")

# Get List of results, pass element looking for and dict-obj of attributes looking for -> put into variable
results = soup.find("ol", {"id": "b_results"})
# Only want specific info from result (omitting ads and sidebar), pass elements - list items, attribute - class
# Finds and stores in list called links
links = results.findAll("li", {"class": "b_algo"})

# Get text for element and a for href property, get list of attributes
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    # Make sure both exist
    if item_text and item_href:
        print(item_text)
        print(item_href)
        # Find parent element
        print("Parent", item.find("a").parent)
        # Find child element, go back another parent, find p element, get text
        print("Summary", item.find("a").parent.parent.find("p").text)

        # Compile list of all children elements of item list
        children = item.children
        for child in children:
            print("Child", child)

        # Next sibling, can also find previous
        children = item.find("h2")
        print("Next sibling of the h2", children.next_sibling)




