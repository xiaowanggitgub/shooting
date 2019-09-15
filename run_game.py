import pygame

from pygame.sprite import Group

from button import Button
from bullet import Bullet
from settings import Settings
from ship import Ship
from rectangle import Rectangle
from game_stats import GameStats
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
    (ai_settings.screen_width,ai_settings.screen_height))#创建一个窗口
    pygame.display.set_caption('hit')#窗口名
    
    #设置背景色
    bg_color=ai_settings.bg_color
    
    #创建一艘飞船
    ship=Ship(screen,ai_settings)
    
    #创建一个矩形
    rectangle=Rectangle(ai_settings,screen)

    #创建play按钮
    msg='play'
    play_button=Button(ai_settings,screen,msg)
    
    #创建控制游戏的实例
    stats=GameStats(ai_settings)
    
    
    bullets=pygame.sprite.Group()#这个编组是pygame.sprite.Group 类的一个实例；pygame.sprite.Group
                    #类似于列表，但提供了有助于开发游戏的额外功 能。
    rectangles=pygame.sprite.Group()
    rectangles.add(rectangle)
    
    #开始游戏的主循环
    while True:
        
        #监视鼠标和电脑事件
        gf.check_events(ai_settings, stats,play_button,screen, ship, bullets)
        
        
        if stats.game_active:
            
            ship.update()
        
            #删除已消失的子弹
            gf.update_bullets(bullets)
            
            gf.update_rectangles(ai_settings,rectangle)
            
            gf.update_bullets(bullets)
        
            #更新屏幕上的图像并切换到新屏幕        
        
            
        screen.fill(ai_settings.bg_color)
        #背景色填充屏幕
        
        ship.blitme()
        gf.update_screen(ai_settings,stats,play_button,ship, bullets,rectangle,rectangles )
        #让最近绘制的屏幕可见
        pygame.display.flip()
run_game()


