class NavigateTo:
    def __init__(self, driver):
        self.driver = driver
        Print("init")

    def goTo(self, url, verifyText):
        self.driver.get(url)
        return True/False