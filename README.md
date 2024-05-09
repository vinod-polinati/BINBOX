# Team DEDSEC - Optimal Box Packing with Deep Learning (SusHacks'24 Track Prize Winners)

**Problem Statement:**

Shipping warehouses face the "box problem": identifying the most cost-effective set of boxes to minimize packaging material usage for a vast array of orders, each containing items with varying dimensions and orientations. This project tackles this challenge by harnessing the power of deep learning.

**Solution:**

We present a novel deep learning-based approach that streamlines the box selection process for warehouses, leading to significant cost savings in packaging materials. This is a very rare and unique problem. sOur solution leverages:

* **Synthetic Data Generation:** We create a comprehensive dataset of 100,000 simulated historical orders, accurately reflecting real-world order patterns. This dataset includes:
    * Order ID's
    * Number of items per order
    * Item descriptions
    * Item dimensions (x, y, z)
* **Optimization: Taking advantage of existing ILP, LP solvers by identifying how you should frame the problem:
    * we use PuLP module in python which can help us in using the ILP and LP solvers.

 We also tried it using other approaches
 
* **Deep Learning Model:** We employ a state-of-the-art 3D Convolutional Neural Network (CNN) to effectively capture the spatial relationships between items in different orientations within potential boxes. This model is meticulously trained using the synthetic data to:
    * Analyze order details (number of items, item dimensions)
    * Predict the optimal box configuration, including:
        * Predicted box dimensions (x, y, z)
        * Predicted number of boxes required (if multiple boxes are necessary)

**Winning at SusHacks'24 Wild Card Entry (Aegion Dynamics):**

We are thrilled to announce that our innovative solution, "Team DEDSEC - Optimal Box Packing with Deep Learning," has emerged victorious as the Wild Card Entry winner at SysHacks'24, the prestigious nationwide hackathon, sponsored by Aeon Dynamics! This recognition is a testament to the effectiveness and ingenuity of our approach.

**Key Features and Benefits:**

* **Data-Driven Optimization:** Our deep learning model learns from a massive dataset, enabling it to make increasingly accurate predictions over time.
* **Cost Reduction:** By recommending the most space-efficient box configurations, our solution helps warehouses minimize packaging material usage, leading to substantial cost savings.
* **Scalability and Adaptability:** This approach is designed to handle large datasets of orders efficiently and can be readily adapted to accommodate changing order patterns.

**Getting Started:**

1. **Prerequisites:** Ensure you have Python (3.x) and the necessary deep learning libraries (TensorFlow, PyTorch, etc.) installed on your system.
2. **Clone the Repository:** Use `git clone https://github.com/your-username/optimal-box-packing.git` to clone this repository.
3. **Set Up the Environment:** Create a virtual environment (recommended) and install the required dependencies using `pip install -r requirements.txt`.
4. **Run the final phase notebook file in the guthub 'Final_Phase.ipynb'

**Further Enhancements:**

* Explore alternative deep learning architectures (e.g., Graph Neural Networks) to potentially improve the model's performance.
* Integrate the solution with a warehouse management system for seamless box selection during order processing.
* Implement a continuous learning mechanism to allow the model to adapt to evolving order patterns over time.

**Team DEDSEC:**

We are a team of passionate developers and problem-solvers who are dedicated to creating innovative solutions. Our team members include:

* Sasi - Core ML and DL Developer
* Vinod - ML Developer 
* Rahaman - UI/UX Designer and Data Analyst
* Siddu - Full Stack Developer.

**License:**

This project is licensed under the MIT License (https://opensource.org/license/mit).

We are confident that this comprehensive and well-structured README will effectively showcase your project's merits, celebrate your SUS HACKS'24 victory, and attract the interest of the developer community.
