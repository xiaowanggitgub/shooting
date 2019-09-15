class GameStats():
    '''跟踪游戏的统计信息'''
    
    def __init__(self,ai_settings):
        '''初始化统计信息'''
        self.ai_settings=ai_settings
        self.reset_stats()
        #游戏一开始处于非活动状态
        self.game_active=False
        self.hit_limit=ai_settings.hit_limit
        
        
    def reset_stats(self):
        '''初始化在游戏运行期间肯变化的统计信息'''
        self.hit_limit=self.ai_settings.hit_limit
