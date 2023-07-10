from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def scrapeSite(path):
    # * This function scrapes AI-Roadmap.com and return the results in a txt file.
    userinput = path
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    url = "https://ai-roadmap.com/"
    driver.get(url)
    sleep(10)
    input_field = driver.find_element(By.ID, 'react-aria-1')
    input_field.clear()
    input_field.send_keys(userinput)
    button = driver.find_element(By.XPATH, "/html[@class='dark-theme']/body/div[@id='__next']/div[2]/div[@class='nextui-c-bsxZDy']/div[@class='nextui-c-fdHeMm nextui-c-fdHeMm-dwxLNB-responsive-true nextui-c-fdHeMm-iizPHCF-css']/div[@class='nextui-c-kRHeuF nextui-c-kRHeuF-ijDEIix-css nextui-grid-item nextui-grid-container content']/div[@class='nextui-c-kRHeuF nextui-c-kRHeuF-ibBQlvc-css nextui-grid-item xs sm md lg xl'][1]/div[@class='box']/div[@class='nextui-c-ceYOvq']/div[@class='nextui-c-BDLTQ nextui-c-jMTBsW nextui-c-gulvcB nextui-c-BDLTQ-eZMbDJ-variant-shadow nextui-c-BDLTQ-fmlsco-borderWeight-light nextui-c-BDLTQ-cuwTXc-disableAnimation-false card']/form/div[@class='formContainer']/div[2]/button[@class='nextui-c-iWjDFM nextui-c-gulvcB nextui-c-iWjDFM-hkKLfu-color-default nextui-c-iWjDFM-fbAdQA-size-lg nextui-c-iWjDFM-cwXrJp-borderWeight-normal nextui-c-iWjDFM-iPJLV-css nextui-button nextui-button--ready nextui-c-bBkWuD submitButton']")
    button.click()
    sleep(70)  # Replace with the class name of the resulting content
    page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page_source, 'html.parser')
    divs_hello = soup.find_all('div', class_='styles_nodeOtherLevel__SZmQG')
    with open(r"C:/Shaven Stuff\Web Development/DjangoLearning/CourseApp - Copy/base/output.txt", 'w') as file:
        for div_hello in divs_hello:
            inner_div_text = div_hello.find('div').text
            file.write(inner_div_text + '\n')


def searchsite(sites):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    for i in sites:
        site = sites[i]
        match site:
            case "youtube":
                url = "www.youtube.com"
                driver.get(url)
                with open(r"output.txt") as file:
                    for item in file:
                        input_field = driver.find_element(By.ID, 'u147-search-form-autocomplete--3')
                        input_field.clear()
                        input_field.send_keys(userinput)
                        

            case "udemy":
                url = "www.udemy.com"
                driver.get(url)
                with open(r"output.txt") as file:
                    for item in file:
                        print(item)

            case "edex":
                url = "www.edex.com"
                driver.get(url)
                with open(r"output.txt") as file:

            case _:
                print("No valid site")
    


def index(request):
    # * Renders The Home Page
    return render(request, 'index.html')


def about(request):
    # * Renders the about page
    return render(request, 'about.html')


def start(request):
    # * Renders the data collection page
    return render(request, 'start.html')


def check(request):

    sites = []
    if request.method == 'POST':
        prompt = request.POST['pathway']
        sites.append(request.POST.get('youtube'))
        sites.append(request.POST.get('udemy'))
    # Uses the user's prompt to generate the roadmap
      # u_name is the name of the input tag
    scrapeSite(prompt)
    searchsites(sites)
    context = {
        'path': prompt,
    }
    return render(request, 'generate.html', context)
