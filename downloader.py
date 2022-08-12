from selenium import webdriver
import time
from tkinter import *

# filling in the web not working
# executable file bolgoh

path_to_download = 'C:/Users/bayar/Music'
url = 'https://getn.topsandtees.space/W1GnkMJ2JD'
fill_xpath = '/html/body/main/div/section/form/div/input[1]'
search_xpath = '/html/body/main/div/section/form/div/button'
download_prep_xpath = '/html/body/main/div/section/div[1]/div[1]/div/a'
download_xpath = '//*[@id="dl_wrap"]/p/span'

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": path_to_download}
options.add_experimental_option("prefs", prefs)

web = webdriver.Chrome(
    executable_path='./chromedriver.exe', options=options)

err = ''


def download():
    global music
    music = inp.get()
    print(music)
    try:
        web.get(url)
        time.sleep(2)

        print('fsyfuh')

        fill_inp = web.find_element_by_xpath(fill_xpath)
        print('nscj')
        fill_inp.send_keys(music)

        print('gtyuhj')

        search_btn = web.find_element(search_xpath)
        search_btn.click()

        download_prep_btn = web.find_element(download_prep_xpath)
        download_prep_btn.click()

        download_btn = web.find_element(download_xpath)
        download_btn.click()
    except:
        err = 'Something went wrong!'
        return err


root = Tk()
root.geometry('560x330')
root.title('Music Downloader')

wrapper = Frame(root)
wrapper.place(relx=.5, rely=.5, anchor=CENTER)

inp = Entry(wrapper, font=('Arial', 16), width=30)
inp.grid(column=0, row=0)

btn = Button(wrapper, text='Download', width=10,
             height=2, command=lambda: download())
btn.grid(column=1, row=0, padx=10)

out = Frame(root)
out.place(relx=10, rely=10)
msg = Label(out, text=err, font=('Arial', 16))


root.mainloop()
