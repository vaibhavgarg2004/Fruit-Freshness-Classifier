import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image

trained_model = None
class_names = [
    'Fresh Banana', 'Fresh Lemon', 'Fresh Lulo', 'Fresh Mango', 
    'Fresh Orange', 'Fresh Strawberry', 'Fresh Tamarillo', 'Fresh Tomato',
    'Stale Banana', 'Stale Lemon', 'Stale Lulo', 'Stale Mango', 
    'Stale Orange', 'Stale Strawberry', 'Stale Tamarillo', 'Stale Tomato'
]


# Load the pre-trained ResNet model
class FruitClassifierResNet(nn.Module):
    def __init__(self, num_classes=16):
        super().__init__()
        self.model = models.resnet50(weights='DEFAULT')
        # Freeze all layers except the final fully connected layer
        for param in self.model.parameters():
            param.requires_grad = False

        # Unfreeze layer4 and fc layers
        for param in self.model.layer4.parameters():
            param.requires_grad = True

        # Replace the final fully connected layer
        self.model.fc = nn.Sequential(
            nn.Linear(self.model.fc.in_features, num_classes)
        )

    def forward(self, x):
        x = self.model(x)
        return x


def predict(image_path):
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image_tensor = transform(image).unsqueeze(0)

    global trained_model

    if trained_model is None:
        trained_model = FruitClassifierResNet()
        trained_model.load_state_dict(torch.load("artifacts\saved_model.pth"))
        trained_model.eval()

    with torch.no_grad():
        output = trained_model(image_tensor)
        _, predicted_class = torch.max(output, 1)
        return class_names[predicted_class.item()]
