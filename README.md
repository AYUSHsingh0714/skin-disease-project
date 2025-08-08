# skin-disease-project
Deep Learning-Based Skin Disease Prediction Using Convolutional Neural Networks (CNN)
Overview
This project, developed by Ayush Singh and Amishu Negi, addresses the critical challenge of diagnosing skin diseases in underserved areas with limited access to dermatologists. We have created a deep learning model using Convolutional Neural Networks (CNN) for the early detection and diagnosis of common skin diseases. Our goal is to improve public health outcomes by providing an accessible and efficient diagnostic tool.

Project Goals
The primary objective of this project is to develop a deep learning model that predicts skin diseases using CNNs. This model is designed to assist individuals in small towns and villages who lack timely access to dermatologists for diagnosis and treatment. By leveraging technology, we aim to create an accessible tool for early detection and diagnosis, ultimately enhancing public health in underserved regions. The project also includes the establishment of an ecosystem for remote consultations and data-driven diagnostics to provide an inclusive healthcare solution.

Diseases Covered
The model is trained to diagnose four prevalent skin diseases:

Eczema (Atopic Dermatitis): A chronic condition characterized by red, itchy skin, often associated with asthma or hay fever.
Psoriasis: A condition affecting areas like elbows, knees, and the scalp, causing itching, stinging, and a burning sensation.
Herpes (Genital Herpes): Characterized by sores, pain, and itching around the genitals, anus, or mouth, with no known cure.
Melanoma: A type of skin cancer that develops from pigment-controlling cells (melanocytes).
Methodology
The methodology involves several key steps:

Data Collection and Curation: We collected and manually curated a dataset of 1608 images of diseased skin, excluding noisy, low-contrast images. The dataset includes images for Dermatofibroma, Actinic Keratosis, Atopic Dermatitis (Eczema), and Melanoma.

Data Pre-processing: Images were resized to 224x224 pixels, and blurry or noisy images were discarded.

Data Augmentation: To prevent overfitting and increase dataset size, we applied various augmentation techniques, such as:

20% increase in brightness
10% enhancement in contrast
Random 5-degree rotations
Horizontal flipping This process generated five distinct augmented versions for each sample image, resulting in a total of 1608 images in the final dataset.
Model Architecture: We utilized a CNN architecture for image identification and classification, which includes:

Input Layer: Image size of 224x224 pixels with 3 color channels (RGB).
Convolutional Layers: Three layers with 16, 32, and 32 filters, respectively, using a (3,3) kernel size, 'same' padding, and ReLU activation.
Max Pooling Layers: Applied after each convolutional layer with a pool size of (2,2).
Dropout Layers: Regularization technique with dropout rates of 0.3, 0.4, 0.4, and 0.2.
Fully Connected (Dense) Layers: Two dense layers with 4096 neurons and ReLU activation, followed by a final dense output layer with 4 neurons and softmax activation.
Training: The dataset was split with an 80-20 ratio for training and validation. The model was trained for 20 epochs using the Adam optimizer.

Results
The model was tested using 400 separate skin disease images. Utilizing the Inception ResNet-v2 architecture combined with the Adam optimizer, the proposed model achieved:

Training Accuracy: 99.7%
Validation Accuracy: 97.1%
Testing Accuracy: 95.8%
How to Use (Possible Future Implementation)
The project can be implemented through two practical applications for real-time diagnosis and assessment of skin disease severity:

Smartphone-oriented approach: A mobile application where users can upload images of their skin for immediate analysis.
Web server-oriented approach: A web-based platform for remote consultations and diagnostics.
Future Work
This research opens up opportunities for further development, including:

Expanding the dataset to cover more skin diseases.
Integrating the model into a user-friendly application for wider accessibility.
Contributing
We welcome contributions to enhance the model and expand its capabilities. Please feel free to fork the repository and submit pull requests.
