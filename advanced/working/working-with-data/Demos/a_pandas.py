import pandas as pd
base_url= 'https://www.coolblue.nl/product/956915/apple-macbook-pro-14-inch-m4-10-core-cpu-10-core-gpu-16gb-512gb-spacezwart-qwerty.html'
table = pd.read_html(base_url) 
print(table)