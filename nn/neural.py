import torch
import torch.nn as nn



class Net(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.network = nn.Sequential (
            nn.Linear(9, 6),
            nn.ReLU(),
            nn.Linear(6, 4),
            nn.ReLU(),
            nn.Linear(4, 3),
        )
    
    def forward(self, x):
        return self.network(x)
    


if __name__ == "__main__":
    n = Net()
    t = torch.randn((1, 10))
    print(n(t))



"""
FOR BINARY CLASSIFY:
    self.network = nn.Sequential (
            nn.Linear(8, 4),
            nn.ReLU(),
            nn.Linear(4, 1),
            nn.Sigmoid()
        )



"""