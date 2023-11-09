


import os, sys
import yshs
yshs.api_key = os.getenv('YSHS_API_KEY')

response = yshs.Models.list(refresh=True, return_all_info=True)
print(response)

