# instascrape.py
## Usage
Either pipe in the contents of a text file, or run instascrape `file`.

`cat dog_links.txt | instascrape.py`
`instascrape.py dog_links.txt`

If no file is given, instascrape will assume you want the first file it can find that ends in "links.txt".

## Options
By default, the pictures will be saved to a folder called `scraped\_pictures`. This can be changed using the -f argument:
`instascrape.py dog_links.txt -f dog_pics`

If your text file ends in "links.txt" or "\_links.txt", it will use the preceeding part of the filename to name the folder.
`instascrape.py dog_links.txt` saves to "./dog\_pictures".

## Caveats
If a page has multiple images, will only grab the first one. Sorry, it's a lot harder to get all of them and I haven't figured that part out just yet.
