class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = homepage
        self.f = []
        self.b = []

    def visit(self, url: str) -> None:
        self.f = []
        self.b.append(self.current)
        self.current = url

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.b))
        for _ in range(steps):
            self.f.append(self.current)
            self.current = self.b.pop()
        
        return self.current

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.f))
        for _ in range(steps):
            self.b.append(self.current)
            self.current = self.f.pop()
        
        return self.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)