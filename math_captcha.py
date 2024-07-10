from PIL import Image, ImageDraw, ImageFont
import random

def generate_math_captcha(math_problem, width=150, height=50, font_path='Anurag-Regular.ttf'):
    # Create an image with white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    
    # Choose a handwritten font and size
    try:
        font = ImageFont.truetype(font_path, 37)
    except OSError:
        print(f"Error: Cannot open font resource {font_path}. Using default font.")
        font = ImageFont.load_default()
    
    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), math_problem, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((width - text_width) / 2, (height - text_height) / 2)
    
    # Draw the text in the image
    text_color = (0, 0, 0)
    draw.text(text_position, math_problem, fill=text_color, font=font)
    
    # Add noise to the background
    noise_level = 300  # Adjust noise level higher for more noise
    for _ in range(noise_level):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    # Create a semi-transparent overlay
    overlay = Image.new('RGBA', image.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle([(0, 0), image.size], fill=(0, 0, 0, 100))  # Adjust alpha (4th element) for opacity
    
    # Combine the image and overlay
    image = Image.alpha_composite(image.convert('RGBA'), overlay)
    
    return image.convert('RGB')

def random_math_problem():
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    problem = f'{num1} {operator} {num2} = ?'
    
    return problem, answer

def generate_captcha():
    math_problem, answer = random_math_problem()
    captcha_image = generate_math_captcha(math_problem)
    return answer, captcha_image

# Example usage
captcha_value, captcha_image = generate_captcha()
captcha_image.show()

print(f'CAPTCHA Value: {captcha_value}')
captcha_image.save('captcha.png')
