import requests
from bs4 import BeautifulSoup

def get_aksam_namaz_vakti():
    url = "https://namazvakitleri.diyanet.gov.tr/tr-TR/14543/winterthur-icin-namaz-vakti"
    
    # Send a GET request
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails
    
    # Parse the page content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the Akşam Namazı time using the data-vakit-name attribute
    aksam_vakti = soup.find("div", {"class": "tpt-cell", "data-vakit-name": "aksam"})
    
    if aksam_vakti:
        aksam_time = aksam_vakti.find("div", {"class": "tpt-time"}).text.strip()
        return aksam_time
    else:
        return "Akşam namaz vakti bulunamadı."



# Get and print the Akşam Namazı time
aksam_time = get_aksam_namaz_vakti()
print(f"Winterthur Akşam Namazı Vakti: {aksam_time}")
