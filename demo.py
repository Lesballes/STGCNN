from dgmr import DGMR
import torch.nn.functional as F
import torch
model = DGMR(
        forecast_steps=4,
        input_channels=1,
        output_shape=128,
        latent_channels=384,
        context_channels=192,
        num_samples=3,
    )
x = 
y = 
out = model(x)

loss = F.mse_loss(y, out)
loss.backward()