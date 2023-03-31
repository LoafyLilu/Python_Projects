

class Thing:

    var1 = None #Public
    _var2 = None #Protected
    __var3 = None #Private

    #constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    #public function
    def displayPublic(self):

        #acessing public
        print("Public Data: ", self.var1)

    #protected function
    def _displayProtected(self):

        #accessing protected
        print("Protected Data: ", self._var2)

    #private function
    def __displayPrivate(self):

        #accessing private
        print("Private Data: ", self.__var3)

    #public function
    def accessPrivate(self):

        #accessing private function
        self.__displayPrivate()

#child class
class Another(Thing):

    #constructor
    def __init__(self,var1,var2,var3):
        Thing.__init__(self,var1,var2,var3)

    #public function
    def accessProtected(self):

        #accessing protected function
        self._displayProtected()


obj = Another("Super", "Sailor", "Senshi")

#calling public functions to access protected and private
obj.displayPublic()
obj.accessProtected()
obj.accessPrivate()




        
        

    
    
    
