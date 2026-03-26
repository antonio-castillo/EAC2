from django.test import TestCase

# Create your tests here.
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User

class MySeleniumTests(StaticLiveServerTestCase):
    # no crearem una BD de test en aquesta ocasió comentem la línia)
    #fixtures = ['testdb.json',]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)

        # creamos super usuario
        user = User.objects.create_user("isard", "isard@isardvdi.com", "pirineus")
        user.is_superuser = True
        user.is_staff = True
        user.save()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_m03eac2(self):
        # Vamos a la pagina principal
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))

        # Comprobamos el por el titulo que es la pagina que queremos
        self.assertEqual( self.selenium.title , "Log in | Django site admin" )

        # Introducimos los datos del user y pass y nos logueamos
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('isard')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('pirineus')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
        time.sleep(1)
        
        #vamos al apartado Add
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/auth/user/add'))
        
        #Rellenamos los datos del nuevo usuario
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('StaffIOC')
        password_input = self.selenium.find_element(By.NAME,"password1")
        password_input.send_keys('Pirineo2026')
        password_input = self.selenium.find_element(By.NAME,"password2")
        password_input.send_keys('Pirineo2026')
        self.selenium.find_element(By.XPATH,'//input[@value="Save"]').click()
        time.sleep(2)
        
        

