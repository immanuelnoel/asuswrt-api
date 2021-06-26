import sys
sys.path.append('../')

from asuswrt import AsusWRT
import creds

router = AsusWRT(url=creds.admin['url'], username=creds.admin['username'], password=creds.admin['password'])
sys = router.get_sys_info()

print('Model: %s' % sys['model'])
print('Firmware: %s' % sys['firmware'])
