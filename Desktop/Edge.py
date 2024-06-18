import time
from playwright.sync_api import sync_playwright

class EdgeAutomation:
    def __init__(self):
        self.exceptions = {}

    def edge_test(self, playwright, url):
        try:
            # edge_executable_path = "C:\\Users\\dell\\Downloads\\msedge.exe"

            browser = playwright.chromium.launch(headless=False, channel='msedge')
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            time.sleep(2)
            page.click('#eve_38')
            time.sleep(2)
            page.click("//*[@id='eve_294']/a")
            time.sleep(12)
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
            page.click("text=Economy (6 - 10 days)")

            page.click("button:has-text(\"Proceed to Payment\")")
            time.sleep(5)
            page.click("text=NET30 Payment")

            time.sleep(2)
            page.click("input[name=\"payment[po_number]\"]")

            time.sleep(2)
            page.fill("input[name=\"payment[po_number]\"]", "123456")
            time.sleep(2)
            page.check(
                "text=Purchase Order # (Optional) We accept the Terms and Conditions and we will NOT u >> input[type=\"checkbox\"]")
            # page.locator('#net_real').click()
            # time.sleep(50)
            print('Performa Invoice Payment!!!')
            context.close()

        except Exception as ex:
            print(f"Edge test failed:", ex)
            self.exceptions[url] = ex

def main():
    automation = EdgeAutomation()
    url = 'https://www.raptorsupplies.com/pd/morse-drum/86'

    with sync_playwright() as playwright:
        print("Running tests on Edge")
        automation.edge_test(playwright, url)

    # Print exceptions, if any
    if automation.exceptions:
        print("\nExceptions:")
        for url, ex in automation.exceptions.items():
            print(f"{url}: {ex}")

if __name__ == "__main__":
    main()
