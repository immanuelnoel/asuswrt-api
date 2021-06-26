import sys
sys.path.append('../')

from asuswrt import AsusWRT
from notifier import Notifier
import creds

def checkConnection(wanDetails, connectionIndex):

    alert_message = ""
    status = 1

    if wanDetails['wan' + connectionIndex + '_ipaddr'] == "0.0.0.0":
        
        status = 0
        alert_message = alert_message + "Internet connection " + str(int(connectionIndex) + 1) + ", which is your " + ("primary " if wanDetails['wan' + connectionIndex + '_primary'] == '1' else "secondary ") + "connection, seems to " + ("enabled " if wanDetails['wan' + connectionIndex + '_enable'] == '1' else "disabled ") + "and disconnected. " 

    return alert_message, status

def getWanDetails():

    router = AsusWRT(url=creds.admin['url'], username=creds.admin['username'], password=creds.admin['password'])
    wanDetails = router.get_wan_details()
    wanList = wanDetails['wans_dualwan'].split(' ')

    alert_message = ""
    wan_down = False
    
    for i in range(len(wanList)):
        
        wan_alert_message, status = checkConnection(wanDetails, str(i))
        alert_message = alert_message + wan_alert_message

        # Disconnected on the WAN port
        if status == 0:
            wan_down = True

    if wan_down == True and len(wanList) > 1:
        alert_message = alert_message + "However, you are using a dual WAN setup with the LAN port " + wanDetails['wans_lanport'] + " in an " + wanDetails['wans_mode'] + " mode, and probably not affected right now." 

    # Send notification
    if wan_down == True:

        notifier = Notifier(botID=creds.telegram['botID'], chatID=creds.telegram['chatID'])
        notifier.message(alert_message)
    
    return

# Invooke! 
getWanDetails()
