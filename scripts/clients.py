import sys
sys.path.append('../')

from asuswrt import AsusWRT
import creds

router = AsusWRT(url=creds.admin['url'], username=creds.admin['username'], password=creds.admin['password'])
clients = router.get_online_clients()

for client in clients:
    for attribute in ['name', 'alias', 'mac', 'ip', 'interface', 'rssi']:
        print('%s: %s' % (attribute.capitalize(), getattr(client, attribute)))
    print()