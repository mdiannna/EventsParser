import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://www.fest.md/')

print(response.text)

# for POST request, form data:
# form_data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://oxylabs.io/', data=form_data)
# print(response.text)


soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)


event_blocks = soup.find_all("div", class_="block-item")
print("event_blocks:")


for evt_block in event_blocks:
	# TODO: get the image here
	figure = evt_block.find("div", class_="figure")

	content = evt_block.find("div", class_="content")
	evt_title = content.find("a", class_="title")
	print("--- Event title:", evt_title.text)

	evt_info = content.find_all("div", class_="oneline")

	for info in evt_info:
		is_date = info.find("span", class_="icon-calendar")!=None
		is_location = info.find("span", class_="icon-pinpoint")!=None
		# print("is_date:", is_date)
		# print("is_location:", is_location)

		if is_date:
			print("Data:", info.text)
		elif is_location:
			print("Locatie:", info.text)
		# else:
			# just ignore
			# print("other:", info.text)
	print("------------------------------------")
	# print("Content:", content)
	# print("evt info:", evt_info)
	# print("evt info:", [info.text for info in evt_info])

	# if "2023" in info.text[0] or ""
# pprint.pprint(event_blocks[0])