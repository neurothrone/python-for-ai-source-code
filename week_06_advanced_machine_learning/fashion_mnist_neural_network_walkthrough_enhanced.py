"""Fashion MNIST neural-network walkthrough, enhanced version.

This file uses the same core model as the lecture version.
It adds a few educational improvements:
- Both accuracy and loss plots.
- A mixed sample of correct and incorrect predictions.
- Colored titles to make mistakes easier to notice.
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

# Step 4: Build the model.
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
print(f"Test accuracy: {test_accuracy:.4f}")

# Step 8: Make predictions on the test data.
# Each prediction contains one probability-like score for each class.
predictions = model.predict(test_images, verbose=0)
predicted_label_indices = np.argmax(predictions, axis=1)

# Step 9: Plot both accuracy and loss.
# Accuracy tells us how often the model predicts the correct label.
# Loss tells us how wrong the model's predictions are in a more detailed way.
#
# train_loss:
# - Error on the part of the data used for learning.
#
# val_loss:
# - Error on the validation part of the training data.
# - Helps us see whether the model is still generalizing well.
#
# If training loss keeps improving while validation loss clearly gets worse,
# that can be a warning sign of overfitting.
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(history.history["accuracy"], label="train_accuracy")
axes[0].plot(history.history["val_accuracy"], label="val_accuracy")
axes[0].set_title("Training and Validation Accuracy")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Accuracy")
axes[0].legend()

axes[1].plot(history.history["loss"], label="train_loss")
axes[1].plot(history.history["val_loss"], label="val_loss")
axes[1].set_title("Training and Validation Loss")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Loss")
axes[1].legend()

plt.tight_layout()
plt.show()

# Step 10: Show a random sample of predictions.
# We mix correct and incorrect examples so the output becomes more educational.
rng = np.random.default_rng(42)
incorrect_indices = np.where(predicted_label_indices != test_labels)[0]
correct_indices = np.where(predicted_label_indices == test_labels)[0]

selected_incorrect = rng.choice(
    incorrect_indices,
    size=min(4, len(incorrect_indices)),
    replace=False,
)
selected_correct = rng.choice(
    correct_indices,
    size=12 - len(selected_incorrect),
    replace=False,
)

selected_indices = np.concatenate([selected_incorrect, selected_correct])
rng.shuffle(selected_indices)

plt.figure(figsize=(12, 8))

for plot_position, sample_index in enumerate(selected_indices):
    plt.subplot(3, 4, plot_position + 1)
    plt.imshow(test_images[sample_index], cmap=plt.cm.binary)

    predicted_label_index = predicted_label_indices[sample_index]
    predicted_label = class_names[predicted_label_index]
    true_label = class_names[test_labels[sample_index]]

    title_color = "green" if predicted_label_index == test_labels[sample_index] else "red"
    title_text = f"Pred: {predicted_label}\nTrue: {true_label}"
    plt.title(title_text, fontsize=9, color=title_color)
    plt.axis("off")

plt.tight_layout()
plt.show()

# Step 11: Print a few example confidences.
# Confidence here means the model's highest score for its predicted class.
for index in range(3):
    predicted_label_index = predicted_label_indices[index]
    predicted_label = class_names[predicted_label_index]
    confidence = predictions[index][predicted_label_index]
    true_label = class_names[test_labels[index]]

    print(
        f"Example {index + 1}: predicted '{predicted_label}' "
        f"with confidence {confidence:.3f} | true label: '{true_label}'"
    )
