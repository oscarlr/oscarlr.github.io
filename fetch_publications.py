import json
from scholarly import scholarly

def fetch_publications():
    # Replace 'Your Name' with your name or Google Scholar ID
    search_query = scholarly.search_author('AVzJo1MAAAAJ')
    author = next(search_query)
    scholarly.fill(author)

    publications = []
    for pub in author['publications']:
        # Extract relevant publication details, like title and publication year
        publications.append({
            'title': pub['bib']['title'],
            'year': pub['bib'].get('pub_year', 'Unknown'),
            'journal': pub['bib'].get('venue', 'Unknown'),
            'authors': pub['bib'].get('author', 'Unknown'),
            'url': pub.get('pub_url', '')
        })

    # Write the publications data to a JSON file
    with open('publications.json', 'w') as f:
        json.dump(publications, f, indent=4)

    print("Publications fetched and saved to publications.json")

if __name__ == '__main__':
    fetch_publications()
