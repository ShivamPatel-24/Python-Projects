from selenium import webdriver

chrome_driver_path = "/Users/shivampatel/Developer/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/Tommy-Hilfiger-Redder-Slide-Sandal/dp/B07Y5TPHFP/ref=sr_1_1?pd_rd_r=61ccfde5-0631-4027-9479-5a2ea7613a67&pd_rd_w=yOMzc&pd_rd_wg=xwkCf&pf_rd_p=b3e1d634-a17d-4d08-8031-67d51f48516e&pf_rd_r=5X1ZFBE4XC321MP2QJAK&qid=1657821066&s=apparel&sr=1-1")

complete = driver.find_elements_by_class_name("a-offscreen")
print(complete.text)

driver.quit()