import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射子弹进行管理的类'''
    
    def __init__(self, ai_settings, screen, ship):
        '''在飞船的位置创造一个子弹对象'''
        super(Bullet,self).__init__()#可简写为super().__init__()
        # super(Bullet,self) 首先找到 Bullet 的父类（就是类 Sprite），
        #然后把类 Bullet 的对象转换为类 Sprite 的对象
        self.screen=screen
        self.screen_rect=screen.get_rect()
        
        #在（0,0)出创建一个表示子弹的矩形，再设置正确位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.centery
        
        #储存用小数表示的子弹位置
        self.x=float(self.rect.x)
        
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
      
        

    def update(self):
        '''向上移动子弹'''
        #更新表示子弹位置的小数值
        self.x+=self.speed_factor
        #更新表示子弹的rect位置
        self.rect.x=self.x
        
    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)#blit绘制图像draw绘制图形
        #函数draw.rect() 使用存储在self.color 中的颜色填充表示子弹的rect 占据的屏幕部分
        
        
        
        
        
        
        

