'''
@Project:                   .py   #项目名称
@Description:               #描述
@Time:2022-04-15 16:56       #日期
@Author:MING                #创建人
'''
import torch
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
device = 'cpu'
print(device)
x_data = torch.Tensor([[1.0], [2.0], [3.0]]).to(device)
y_data = torch.Tensor([[0], [0], [1]]).to(device)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        y_pred = self.sigmoid(self.linear(x))
        return y_pred


if __name__ == '__main__':
    model = Model().to(device)
    criterion = torch.nn.BCELoss(reduction='mean')
    optimizer = torch.optim.SGD(params=model.parameters(), lr=0.1)

    for batch in range(1000):
        y_pred = model(x_data)
        loss = criterion(y_pred, y_data)
        print(batch, loss.data)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


        print('w=', model.linear.weight.item())
        print('b=', model.linear.bias.item())
        x_test = torch.Tensor([4.0]).to(device)
        y_test = model(x_test)
        print('y_pred', y_test.data)