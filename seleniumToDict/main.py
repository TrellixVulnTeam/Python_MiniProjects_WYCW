from selenium import webdriver

chrome_driver_path = "/Users/loaialebdi/Dev/Python_MiniProjects/seleniumToDict/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)


# for time in event_times:
#     print(time.text)

# for name in event_names:
#     print(name.text)

driver.close()
