import pygame.font
class Button():
    
    def __init__(self,ai_settings,screen,msg):
        '''初始化按钮属性'''
        self.screen=screen
        self.screen_rect=screen.get_rect()
        
        #设置按钮尺寸和其他属性
        self.width,self.height=200,50
        self.button_color=(0,255,2)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont('arial',48)#实参None让pygame使用默认字体，48是字号
        
        #创建按钮的rect对象，并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        
        #按钮的标签只需要设置一次
        self.prep_msg(msg)#msg是要在按钮中显示的文本
        
    def prep_msg(self,msg):
        '''将msg渲染为图像，并使其在按钮上居中'''
        self.msg_image=self.font.render(msg,True,self.text_color,
                        self.button_color)#font.render()将存储在msg中的文本转换为图像
    #方法font.render() 还接受一个布尔实参，该实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘
    #更平滑）。余下的两个实参分别是文本颜色和背景色。如果没有指定背景色，Pygame将以透明背景的方式渲染文本）。
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
        
    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        #这里的self.msg_image_rect是位置参数，指出要把surface画在屏幕上的哪个位置
        
        
        
        

