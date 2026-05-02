import zipfile  
import os  
from playwright.sync_api import sync_playwright

def start():  
    try:  
        print("Searching for identity zip...")  
        # Double check: ensure this filename matches your GitHub EXACTLY  
        zip_filename = 'sovereign_identity.zip'   
          
        if not os.path.exists(zip_filename):  
            print(f"ERROR: {zip_filename} not found in the folder!")  
            return

        print("Unzipping identity to /tmp...")  
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:  
            zip_ref.extractall('/tmp/identity')

        with sync_playwright() as p:  
            print("Launching browser as YOU...")  
            browser = p.chromium.launch_persistent_context(  
                user_data_dir='/tmp/identity',  
                headless=True,  
                args=["--no-sandbox", "--disable-setuid-sandbox"]  
            )  
              
            page = browser.new_page()  
            print("Navigating to Grok...")  
            page.goto("https://grok.com")

            if "Connect your X account" not in page.content():  
                print("SUCCESS: You are logged into Grok!")  
            else:  
                print("FAIL: Session rejected. Identity file might be old.")  
              
            browser.close()

    except Exception as e:  
        print(f"CRITICAL ERROR: {str(e)}")

if __name__ == "__main__":  
    start()  
