import pygame
from pygame.sprite import Sprite
class Rectangle(Sprite):
    '''创建一个矩形'''
    def __init__(self,ai_settings,screen):
        '''初始化矩形属性,并设定其位置'''
        super(Rectangle,self).__init__()
        
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect=pygame.Rect(10,20,30,60)#后面2个参数为矩形的宽和高
        #设置其位置
        self.rect.centery=self.screen_rect.centery
        self.rect.right=self.screen_rect.right
        self.centery = float(self.rect.centery)
        #设置颜色
        self.color=ai_settings.rectangle_color
        #设置移动速度
        self.speed_factor=ai_settings.rectangle_speed
        self.y=float(self.rect.y)
        
    def update(self,ai_settings):
        '''更新矩形位置'''
        self.centery+=ai_settings.rectangle_speed*ai_settings.rectangle_direction
        if self.rect.bottom>=self.screen_rect.bottom:#由于像素点的不精确，最后能写具体的大于等于就不写==容易出BUG
            ai_settings.rectangle_direction=-1
        elif self.rect.top<=0:
            ai_settings.rectangle_direction=1
            
        self.rect.centery=self.centery
        
    def draw_bullet(self):
        '''在屏幕上绘制矩形'''
        pygame.draw.rect(self.screen,self.color,self.rect)
