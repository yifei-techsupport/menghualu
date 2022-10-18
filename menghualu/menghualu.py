import playwright
from playwright.sync_api import sync_playwright
import time
import random
import math
import subprocess


def open_browser_auto_refresh(url_list, interval_time):
    with sync_playwright() as p:
        brow = 0
        # choose chromium
        try:
            browser_chro = p.chromium.launch(headless=False)
            brow = brow + 1
        except:
            pass
        
        # choose firefox
        try:
            browser_ff = p.firefox.launch(headless=False)
            brow = brow + 1
        except:
            pass

        # choose webkit
        try:
            browser_wb = p.webkit.launch(headless=False)
            brow = brow + 1
        except:
            pass

        for url in url_list:
            try:
                page_chro = browser_chro.new_page()
                page_chro.goto(url)
            except:
                pass
            try:
                page_ff = browser_ff.new_page()
                page_ff.goto(url)
            except:
                pass
            try:
                page_wb = browser_wb.new_page()
                page_wb.goto(url)
            except:
                pass
        if brow > 0:
            time.sleep(interval_time+random.randint(1,10))
            try:
                browser_chro.close()
            except:
                pass
            try:
                browser_ff.close()
            except:
                pass
            try:
                browser_wb.close()
            except:
                pass
        else:
            raise Exception("无浏览器可用")


def menghualu():
    url_dict = {'1':'https://v.qq.com/x/cover/mzc00200p51jpn7/t0042h23a9d.html',
            '2':'https://v.qq.com/x/cover/mzc00200p51jpn7/s004237dmoq.html',
            '3':'https://v.qq.com/x/cover/mzc00200p51jpn7/w0042lrzofx.html',
            '4':'https://v.qq.com/x/cover/mzc00200p51jpn7/n0042uyyrj8.html',
            '5':'https://v.qq.com/x/cover/mzc00200p51jpn7/c0042hveuha.html',
            '6':'https://v.qq.com/x/cover/mzc00200p51jpn7/l0042qaaw0x.html',
            '7':'https://v.qq.com/x/cover/mzc00200p51jpn7/q004296az63.html',
            '8':'https://v.qq.com/x/cover/mzc00200p51jpn7/x0042d6te3m.html',
            '9':'https://v.qq.com/x/cover/mzc00200p51jpn7/g0042oxlxg4.html',
            '10':'https://v.qq.com/x/cover/mzc00200p51jpn7/p0042grwzzr.html',
            '11':'https://v.qq.com/x/cover/mzc00200p51jpn7/s0043gdo81y.html',
            '12':'https://v.qq.com/x/cover/mzc00200p51jpn7/n0043f59pdt.html',
            '13':'https://v.qq.com/x/cover/mzc00200p51jpn7/j0043h9kf6x.html',
            '14':'https://v.qq.com/x/cover/mzc00200p51jpn7/e00435qwu7d.html',
            '15':'https://v.qq.com/x/cover/mzc00200p51jpn7/a0043v0hqp3.html',
            '16':'https://v.qq.com/x/cover/mzc00200p51jpn7/y00435ad386.html',
            '17':'https://v.qq.com/x/cover/mzc00200p51jpn7/v00432fku1h.html',
            '18':'https://v.qq.com/x/cover/mzc00200p51jpn7/v0043tq177l.html',
            '19':'https://v.qq.com/x/cover/mzc00200p51jpn7/u0043cryv8q.html',
            '20':'https://v.qq.com/x/cover/mzc00200p51jpn7/j0043nxglzx.html',
            '21':'https://v.qq.com/x/cover/mzc00200p51jpn7/q0043hgkoz4.html',
            '22':'https://v.qq.com/x/cover/mzc00200p51jpn7/k0043gxinbi.html',
            '23':'https://v.qq.com/x/cover/mzc00200p51jpn7/z0043zmqjyu.html',
            '24':'https://v.qq.com/x/cover/mzc00200p51jpn7/k0043kq7gr7.html',
            '25':'https://v.qq.com/x/cover/mzc00200p51jpn7/d00430h3l09.html',
            '26':'https://v.qq.com/x/cover/mzc00200p51jpn7/s0043wrdxrx.html',
            '27':'https://v.qq.com/x/cover/mzc00200p51jpn7/v00434g5vc6.html',
            '28':'https://v.qq.com/x/cover/mzc00200p51jpn7/g0043f4h9q5.html',
            '29':'https://v.qq.com/x/cover/mzc00200p51jpn7/q0043lqngee.html',
            '30':'https://v.qq.com/x/cover/mzc00200p51jpn7/p0043pvod9k.html',
            '31':'https://v.qq.com/x/cover/mzc00200p51jpn7/c0043ll9a3s.html',
            '32':'https://v.qq.com/x/cover/mzc00200p51jpn7/z0043cus21w.html',
            '33':'https://v.qq.com/x/cover/mzc00200p51jpn7/k0043fgsydd.html',
            '34':'https://v.qq.com/x/cover/mzc00200p51jpn7/n0043712oit.html',
            '35':'https://v.qq.com/x/cover/mzc00200p51jpn7/c0043wgocl9.html',
            '36':'https://v.qq.com/x/cover/mzc00200p51jpn7/b0043zljvjo.html',
            '37':'https://v.qq.com/x/cover/mzc00200p51jpn7/v0043ujmfn0.html',
            '38':'https://v.qq.com/x/cover/mzc00200p51jpn7/l0043xvxjzl.html',
            '39':'https://v.qq.com/x/cover/mzc00200p51jpn7/y0043nfzbsm.html',
            '40':'https://v.qq.com/x/cover/mzc00200p51jpn7/y0043a3qg2h.html'}

    interval_time = 1380
    # first_time = input('是否为初次使用，请输入Y或N: ')
    # if str.lower(first_time) == 'y':
    #     subprocess.Popen("playwright install", close_fds=True)
	
    selected_ep_str = input('请选择6集或更少的非会员集，以‘/’隔开（例如1/2/3/5/6）: ')
    running_time = input('请输入使用时长，单位为分钟（例：600）: ')
    selected_ep = selected_ep_str.split('/')
    selected_ep = list(set(selected_ep))
    url_list = []
    for ep in selected_ep:
        try:
            url_list.append(url_dict[ep])
        except:
            pass
    try:
        running_time = int(running_time)
    except:
        running_time = 0
    for i in range(math.ceil(running_time*60/interval_time)):
        if len(url_list) > 0:
            print(i)
            open_browser_auto_refresh(url_list, interval_time)
