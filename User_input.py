city_code = input(str('Please enter city code made of 4 digits'))
pages_to_scan = input('Please enter the number of pages needed')
first_page_url = 'https://www.yad2.co.il/realestate/forsale?city=' + city_code
count = 0
additional_pages = []
while count < int(pages_to_scan):
    place = str(count + 2)
    temp = (first_page_url + '&page=' + place)
    additional_pages.append(temp)
    count += 1
    print(count)

print(count)
for item in additional_pages:
    print(item)
