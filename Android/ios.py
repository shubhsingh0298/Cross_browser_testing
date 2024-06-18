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

            # Create a new context for the browser
            context = browser.new_context(
                viewport={"width": 1366, "height": 768},  # Adjust viewport size as needed
                locale='en-US',
                geolocation=None,  # Remove geolocation for desktop
                permissions=None,  # Remove permissions for desktop
                user_agent=None  # Use default user agent for desktop
            )

            page = context.new_page()
            page.goto(url)
            time.sleep(12)
            page.click('#eve_38')
            time.sleep(2)
            page.click("//*[@id='eve_294']/a")
            time.sleep(5)
            page.fill("#customer-email", "shubham@raptorsupplies.co.uk")
            page.fill("[name='firstname']", "Shubham")
            page.fill("[name='lastname']", "Singh")
            page.fill("[name='company']", "Raptor")
            page.fill("[name='street[0]']", "Mohan Estate")
            page.fill("[name='city']", "Delhi")
            page.select_option("[name='country_id']", "IN")
            page.select_option("[name='region_id']", "Delhi")
            page.fill("[name='postcode']", "110021")
            page.fill("[name='telephone']", "1234567890")
            page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
            page.wait_for_selector('#eve_200').click()
            page.wait_for_selector("//*[@class='edit_shipping_info']").click()
            time.sleep(8)
            page.select_option('select[name="region_id"]', 'Goa')
            page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
            page.wait_for_selector('#eve_200').click()
            page.get_by_label("Economy (6 - 10 days)").check()
            page.get_by_role("button", name="Proceed to Payment").click()
            time.sleep(5)
            page.get_by_text("Proforma Invoice").click()
            time.sleep(2)
            page.get_by_role("textbox", name="Purchase Order # (Optional)").click()
            time.sleep(2)
            page.get_by_role("textbox", name="Purchase Order # (Optional)").fill("123456")
            time.sleep(2)
            page.locator("#performa_check").check()
            page.locator('#performa_real').click()
            print('Performa Invoice Payment!!!')
            time.sleep(15)
            context.close()

        except Exception as ex:
            print(f"Desktop View request failed for {browser_name}:", ex)
            self.exceptions[url] = ex

def main():
    automation = MobileAutomation()
    url = 'https://www.raptorsupplies.com/pd/morse-drum/86'

    with sync_playwright() as playwright:
        # Iterate over each browser type
        for browser_name in ['chromium', 'webkit', 'firefox', 'bing', 'yahoo']:
            print(f"Running tests on {browser_name}")
            automation.mobile_screen_request(playwright, browser_name, url)

    # Print exceptions, if any
    if automation.exceptions:
        print("\nExceptions:")
        for url, ex in automation.exceptions.items():
            print(f"{url}: {ex}")

if __name__ == "__main__":
    main()
