# Insta-download
This little script will let you download Instagram photos.

## Usage
Just enter the link to image as command line argument as below :
```
$ python insta_download.py https://www.instagram.com/p/BJaZ10IDQr6/
```
Downloaded image will be saved in the Download folder of logged user.

### Downloading private photos
If the photo is private and only can be accessed by a follower then you can provide custom header with your cookie.
Pass your header to the **get_link()** function as an optional argument.Example of header is given below :
```python
header={
		'Host':'www.instagram.com',
		'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
		'Accept':'*/*',
		'Accept-Language':'en-US,en;q=0.5',
		'Accept-Encoding':'gzip, deflate, br',
		'X-Requested-With':'XMLHttpRequest',
		'Cookie':'your cookie here',	
		'Connection':'keep-alive'	
	}
```

##Dependency
Please make sure that following libraries are installed before running this script
* beautifulsoup4 (4.4.1)
* requests (2.10.0)

