import os
import sys
from datetime import datetime

mig_name = '__' + '_'.join(sys.argv[1:]) + '.sql'

migs = list(map(lambda x:x[:x.index('__')], os.listdir('./sql')))
today_mig = datetime.today().strftime('V%Y_%m_%d')

addon = 0

new_meg = ''

if today_mig in migs:
    while today_mig+'_'+str(addon) in migs:
        addon += 1
    new_mig = today_mig+'_'+str(addon)+mig_name
else:
    new_mig = today_mig+mig_name
open('./sql/'+new_mig, 'w+').close()
print(new_mig)
