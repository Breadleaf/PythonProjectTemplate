"""
READ ME: DO NOT USE THIS FOR PRODUCTION CODE OR PERFORMANCE FOCUSED CODE!
"""

class Reference:
    """
    Class to simulate a reference from Java in Python.
    NOTE: DO NOT USE THIS FOR PRODUCTION CODE OR PERFORMANCE FOCUSED CODE!
    """

    def __init__(self, data: any) -> None:
        """
        Constructor
        """

        self.data = [data]


    def setData(self, data: any) -> None:
        """
        Set the data in the reference
        """

        self.data[0] = data


    def getData(self) -> any:
        """
        Get the data in the reference
        """

        return self.data[0]