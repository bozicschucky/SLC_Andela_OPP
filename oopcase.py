class phone(object):
    def __init__(self,size=None,phone_type=None,screen_attributes=None,os_type=None):
        self.size=size
        self.phone_type=phone_type
        self.screen_attributes=screen_attributes
        self.os_type=os_type

    def call(self,number):
        self.number=number
        print('calling the number '+str(number))
        return "calling the number !" +str(number)

    def recieve(self):
        self.number=number
        return "Recieving call from the number " +str(number)

class smart_phone(phone):
    def __init__(self,size,phone_type,screen_attributes,os_type):
        self.size=size
        self.phone_type=phone_type
        self.screen_attributes=screen_attributes
        self.os_type=os_type
    '''
        self.size=5.7 
        self.phone_type='smart_phone'
        self.os_type='android_os or Ios'
        self.screen_attributes={'screen':'Touch_screen','multi-touch':True}'''

    def can_browse(self):
        self.web_page='www.twitter.com'
        print('I am browsing the internet '+str(self.web_page))
        return 'I am browsing the internet '+str(self.web_page)

    def can_watch_and_stream(self):
        self.videos='youtube videos playing on my device'
        print('watching '+(self.videos))
        return 'watching '+(self.videos)



class smart_phone(phone):
    def __init__(self,size,phone_type,screen_attributes,os_type):
        autorotate=90
        self.size=size
        self.phone_type=phone_type
        self.screen_attributes=screen_attributes
        self.os_type=os_type
        self.__autorotate=autorotate
    '''
        self.size=5.7 
        self.phone_type='smart_phone'
        self.os_type='android_os or Ios'
        self.screen_attributes={'screen':'Touch_screen','multi-touch':True} '''

    def can_browse(self):
        self.web_page='www.twitter.com'
        print('I am browsing the internet '+str(self.web_page))

class non_smart_phone(phone):
        def __init__(self,size,phone_type,screen_attributes,os_type):
            keyboard = 'qwerty'
            self.size=size
            self.phone_type=phone_type
            self.screen_attributes=screen_attributes
            self.os_type=os_type
            self.__keyboard=keyboard

        '''
            self.size=2
            self.phone_type='regular_phone'
            self.os_type='taizen_os'
            self.screen_attributes={'screen':'non_touch_screen','buttons':True,'Touch_screen':False} '''

        def play_snake_game(self):
            self.game='Preinstalled game of snake to be played by user'
            print('I always play the '+self.game)
            return 'I always play the '+self.game

        def keyboard(self):
            self.press='i normally interact with the key board'
            print(self.press)
            return self.press

'''

s=smart_phone(5.7,'smart_phone','android_os or Ios',{'screen':'Touch_screen','multi-touch':True} )
s.can_browse()

n=non_smart_phone(2,'regular_phone','taizen_os',{'screen':'non_touch_screen','buttons':True,'Touch_screen':False})
n.play_snake_game()

'''