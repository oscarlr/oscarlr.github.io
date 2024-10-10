import json
from scholarly import scholarly

def fetch_publications():
    # Replace 'AVzJo1MAAAAJ' with your Google Scholar ID or use a search term
    search_query = scholarly.search_author('Oscar L Rodriguez')

    try:
        author = next(search_query)
        scholarly.fill(author)

        publications = []
        for pub in author['publications']:
            # Fill each publication to get full details, including authors
            scholarly.fill(pub)

            print(pub)

            # Extract relevant publication details, like title, publication year, and authors
            publications.append({
                'title': pub['bib']['title'],
                'year': pub['bib'].get('pub_year', 'Unknown'),
                'journal': pub['bib'].get('journal', 'Unknown'),
                'authors': pub['bib'].get('author', 'Unknown').replace(" and",","),
                'url': pub.get('pub_url', '')
            })

        # Write the publications data to a JSON file
        with open('publications.json', 'w') as f:
            json.dump(publications, f, indent=4)

        print("Publications fetched and saved to publications.json")
    except StopIteration:
        print("No author found for the given Google Scholar ID.")

if __name__ == '__main__':
    fetch_publications()
