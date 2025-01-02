from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

def evaluate_expression_from_image(image_path):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return "Error: Image file not found. Please provide a valid image path."
    except Exception as e:
        return f"Error loading image: {e}"
    img = img.convert("L")  # Convert to grayscale
    img = img.filter(ImageFilter.MedianFilter(3))  # Apply a median filter (helps reduce noise)
    img = img.resize((img.width * 2, img.height * 2))  # Increase the image size by a factor of 2
    img = ImageEnhance.Contrast(img).enhance(3.0)  # Increase contrast
    img = img.point(lambda p: p > 150 and 255)  # Adjust threshold to improve clarity

    try:
        extracted_text = pytesseract.image_to_string(img, config='--psm 6').strip()  
        print(f"Extracted Text: '{extracted_text}'")  # Debugging: print the raw text
    except Exception as e:
        return f"Error during OCR: {e}"
    if any(op in extracted_text for op in ['+', '-', '*', '/']):
        try:
            # Try to evaluate the extracted arithmetic expression
            result = eval(extracted_text)
            return f"The result of the expression is: {result}"
        except Exception as e:
            return f"Error evaluating expression: {e}"
    else:
        return "Error: Extracted text is not a valid arithmetic expression."

image_path = '/home/sanjusri/amFOSS-tasks/Amfoss-tasks./Task -02/arithmetic_expression(1).png'
result = evaluate_expression_from_image(image_path)
print(result)


