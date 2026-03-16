class Monitor:
    """A class to represent a monitor model"""
    def __init__(self,model:str,width:int,height:int):
        """Initialise the attributes of the Monitor class"""
        self.model = model
        self.width = width
        self.height = height

    def get_resolution(self):
        """Return the resolution of a monitor width and height"""
        return self.width,self.height

    def get_total_pixels(self):
        """Calculate and return the total number od pixels of the monitor"""
        return self.width * self.height