from selenium import webdriver
PROXY = "proxy:5566"

def show_pack_title():
	url = "https://www.packtpub.com/packt/offers/free-learning"
	driver.get(url)
	title = driver.find_element_by_css_selector("div.dotd-title>h2").text
	print(title)

def hard_quit(funct):
	def wrapper():
		try:
			funct()
		except Exception as e:
			print(e)
			driver.quit()
	return wrapper

def show_ip():
	url = "https://api.ipify.org"
	driver.get(url)
	print(driver.find_element_by_css_selector("body").text)
	# ip_el = driver.find_element_by_css_selector("div#json").text
	# print(ip_el)

capabilities = webdriver.DesiredCapabilities.CHROME
proxy_caps = {
	"httpProxy":PROXY,
	"ftpProxy":PROXY,
	"sslProxy":PROXY,
	"proxyType": "manual",
	"noProxy":None,
	"class":"org.openqa.selenium.Proxy",
	"autodetect":False

}
capabilities["proxy"] = proxy_caps
driver = webdriver.Remote(
	command_executor="http://127.0.0.1:4444/wd/hub", 
	desired_capabilities=capabilities
	)
show_ip()

driver.quit()
