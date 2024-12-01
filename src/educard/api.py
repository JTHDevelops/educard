from gptk import Property

class API:
    
    @Property(default="valid value")
    def tester(self):
        '''
        '''


    @Property("The window Property")
    def _window(self):
        pass
    
    def destroy(self):
        self._window.destroy()

    def log(self, value):
        print(value)
    
__all__ = ['API']