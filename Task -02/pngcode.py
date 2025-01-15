from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import matplotlib.pyplot as plt

def show_image(img, title="Image"):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def evaluate_expression_from_image(image_path):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return "Error: Image file not found. Please provide a valid image path."
    except Exception as e:
        return f"Error loading image: {e}"

    img = img.convert("L")  
    show_image(img, "Grayscale Image")  

    img = img.filter(ImageFilter.MedianFilter(1))  
    show_image(img, "Median Filtered Image") 

    img = img.resize((img.width * 2, img.height * 2), Image.Resampling.LANCZOS) 
    show_image(img, "Resized Image")  

    img = ImageEnhance.Contrast(img).enhance(3.0)  
    show_image(img, "High Contrast Image")  

    img = img.point(lambda p: p > 180 and 255)  
    show_image(img, "Thresholded Image")  

    img = img.filter(ImageFilter.SHARPEN)  
    show_image(img, "Sharpened Image")  

    try:
        extracted_text = pytesseract.image_to_string(img, config='--psm 6').strip()  
        print(f"Extracted Text: '{extracted_text}'")  
    except Exception as e:
        return f"Error during OCR: {e}"

    if any(op in extracted_text for op in ['+', '-', '*', '/']):
        try:
          
            result = eval(extracted_text)
            return f"The result of the expression is: {result}"
        except Exception as e:
            return f"Error evaluating expression: {e}"
    else:
        return "Error: Extracted text is not a valid arithmetic expression."

image_path = '/home/sanjusri/amFOSS-tasks/Amfoss-tasks./Task -02/arithmetic_expression(1).png'
result = evaluate_expression_from_image(image_path)
print(result)
