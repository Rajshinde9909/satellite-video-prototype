import requests

def fetch_wms_image(url, params, output_path):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
    else:
        print("Failed to fetch image:", response.status_code)

url = "https://example.com/wms"
params = {
    "service": "WMS",
    "request": "GetMap",
    "layers": "satellite",
    "bbox": "-80.0,25.0,-70.0,35.0",
    "width": "256",
    "height": "256",
    "srs": "EPSG:4326",
    "format": "image/png",
    "time": "2023-01-01T00:00:00Z/2023-01-01T00:30:00Z"
}
fetch_wms_image(url, params, "output.png")
