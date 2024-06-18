import time
from playwright.sync_api import sync_playwright

def run(playwright, browser_name, device_name):

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "playwright-webkit":
        browser = playwright.webkit.launch(headless=False)
    # elif browser_name == "playwright-firefox":
    #     browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError("Unsupported browser: " + browser_name)

    device = playwright.devices[device_name]
    context = browser.new_context(
        **device,
        locale='en-US',
        geolocation={'longitude': 10, 'latitude': 20},
        permissions=['geolocation']
    )

    page = context.new_page()

    page.goto('https://www.raptorsupplies.com/pd/morse-drum/86')

    page.click('#eve_38')

    page.click("//*[@id='eve_294']/a")
    time.sleep(12)
    page.fill("#customer-email", "shubham@raptorsupplies.co.uk")
    page.fill("[name='firstname']", "Shubham")
    page.fill("[name='lastname']", "Singh")
    page.fill("[name='company']", "Raptor")
    page.fill("[name='street[0]']", "Mohan Estate")
    page.fill("[name='city']", "Delhi")
    time.sleep(2)
    page.select_option('select[name="country_id"]', 'India')
    page.select_option('select[name="region_id"]', 'Delhi')
    page.fill("[name='postcode']", "110021")
    page.fill("[name='telephone']", "1234567890")
    page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
    page.wait_for_selector('#eve_200').click()
    page.click("//*[@class='edit_shipping_info']")

    page.select_option("[name='region_id']", "Goa")
    page.click("//button[@id='eve_200']")
    page.get_by_label("Economy (6 - 10 days)").check()
    page.get_by_role("button", name="Proceed to Payment").click()
    page.fill('//*[@id="eve_209"]', '6547685')
    page.click('#net_check')
    page.click('//*[@id="performa_real"]')
    time.sleep(15)
    print('Performa Invoice Payment!!!')

    browser.close()

# Define the platforms and browsers
platforms = [
    {'os': 'Windows', 'osVersion': '11', 'browserName': 'chrome', 'browserVersion': 'latest', 'deviceName': 'iPhone 11 Pro'},
    {'os': 'OS X', 'osVersion': 'Ventura', 'browserName': 'playwright-webkit', 'browserVersion': 'latest', 'deviceName': 'iPhone 11 Pro'},
    {'os': 'Windows', 'osVersion': '11', 'browserName': 'playwright-firefox', 'browserVersion': 'latest', 'deviceName': 'iPhone 11 Pro'}
]

with sync_playwright() as playwright:
    for platform in platforms:
        print(f"Running tests on {platform['os']} {platform['osVersion']} with {platform['browserName']}")
        run(playwright, platform['browserName'], platform['deviceName'])
