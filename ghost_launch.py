import zipfile  
from playwright.sync_api import sync_playwright

def start():  
    try:  
        print("Unzipping identity...")  
        # I am using the name exactly as seen in your previous screenshot  
        with zipfile.ZipFile('sovereignidentity.zip', 'r') as zip_ref:  
            zip_ref.extractall('/tmp/identity')  
          
        with sync_playwright() as p:  
            print("Launching browser as YOU...")  
            browser = p.chromium.launch_persistent_context(  
                user_data_dir='/tmp/identity',  
                headless=True,  
                args=["--no-sandbox", "--disable-setuid-sandbox"]  
            )  
            page = browser.new_page()  
            page.goto("https://grok.com")  
              
            if "Connect your X account" not in page.content():  
                print("SUCCESS: You are logged into Grok!")  
            else:  
                print("FAIL: Session rejected.")  
            browser.close()  
    except Exception as e:  
        print(f"ERROR: {e}")

if __name__ == "__main__":  
    start()  
