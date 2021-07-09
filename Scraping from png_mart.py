import requests
from bs4 import BeautifulSoup
import os 

site_maps = []

main_url = 'https://www.pngmart.com/sitemap.xml/'

response = requests.get(main_url)

xml = response.text

soup = BeautifulSoup(xml,'xml') #Parses text

for loc in soup.find_all('loc'):
    url = loc.text
    if 'post' in url:
       site_maps.append(url)

site_map_1 = site_maps[0]

for site_map in site_maps:
    response = requests.get(site_map)
    soup = BeautifulSoup(response.text,'xml')
    master_list = [loc.text for loc in soup.find_all('loc')]
    
    for n in range(10,20,2):
        png_url = master_list[n+1]
        image_url = master_list[n]

        #print(f"Png_url = {png_url}")
        #print(f"Image_url = {image_url}")

    response = requests.get(image_url)
    soup     = BeautifulSoup(response.text, 'html.parser')
    image    = requests.get(image_url)
    image_title = image_url.split('/')[-1]  + png_url.split('/')[-1]
    print(image_title)
    
    #Creating a directory
    #folder_name = input('\nName your folder')
    #folder = os.path.join('/Users\Emmanuel\Desktop\Code\Web scraping', folder_name)
    #file_name = image_title

    with open(image_title, 'wb') as file:
        file.write(image.content)

    #file = os.path.join(folder, file_name)
    #os.makedirs(folder)



