class Settings():
    '''储存《外星人入侵》的所有设置的类'''
    
    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)
        #飞船的设置
        self.ship_speed_factor=1.5
        #子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=15
        self.bullet_height=3
        self.bullet_color=60,60,60
        self.bullets_allowed=3
        #矩形的设置
        self.rectangle_color=(20,20,20)
        self.rectangle_direction=1#矩形的方向
        #未击中矩形的设置
        self.hit_limit=3
        #被击中升级的矩形设置
        self.upgrade_number=4   #击中多少次矩形后升级

        #以什么样的速度加快节奏
        self.speedup_scale=2
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        #最开始的游戏参数
        self.rectangle_speed=0.5    #矩形的初始速度

    def increase_speed(self):
        '''提高速度设置'''
        self.rectangle_speed*=self.speedup_scale
