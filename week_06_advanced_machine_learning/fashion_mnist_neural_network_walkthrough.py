"""Fashion MNIST neural-network walkthrough.

This is the original lecture version.
It stays close to the code built step by step during class.
"""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# Step 1: Load the dataset.
# Fashion MNIST contains labeled images of clothing items.
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Step 2: Add readable class names for the numeric labels.
class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

# Step 3: Prepare the data.
# Pixel values go from 0 to 255.
# Dividing by 255.0 normalizes them to a 0 to 1 range.
train_images = train_images / 255.0
test_images = test_images / 255.0

# Step 4: Build a small neural network.
# Sequential builds the model as a simple stack of layers.
# Flatten reshapes each 28x28 image into one long vector.
# Dense(128, activation="relu") is the hidden layer.
# Dense(10, activation="softmax") gives one score per class.
model = tf.keras.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28), name="flatten_input"),
        tf.keras.layers.Dense(128, activation="relu", name="hidden_layer_1"),
        tf.keras.layers.Dense(10, activation="softmax", name="output_layer"),
    ],
    name="fashion_mnist_classifier",
)

# Step 5: Compile the model.
# Adam is a common optimizer.
# sparse_categorical_crossentropy fits integer labels like 0 to 9.
# accuracy is included as an easy-to-read metric.
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

# Step 6: Train the model.
# epochs=5 means the model sees the training data five times.
# validation_split=0.1 uses 10% of the training data for validation.
history = model.fit(
    train_images,
    train_labels,
    epochs=5,
    validation_split=0.1,
    verbose=1,
)

# Step 7: Evaluate the model on test data.
# This checks how the model performs on unseen data.
test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose=0)
print(f"\nTest loss: {test_loss:.4f}")
print(f"Test accuracy: {test_accuracy:.4f}\n")

# Step 8: Make predictions on the test data.
# Each prediction contains one probability-like score for each class.
predictions = model.predict(test_images, verbose=0)

# Step 9: Show a simple training-history plot.
# Compare training accuracy and validation accuracy over time.
plt.figure(figsize=(8, 4))
plt.plot(history.history["accuracy"], label="train_accuracy")
plt.plot(history.history["val_accuracy"], label="val_accuracy")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.show()

# Step 10: Show some prediction examples.
plt.figure(figsize=(12, 8))

# Show 12 example images in a 3 x 4 grid.
for index in range(12):
    plt.subplot(3, 4, index + 1)
    plt.imshow(test_images[index], cmap=plt.cm.binary)

    # np.argmax(...) returns the index of the largest value.
    predicted_label_index = np.argmax(predictions[index])
    predicted_label = class_names[predicted_label_index]
    true_label = class_names[test_labels[index]]

    title_text = f"Pred: {predicted_label}\nTrue: {true_label}"
    plt.title(title_text, fontsize=9)
    plt.axis("off")

plt.tight_layout()
plt.show()

# Step 11: Print a few example confidences.
# Confidence here means the model's highest score for its predicted class.
for index in range(3):
    predicted_label_index = np.argmax(predictions[index])
    predicted_label = class_names[predicted_label_index]
    confidence = predictions[index][predicted_label_index]
    true_label = class_names[test_labels[index]]

    print(
        f"Example {index + 1}: predicted '{predicted_label}' "
        f"with confidence {confidence:.3f} | true label: '{true_label}'"
    )
