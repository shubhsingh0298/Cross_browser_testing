import time
from playwright.sync_api import sync_playwright

def run_test(browser_type):
    with sync_playwright() as p:
        if browser_type == 'chromium':
            browser = p.chromium.launch(headless=False)
        elif browser_type == 'firefox':
            browser = p.firefox.launch(headless=False)
        elif browser_type == 'webkit':
            browser = p.webkit.launch(headless=False)
        elif browser_type == 'safari':
            browser = p.webkit.launch(headless=False)  # Safari is supported via WebKit
        elif browser_type == 'edge':
            browser = p.chromium.launch(headless=False, executable_path='/path/to/msedge')  # Replace with actual path to Edge executable
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

        page = browser.new_page()
        page.goto("https://www.raptorsupplies.com/pd/morse-drum/86")
        time.sleep(1)
        page.wait_for_selector('#eve_38').click()
        time.sleep(2)
        element = page.wait_for_selector("//*[@id='eve_294']/a", state='visible')
        element.click()
        time.sleep(12)
        page.fill("#customer-email", "shubham@raptorsupplies.co.uk")
        firstname_input = page.wait_for_selector('input[name="firstname"]')
        firstname_input.fill('Shubham')
        page.fill('input[name="lastname"]', 'Singh')
        page.fill('input[name="company"]', 'Raptor ')
        page.fill('input[name="street[0]"]', 'Mohan Estate')
        page.fill('input[name="city"]', 'Delhi')
        page.select_option("[name='country_id']", "IN")
        page.select_option("[name='region_id']", "Delhi")
        page.fill("[name='postcode']", "110021")
        page.fill("[name='telephone']", "123456789")
        time.sleep(4)
        page.get_by_label("Billing / Delivery Same").uncheck()
        page.get_by_label("Billing / Delivery Same").check()
        print('Same day delivery check !!')
        page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
        page.wait_for_selector('#eve_200').click()
        page.wait_for_selector("//*[@class='edit_shipping_info']").click()
        time.sleep(8)
        page.fill("[name='telephone']", "1234567890")
        page.evaluate('document.querySelector("#eve_200").removeAttribute("disabled")')
        page.wait_for_selector('#eve_200').click()
        page.get_by_text("Shipping Information Edit Shipping Details Edit Payment").click()
        page.get_by_label("Economy (6 - 10 days)").check()
        page.get_by_role("row", name="Express (5 - 7 days) $").click()
        page.get_by_label("Ex-Works Pickup").check()
        page.get_by_text("FedEx - International Priority").click()
        page.get_by_placeholder("xxxxxxxxx").click()
        page.get_by_placeholder("xxxxxxxxx").fill("4325665")
        page.get_by_role("button", name="Proceed to Payment").click()
        page.get_by_text("NET30 Payment").click()
        purschase_no = "//*[@id='eve_209']"
        page.fill(purschase_no, '6547685')
        # Click on checkbox of credit card
        net_payment_Checkbox = "//*[@id='net_check']"
        page.locator(net_payment_Checkbox).check()
        page.get_by_text("Proforma Invoice").click()
        time.sleep(2)
        page.get_by_role("textbox", name="Purchase Order # (Optional)").click()
        time.sleep(2)
        page.get_by_role("textbox", name="Purchase Order # (Optional)").fill("123456")
        time.sleep(2)
        page.get_by_role("textbox", name="Purchase Order # (Optional)").click()
        time.sleep(2)
        page.locator("#performa_check").check()
        page.locator('#performa_real').click()
        print('Performa Invoice Payment!!!')
        time.sleep(10)
        browser.close()

def main():
    for browser_type in ['chromium', 'firefox', 'webkit', 'safari', 'edge']:
        print(f"Running tests on {browser_type}")
        run_test(browser_type)

if __name__ == "__main__":
    main()
