import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'household_services_platform.settings')
django.setup()

from services.models import Service

image_map = {
    'Cleaning': r'C:\Users\Roqaiah Anjum E\.gemini\antigravity\brain\9b315ea2-88c7-4463-98a8-e6c68ccb1d75\service_cleaning_1779128091641.png',
    'Dishwashing': r'C:\Users\Roqaiah Anjum E\.gemini\antigravity\brain\9b315ea2-88c7-4463-98a8-e6c68ccb1d75\service_dishwashing_1779128455614.png',
    'Kitchen Cleaning': r'C:\Users\Roqaiah Anjum E\.gemini\antigravity\brain\9b315ea2-88c7-4463-98a8-e6c68ccb1d75\service_kitchen_1779128519263.png',
    'Bathroom Cleaning': r'C:\Users\Roqaiah Anjum E\.gemini\antigravity\brain\9b315ea2-88c7-4463-98a8-e6c68ccb1d75\service_bathroom_1779128537278.png',
    'Laundry': r'C:\Users\Roqaiah Anjum E\.gemini\antigravity\brain\9b315ea2-88c7-4463-98a8-e6c68ccb1d75\service_laundry_1779128555665.png',
    'Fan Cleaning': r'C:\Users\Roqaiah Anjum E\.gemini\antigravity\brain\9b315ea2-88c7-4463-98a8-e6c68ccb1d75\service_fan_1779128749311.png'
}

def update():
    for name, path in image_map.items():
        try:
            service = Service.objects.get(name=name)
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    filename = f"{name.lower().replace(' ', '_')}.png"
                    service.image.save(filename, File(f), save=True)
                print(f"Successfully attached image for {name}.")
            else:
                print(f"Image not found at path: {path}")
        except Service.DoesNotExist:
            print(f"Service '{name}' not found in database.")

if __name__ == '__main__':
    update()
