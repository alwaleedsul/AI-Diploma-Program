"""
Unit 2 - Example 1: CNN Architecture
الوحدة 2 - مثال 1: هيكل CNN

This example demonstrates:
1. CNN architecture components
2. Convolution and pooling operations
3. Building a simple CNN
"""

print("=" * 60)
print("Example 1: CNN Architecture")
print("مثال 1: هيكل CNN")
print("=" * 60)

# 1. CNN Components
# مكونات CNN
print("\n1. CNN Architecture Components")
print("مكونات هيكل CNN")
print("-" * 60)

cnn_components = """
CNN Architecture:
1. Convolutional Layers - Detect features (edges, shapes)
2. Pooling Layers - Reduce dimensionality (Max, Average)
3. Fully Connected Layers - Classification
4. Activation Functions - ReLU, Softmax

هيكل CNN:
1. طبقات الالتفاف - اكتشاف الميزات (الحواف، الأشكال)
2. طبقات التجميع - تقليل الأبعاد (الحد الأقصى، المتوسط)
3. الطبقات المتصلة بالكامل - التصنيف
4. دوال التنشيط - ReLU، Softmax
"""

print(cnn_components)

# 2. Convolution Operation
# عملية الالتفاف
print("\n" + "=" * 60)
print("2. Convolution Operation")
print("عملية الالتفاف")
print("=" * 60)

def simple_convolution_example():
    """
    Demonstrate convolution concept.
    توضيح مفهوم الالتفاف.
    """
    # Simple 3x3 image
    image = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # 2x2 filter (kernel)
    filter_kernel = [
        [1, 0],
        [0, -1]
    ]
    
    print("\nImage (3x3):")
    for row in image:
        print(f"  {row}")
    
    print("\nFilter (2x2):")
    for row in filter_kernel:
        print(f"  {row}")
    
    # Apply convolution (simplified)
    result = []
    for i in range(len(image) - 1):
        row_result = []
        for j in range(len(image[0]) - 1):
            # Element-wise multiplication and sum
            conv_value = (image[i][j] * filter_kernel[0][0] +
                         image[i][j+1] * filter_kernel[0][1] +
                         image[i+1][j] * filter_kernel[1][0] +
                         image[i+1][j+1] * filter_kernel[1][1])
            row_result.append(conv_value)
        result.append(row_result)
    
    print("\nConvolution Result (2x2):")
    for row in result:
        print(f"  {row}")

simple_convolution_example()

# 3. CNN Architecture Example
# مثال على هيكل CNN
print("\n" + "=" * 60)
print("3. CNN Architecture Example")
print("مثال على هيكل CNN")
print("=" * 60)

cnn_architecture = """
Simple CNN for Image Classification:

Input (28x28x1)  # Grayscale image
    ↓
Conv2D (32 filters, 3x3) + ReLU
    ↓
MaxPooling2D (2x2)
    ↓
Conv2D (64 filters, 3x3) + ReLU
    ↓
MaxPooling2D (2x2)
    ↓
Flatten
    ↓
Dense (128) + ReLU
    ↓
Dense (10) + Softmax  # 10 classes
    ↓
Output (10 classes)
"""

print(cnn_architecture)

# 4. Transfer Learning Concept
# مفهوم التعلم بالنقل
print("\n" + "=" * 60)
print("4. Transfer Learning")
print("التعلم بالنقل")
print("=" * 60)

transfer_learning = """
Transfer Learning Process:
1. Use pre-trained model (e.g., ResNet, VGG)
2. Remove final classification layer
3. Add new layers for your task
4. Fine-tune on your dataset
5. Much faster than training from scratch!

عملية التعلم بالنقل:
1. استخدام نموذج مدرب مسبقاً (مثل ResNet، VGG)
2. إزالة طبقة التصنيف النهائية
3. إضافة طبقات جديدة لمهمتك
4. الضبط الدقيق على مجموعتك
5. أسرع بكثير من التدريب من الصفر!
"""

print(transfer_learning)

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
print("\nNote: For actual implementation, use TensorFlow/Keras or PyTorch")
print("ملاحظة: للتنفيذ الفعلي، استخدم TensorFlow/Keras أو PyTorch")

