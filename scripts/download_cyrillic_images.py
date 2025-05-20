import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from PIL import Image
import io

# List of Cyrillic words in alphabetical order
CYRILLIC_WORDS = [
    'ананас',    # А
    'банан',     # Б
    'вишня',     # В
    'груша',     # Г
    'дом',       # Д
    'еда',       # Е
    'ёлка',      # Ё
    'жираф',     # Ж
    'зонт',      # З
    'игрушка',   # И
    'йогурт',    # Й
    'кот',       # К
    'лимон',     # Л
    'машина',    # М
    'нос',       # Н
    'окно',      # О
    'пёс',       # П
    'роза',      # Р
    'солнце',    # С
    'тигр',      # Т
    'утка',      # У
    'фотоаппарат', # Ф
    'хлеб',      # Х
    'цветок',    # Ц
    'часы',      # Ч
    'шар',       # Ш
    'щука',      # Щ
    'подъезд',   # Ъ
    'мышь',      # Ы
    'дверь',     # Ь
    'эскимо',    # Э
    'юла',       # Ю
    'яблоко'     # Я
]

def download_images():
    # Create output directory if it doesn't exist
    os.makedirs('cyrillic_images', exist_ok=True)
    
    # Cyrillic letters in order
    CYRILLIC_LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    
    for index, word in enumerate(CYRILLIC_WORDS, start=1):
        letter = CYRILLIC_LETTERS[index-1]
        filename = f"{index:02d}-alphabet-{word}.png"
        filepath = os.path.join('cyrillic_images', filename)
        
        # Skip if file already exists
        if os.path.exists(filepath):
            print(f"Skipping {filename} - already exists")
            continue
        try:
            # Search for realistic photos of the word
            search_term = f"{word} фото реалистичное"
            url = f"https://www.google.com/search?q={quote_plus(search_term)}&tbm=isch"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find image results
            img_tags = soup.find_all('img')
            if len(img_tags) > 1:  # Skip first img which is usually Google logo
                for img_tag in img_tags[1:]:  # Try all found images
                    img_url = img_tag.get('src')
                    
                    if not img_url or not img_url.startswith('http'):
                        continue
                        
                    try:
                        img_data = requests.get(img_url, timeout=5).content
                        img = Image.open(io.BytesIO(img_data))
                        width, height = img.size
                        
                        # Skip if too small
                        if width < 100 or height < 100:
                            print(f"Too small ({width}x{height}px), trying next image...")
                            continue
                            
                        # Downscale if needed
                        if width > 150 or height > 150:
                            ratio = min(150/width, 150/height)
                            new_width = int(width * ratio)
                            new_height = int(height * ratio)
                            img = img.resize((new_width, new_height), Image.LANCZOS)
                            print(f"Resized: {width}x{height}px -> {new_width}x{new_height}px")
                        
                        # Use pre-generated filename and path
                        
                        # Save image
                        img.save(filepath, 'PNG')
                        print(f"Saved: {filename} ({img.width}x{img.height}px)")
                        break  # Success - move to next word
                        
                    except Exception as img_error:
                        print(f"Error processing image: {str(img_error)}")
                        continue  # Try next image
                
                else:
                    print(f"Couldn't find suitable image for {word}")
                    
            # Be polite and don't hammer the server
            time.sleep(2)
                    
        except Exception as e:
            print(f"Error processing {word}: {str(e)}")

if __name__ == "__main__":
    download_images()
