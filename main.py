import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd
from io import BytesIO
import ast

def draw_polygons_from_csv(csv_path, row_idx):
    # Read CSV file
    df = pd.read_csv(csv_path)
    
    if row_idx >= len(df):
        print(f"Row index {row_idx} out of range.")
        return
    
    row = df.iloc[row_idx]
    image_url = row['image_url']
    # image_width = int(row['image_width'])
    # image_height = int(row['image_height'])
    
    try:
        polygons = ast.literal_eval(row['view_annotation_result_Polygon'])  # Safely parse string to list of dictionaries
    except Exception as e:
        print(f"Error parsing polygons: {e}")
        return
    
    # Load the image from URL
    response = requests.get(image_url)
    if response.status_code != 200:
        print(f"Failed to fetch image from {image_url}")
        return
    
    image = np.array(bytearray(response.content), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    if image is None:
        print(f"Error decoding image from {image_url}")
        return
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Define multiple colors
    
    for i, poly in enumerate(polygons):
        points = np.array(poly['points'], np.int32)
        points = points.reshape((-1, 1, 2))
        color = colors[i % len(colors)]  # Cycle through colors if more polygons
        cv2.polylines(image, [points], isClosed=True, color=color, thickness=2)
        # cv2.fillPoly(image, [points], (color[0], color[1], color[2], 50))  # Semi-transparent fill
    
    # Show the image
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis("off")
    plt.show()

# Example usage
draw_polygons_from_csv("label_validation.csv", 0)
