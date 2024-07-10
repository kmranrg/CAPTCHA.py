from PIL import Image, ImageDraw, ImageFont
import random
import string

def generate_text_captcha(text, width=150, height=50):
    # Create an image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Choose a font and size
    font = ImageFont.truetype('arial.ttf', 36)
    
    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((width - text_width) / 2, (height - text_height) / 2)
    
    # Draw the text in the image
    text_color = (0, 0, 0)
    draw.text(text_position, text, fill=text_color, font=font)
    
    return image

def random_string(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_math_captcha(math_problem, width=150, height=50):
    # Create an image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Choose a font and size
    font = ImageFont.truetype('arial.ttf', 36)
    
    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), math_problem, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((width - text_width) / 2, (height - text_height) / 2)
    
    # Draw the text in the image
    text_color = (0, 0, 0)
    draw.text(text_position, math_problem, fill=text_color, font=font)
    
    return image

def random_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return f'{num1} + {num2} = ?', num1 + num2

def generate_captcha(captcha_type='text'):
    if captcha_type == 'text':
        captcha_text = random_string()
        captcha_image = generate_text_captcha(captcha_text)
        return captcha_text, captcha_image
    elif captcha_type == 'math':
        math_problem, answer = random_math_problem()
        captcha_image = generate_math_captcha(math_problem)
        return answer, captcha_image

# Example usage
captcha_type = input("Enter CAPTCHA type ('text' or 'math'): ").strip().lower()
captcha_value, captcha_image = generate_captcha(captcha_type)
captcha_image.show()

print(f'CAPTCHA Value: {captcha_value}')
captcha_image.save('captcha.png')
