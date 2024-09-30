import openai
from PIL import Image, ImageDraw, ImageFont

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_meme_caption(user_text):
    prompt = f"Create a reaction meme caption based on the text: {user_text}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # or GPT-4
        prompt=prompt,
        max_tokens=50
    )
    meme_caption = response['choices'][0]['text'].strip()
    return meme_caption

def create_meme_image(base_image_path, meme_caption, output_image_path):
    image = Image.open(base_image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # Use a default font
    
    # Position and style
    text_position = (10, image.height - 50)
    text_color = (255, 255, 255)
    
    # Add the text
    draw.text(text_position, meme_caption, font=font, fill=text_color)
    
    # Save the image
    image.save(output_image_path)
    print(f"Meme saved as {output_image_path}")

# Example workflow
user_text = "When the code works without any errors!"
meme_caption = generate_meme_caption(user_text)
base_image_path = 'meme_template.jpg'
output_image_path = 'reaction_meme.jpg'
create_meme_image(base_image_path, meme_caption, output_image_path)
