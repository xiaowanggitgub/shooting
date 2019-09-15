import sys

import pygame

from bullet import Bullet

from time import sleep


def check_keydown_events(event,stats, ai_settings, screen, ship, bullets):
    '''响应按键'''
                
                #按下右键时，飞船连续移动开关打开
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
                
                #按下左键时，飞船连续移动开关打开
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
        
    elif event.key==pygame.K_UP:
        ship.moving_top=True
        
    elif event.key==pygame.K_DOWN:
        ship.moving_bottom=True
        
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
    elif event.key==pygame.K_q:
        sys.exit() 
           
    elif event.key==pygame.K_p:
        start_game(stats,bullets,ai_settings,ship)
        
        
def check_keyup_events(event,ship):
    '''响应松开'''
     #松开右键时，飞船连续移动开关关闭
    if  event.key==pygame.K_RIGHT:
        ship.moving_right=False
    #松开左键时，飞船连续移动开关关闭
    if  event.key==pygame.K_LEFT:
        ship.moving_left=False
        
    if event.key==pygame.K_UP:
        ship.moving_top=False
        
    if event.key==pygame.K_DOWN:
        ship.moving_bottom=False

def check_events(ai_settings, stats,play_button,screen, ship, bullets):
    '''响应按键和鼠标事件'''
    #监视鼠标和电脑事件
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:#鼠标点击关闭窗口
            sys.exit()#退出程序
            
            #监测按键
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,stats, ai_settings, screen, ship, bullets)
                
               #监测松键
        elif event.type==pygame.KEYUP: 
            check_keyup_events(event,ship)
            
                        #检测点击屏幕
        elif event.type==pygame.MOUSEBUTTONDOWN:#点击屏幕行为
            mouse_x,mouse_y=pygame.mouse.get_pos()#它返回一个元组，其中包含玩家单击时鼠标的x 和y 坐标
            check_play_button(ai_settings,stats,play_button,ship,bullets,mouse_x,mouse_y)
            
  
def fire_bullet(ai_settings,screen,ship,bullets):
    '''如果子弹还没达到上限，就再发一颗子弹'''
    if len(bullets)<=ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings, screen, ship)
        #创建一颗子弹并加入编组bullets中
        bullets.add(new_bullet)
        

            
def update_screen(ai_settings,stats,play_button,ship, bullets,rectangle,rectangles):
    '''更新屏幕上的图像并切换到新屏幕'''

    #每次循环时都重绘屏幕

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():#方法bullets.sprites() 返回一个列表，其中包含编组
                            #bullets 中的所有精灵。为在屏幕上绘制发射的所有子弹
        bullet.draw_bullet()
    #检查子弹和矩形的碰撞,并删除相应子弹
    checke_bullet_anlien_collisions(ai_settings,bullets,rectangle,rectangles)
    
    #记录未击中矩形的子弹,并删除子弹
    not_hit(stats,bullets)
    
    #超过限定子弹未击中，结束游戏
    stop_game(stats,bullets,ship)
        #在屏幕上绘制矩形
    rectangle.draw_bullet()
    
    if not stats.game_active:
        
        play_button.draw_button()#为了让按钮处于屏幕顶层，绘制完其他元素再绘制按钮
    
    
def update_bullets(bullets):
    '''更新子弹位置'''
    #更新子弹位置
    bullets.update()
    
def update_rectangles(ai_settings,rectangle):
    '''更新矩形位置'''
    global i
    if i==ai_settings.upgrade_number:#如果矩形被击中5次，移动速度加快
        ai_settings.increase_speed()
        i=0     #速度升级后次数累计归零重新开始计数
        print(ai_settings.rectangle_speed)
    rectangle.update(ai_settings)

i=0            
def checke_bullet_anlien_collisions(ai_settings,bullets,rectangle,rectangles):
    '''检查子弹和矩形的碰撞'''
    #检查是否有子弹击中了矩形
    #如果有，就删除相应的子弹
    bullet_list=pygame.sprite.spritecollideany(rectangle,bullets)
    global i   #i是子弹与矩形发生碰撞的次数累计
     
    if bullet_list != None:
        i+=1

    collision=pygame.sprite.groupcollide(bullets,rectangles,True,False)

    '''这行代码遍历编组bullets 中的每颗子弹，再遍历编组aliens 中的每个外星人。每当有子弹和外星人
    #的rect 重叠时，groupcollide() 就在它返回的字典中添加一 个键-值对。两个实参True 告诉
    #Pygame删除发生碰撞的子弹和外星人。（要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星
    #人，可将第一个布尔实参设置 为False ，并让第二个布尔实参为True 。这样被击中的外星人将消失，
    #但所有的子弹都始终有效，直到抵达屏幕顶端后消失。）'''
            
def count_not_hit(bullets):
    '''记录未击中矩形的子弹,并删除子弹'''
    count=0
        #删除已消失子弹
    for bullet in bullets.copy():
        if bullet.rect.left>1200:
            count+=1
            bullets.remove(bullet)
            
    print(len(bullets))
    
def check_play_button(ai_settings,stats,play_button,ship,bullets,mouse_x,mouse_y):
    '''在玩家单击play按钮时开始新游戏'''
    #测试点是否在矩形内，前面需要一个rect对象，检测点是否在其内
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active: #如果游戏在运行点击play区域也不会重置信息                   
        start_game(stats,bullets,ai_settings,ship)
        
def start_game(stats,bullets,ai_settings,ship):
    '''开始游戏'''
        #隐藏光标
    pygame.mouse.set_visible(False)
        #重置游戏统计信息                                  
    stats.reset_stats()
    stats.game_active=True
    ai_settings.initialize_dynamic_settings()
        
        #清空子弹列表
    bullets.empty()
    #让飞船居中
    ship.center_ship()
    ship.update()
    ship.blitme()
    
def not_hit(stats,bullets):
    '''没有射击到矩形,删除屏幕外子弹'''
    for bullet in bullets.sprites():#加了s的
        if bullet.rect.right>=bullet.screen_rect.right :
            #将hit_limit减1
            stats.hit_limit-=1
            bullets.remove(bullet)
            
def stop_game(stats,bullets,ship):        
    if stats.hit_limit==0:
        #暂停
        sleep(0.5)
        
        #清空子弹列表
        bullets.empty()
    
        #将飞船放到屏幕底端中央
        ship.center_ship()
    
        stats.game_active=False
        pygame.mouse.set_visible(True)#鼠标可见
    
