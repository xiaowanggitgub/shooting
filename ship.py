import pygame
class Ship():
    
    def __init__(self,screen,ai_settings):
        '''初始化飞船并设置初始位置'''
        self.screen=screen
        self.ai_settings=ai_settings
        
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        #将每艘新飞船放在屏幕左侧中央
        self.rect.centery=self.screen_rect.centery
        
        self.image=pygame.transform.rotate(self.image , 270)#旋转图像
        self.rect.left=self.screen_rect.left
        #在飞船的属性center中储存小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)##可以储存小数，但最终只能显示整数
        
        #移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_top=False
        self.moving_bottom=False
    def update(self):
        '''根据移动标志调整飞船位置'''
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
         
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor 
            
        if self.moving_top and self.rect.top>0:
            self.centery -= self.ai_settings.ship_speed_factor
            
        if self.moving_bottom and self.rect.bottom<self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            
            #根据self.center更新rect对象
        self.rect.centerx=self.centerx
        self.rect.centery=self.centery
        
        
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.centery=self.screen_rect.centery
        self.centerx=30
