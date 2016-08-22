#---------------------------------------------------------------------
#Name      : Insta Download
#Purpose   : Download Instagram photos
#Author    : Atul Kumar
#Created   : 20/08/2016
#License   : GPL V3
#Copyright : (c) 2016 Atul Kumar (www.facebook.com/atul.kr.007)

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Contact Author at atulkumar0417@gmail.com
#-----------------------------------------------------------------------

import requests,time,os,sys
from bs4 import BeautifulSoup

def get_link(pic_link,header=None):
	try:
		if(header == None):
			req1 = requests.get(pic_link)
		else:
			req1 = requests.get(pic_link,headers=header)

		req1.raise_for_status()
		soup = BeautifulSoup(req1.text,'html.parser')
		pic_downoad_link = soup.find_all('meta',property='og:image')[0].get('content').split('?')[0]
		return pic_downoad_link

	except Exception as e:
		print(str(e))
		sys.exit()

def download(download_link):
	try:
		req2 = requests.get(download_link)
		req2.raise_for_status()
		filename = 'insta_image_'+str(int(time.time()))+".jpg"
		with open(get_home_dir()+'/Downloads/'+filename,'wb') as image:
			for chunk in req2.iter_content(chunk_size=100000):
				if chunk:
					image.write(chunk)
	except Exception as e:
		print(str(e))
		sys.exit()

def get_home_dir():
	return os.path.expanduser("~")


def main():
	if len(sys.argv)<2:
		pic_link = input("Enter the image link: ")
	else:
		pic_link = sys.argv[1]

	if not os.path.exists(get_home_dir()+'/Downloads/'):
		os.makedirs(get_home_dir()+'/Downloads/')

	# Custom header to download private images of user,whom user have followed.(optional)
	# Please pass your header, mine is shown below as example!
	# Pass header to the "download_link" function as second argument. 

	# header={
	# 	'Host':'www.instagram.com',
	# 	'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
	# 	'Accept':'*/*',
	# 	'Accept-Language':'en-US,en;q=0.5',
	# 	'Accept-Encoding':'gzip, deflate, br',
	# 	'X-Requested-With':'XMLHttpRequest',
	#	'Cookie':'your cookie here',	
	# 	'Connection':'keep-alive'	
	# }
	
	download_link = get_link(pic_link)
	download(download_link)
	print("Image downloaded successfully at '"+get_home_dir()+"/Downloads/'")


if __name__ =='__main__':
	main()
