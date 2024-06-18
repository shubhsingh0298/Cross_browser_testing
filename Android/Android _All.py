import time
from playwright.sync_api import sync_playwright

class MobileAutomation:
    def __init__(self):
        self.exceptions = {}

    def mobile_screen_request(self, playwright, browser_name, url):
        try:
            # Initialize the browser based on the browser_name
            if browser_name == 'chromium':
                browser = playwright.chromium.launch(headless=False)
            elif browser_name == 'webkit':
                browser = playwright.webkit.launch(headless=False)
            elif browser_name == 'firefox':
                browser = playwright.firefox.launch(headless=False)
            else:
                raise ValueError(f"Unsupported browser: {browser_name}")

            # Set up device and context based on browser_name
            if browser_name in ['webkit', 'chromium']:
                device_name = 'iPhone 11 Pro'
                device = playwright.devices[device_name]
                context = browser.new_context(
                    **device,
                    locale='en-US',
                    geolocation={'longitude': 10, 'latitude': 20},
                    permissions=['geolocation']
                )
            elif browser_name == 'firefox':
                # Since playwright.devices does not have 'oneplus nord ce', using 'Pixel 4'
                device_name = 'Pixel 4'
                device = playwright.devices[device_name]
                context = browser.new_context(
                    **device,
                    locale='en-US',
                    geolocation={'longitude': 10, 'latitude': 20},
                    permissions=['geolocation']
                )

            page = context.new_page()
            page.goto(url)
            time.sleep(2)
            page.click('#eve_38')
            page.click("//*[@id='eve_294']/a")
            time.sleep(12)

            page.fill("#customer-email", "shubham@raptorsupplies.co.uk")
            time.sleep(2)
            page.fill("[name='firstname']", "Shubham")
            # time.sleep(2)
            page.fill("[name='lastname']", "Singh")
            # time.sleep(2)
            page.fill("[name='company']", "Raptor")
            page.fill("[name='street[0]']", "Mohan Estate")
            page.fill("[name='city']", "Delhi")
            page.select_option("select[name=\"country_id\"]", "IN")
            page.select_option("select[name=\"region_id\"]", "543")  # goa
            page.fill("[name='postcode']", "110021")
            page.fill("[name='telephone']", "123456789")
            page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
            page.wait_for_selector('#eve_200').click()
            page.wait_for_selector("//*[@class='edit_shipping_info']").click()
            page.select_option("select[name=\"region_id\"]", "542")  # delhi
            page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
            page.wait_for_selector('#eve_200').click()
            page.click("text=Economy (6 - 10 days)")

            page.click("button:has-text(\"Proceed to Payment\")")
            time.sleep(5)
            page.click("text=Proforma Invoice")
            page.click("#eve_210")
            page.fill("#eve_210", "098765")
            page.check("#performa_check")
            page.locator('#performa_real').click()
            time.sleep(50)
            print('Proforma Invoice Payment!!!')

            context.close()

        except Exception as ex:
            print(f"Mobile View request failed for {browser_name}:", ex)
            self.exceptions[browser_name] = ex

def main():
    automation = MobileAutomation()
    url = 'https://www.raptorsupplies.com/pd/morse-drum/86'

    with sync_playwright() as playwright:
        # Iterate over each browser type
        for browser_name in ['chromium']:
            print(f"Running tests on {browser_name}")
            automation.mobile_screen_request(playwright, browser_name, url)

    # Print exceptions, if any
    if automation.exceptions:
        print("\nExceptions:")
        for browser_name, ex in automation.exceptions.items():
            print(f"{browser_name}: {ex}")

if __name__ == "__main__":
    main()
