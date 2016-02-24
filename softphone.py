"""
Qxf2: Example script
 
"""
 
import unittest, time, os
from appium import webdriver
from time import sleep
 
class Android_Softphone(unittest.TestCase):
    "Class to run tests against the Softphone app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'AVD_for_Galaxy_Nexus_by_Google'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'com.orange.softphone.es'
        desired_caps['appActivity'] = 'cz.acrobits.provisioning.ui.ProvisioningActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def test_wifi_connection(self):
        "Testing the Softphone app"
 
        # click on configuration button
        configuration = self.driver.find_element_by_id('android:id/button2')
        configuration.click()
 
        # Assert that the WiFi settings window is shown
        elmnt = self.driver.find_element_by_id('android:id/empty')
        self.assertEqual('To see available networks, turn Wi-Fi on.', elmnt.get_attribute('text'))

 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_Softphone)
    unittest.TextTestRunner(verbosity=2).run(suite)
