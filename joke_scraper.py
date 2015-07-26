import requests, random

from lxml import html

# Create a class that takes the url and strings to find as
# parameters and can create a file containing jokes
class JokeRetriever():

	def __init__(self, url_to_search, search_string):
		self.url_to_search = url_to_search
		self.search_string = search_string
		self.data = self.get_data()

	def get_data(self):
		page_data = requests.get(self.url_to_search)
		return(page_data.text)

	def print_url_file_data(self):
		print(self.data)

	def get_parsed_data(self):
		tree = html.fromstring(self.data)
		return(tree.xpath(self.search_string))

	def set_parsed_data(self, search_string):
		self.search_string = search_string

# URL We Are Scraping
all_jokes_url = "http://safejokes.com/"

# Knowing that there ar 19 pages of jokes, 
# randomly select a number between 1 and 19
# and create the link.
page_num = random.randint(1, 19)
if page_num != 1:
	all_jokes_url = all_jokes_url + 'page/' + str(page_num) + '/'


# Pull the urls of the jokes from the page and store them 
# in a list.
j_url = JokeRetriever(all_jokes_url, '//a[@rel="bookmark"]/@href')
urls = j_url.get_parsed_data()

# Randomly select a url from the page ang pull the
# joke from it
rand_url = random.randint(0, len(urls))
joke_url = urls[rand_url]
j = JokeRetriever(joke_url, '//div[@class="art-postcontent clearfix"]/p/text()')
jokes = j.get_parsed_data()

j.set_parsed_data('//a[@class="url fn n"]/text()')
authors = j.get_parsed_data()

print('Page url:\n     ' + urls[rand_url])
print('\n')
for joke in jokes:
	print(joke + '\n')
print('\nAuthor:\n     ' + authors[0])