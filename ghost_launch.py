import zipfile  
from playwright.sync_api import sync_playwright

def start():  
    # 1. Unzip the identity file you uploaded to GitHub  
    print("Unzipping your identity...")  
    with zipfile.ZipFile('sovereign_identity.zip', 'r') as zip_ref:  
        zip_ref.extractall('/tmp/identity')

    # 2. Launch the browser using that identity  
    with sync_playwright() as p:  
        print("Launching browser as YOU...")  
        browser = p.chromium.launch_persistent_context(  
            user_data_dir='/tmp/identity',  
            headless=True,   
            args=["--no-sandbox"]  
        )  
          
        page = browser.new_page()  
        page.goto("https://grok.com")  
          
        if "Connect your X account" not in page.content():  
            print("SUCCESS: You are logged into Grok!")  
        else:  
            print("FAIL: The session didn't work. Maybe you logged out of Chrome?")  
          
        browser.close()

if __name__ == "__main__":  
    start()  
