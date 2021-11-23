import requests
import streamlit as st

from bs4 import BeautifulSoup
import jdatetime
import re
site = requests.get('https://coinmarketcap.com/currencies/bitcoin/')
findtext = BeautifulSoup(site.text ,'html.parser')

bitcoinprice = findtext.find('div' , attrs={'class':'priceValue'})
nowtime=jdatetime.datetime.now()

price = float(re.sub(',','',bitcoinprice.text[1:]))
  

def bitprice():
    st.write('%s dollor is the price of bitcoin in %s' % (price ,nowtime))



st.write('''
# This App gives the price of **Bitcoin** at the moment

check the price
''')




if st.button('click to check') == True :
    bitprice()
