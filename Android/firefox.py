import time
from playwright.sync_api import sync_playwright

class MobileAutomation:
    def __init__(self):
        self.exceptions = {}

    def mobile_screen_request(self, playwright, device_name, url):
        try:
            # Launch Firefox browser
            browser = playwright.firefox.launch(headless=False)

            user_agent = "Mozilla/5.0 (Linux;Android 9;SM - G950F) Gecko/78.0 Firefox/78.0"
            # Mozilla / 5.0(Linux;Android 9;SM - G950F) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 75.0.3770.101MobileSafari / 537.36
            context = browser.new_context(
                viewport={"width": 360, "height": 640},  # Adjust viewport size as needed
                locale='en-US',
                geolocation={'longitude': 10, 'latitude': 20},
                permissions=['geolocation'],
                user_agent=user_agent
            )

            page = context.new_page()
            page.goto(url)
            time.sleep(5)  # Adjust sleep times as necessary

            # Example interactions with the page
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
            page.click("text=NET30 Payment")

            time.sleep(2)
            page.click("input[name=\"payment[po_number]\"]")

            time.sleep(2)
            page.fill("input[name=\"payment[po_number]\"]", "123456")
            time.sleep(2)
            page.check("text=Purchase Order # (Optional) We accept the Terms and Conditions and we will NOT u >> input[type=\"checkbox\"]")
            page.locator('#net_real').click()
            time.sleep(15)
            print('Performa Invoice Payment!!!')
            context.close()

        except Exception as e:
            print(f"Mobile View request failed for {device_name}:", e)
            self.exceptions[url] = str(e)

def main():
    automation = MobileAutomation()
    url = 'https://www.raptorsupplies.com/pd/morse-drum/86'

    with sync_playwright() as playwright:
        # Iterate over each browser type
        for browser_name in ['firefox']:
            print(f"Running tests on {browser_name}")
            automation.mobile_screen_request(playwright, browser_name, url)

    # Print exceptions, if any
    if automation.exceptions:
        print("\nExceptions:")
        for url, ex in automation.exceptions.items():
            print(f"{url}: {ex}")

if __name__ == "__main__":
    main()
