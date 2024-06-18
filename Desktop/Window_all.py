import time
from playwright.sync_api import sync_playwright

class DesktopAutomation:
    def __init__(self):
        self.exceptions = {}

    def run_test(self, playwright, browser_name, url):
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

            page = browser.new_page()
            page.goto(url)
            time.sleep(1)
            page.wait_for_selector('#eve_38').click()
            time.sleep(2)
            element = page.wait_for_selector("//*[@id='eve_294']/a", state='visible')
            element.click()
            time.sleep(12)
            # page.frame(name="webWidget").click("[aria-label=\"Minimize widget\"]")
            page.fill("#customer-email", "shubham@raptorsupplies.co.uk")
            firstname_input = page.wait_for_selector('input[name="firstname"]')
            firstname_input.fill('Shubham')
            page.fill('input[name="lastname"]', 'Singh')
            page.fill('input[name="company"]', 'Raptor ')
            page.fill('input[name="street[0]"]', 'Mohan Estate')
            page.fill('input[name="city"]', 'Delhi')
            time.sleep(2)
            page.select_option("select[name=\"country_id\"]", "IN")
            page.select_option("select[name=\"region_id\"]", "542")  # delhi
            page.fill("[name='postcode']", "110021")
            page.fill("[name='telephone']", "123456789")
            page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
            page.wait_for_selector('#eve_200').click()
            page.wait_for_selector("//*[@class='edit_shipping_info']").click()
            page.select_option("select[name=\"region_id\"]", "543")  # goa
            page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
            page.wait_for_selector('#eve_200').click()
            page.click("text=$29.99 Flat Rate Shipping (5 - 7 days)")

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
            time.sleep(50)
            print('Performa Invoice Payment!!!')
            browser.close()
        except Exception as e:
            print(f"An error occurred on {browser_name}: {e}")
            self.exceptions[browser_name] = str(e)

def main():
    with sync_playwright() as playwright:
        automation = DesktopAutomation()
        url = "https://www.raptorsupplies.com/pd/keysco-tools/77525"
        for browser_type in ['chromium']:
            print(f"Running tests on {browser_type}")
            automation.run_test(playwright, browser_type, url)

if __name__ == "__main__":
    main()
