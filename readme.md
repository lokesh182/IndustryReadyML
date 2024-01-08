# StudentMarksPredictor 🎓📊

Welcome to the StudentMarksPredictor project! This end-to-end machine learning solution is designed to predict students' marks based on various features. Whether you're a developer, data scientist, or educator, this tool empowers you to analyze and predict student performance effectively.

## Overview 🚀

StudentMarksPredictor is structured into well-defined modules, ensuring a seamless workflow from data ingestion to model prediction. The following modules are implemented:

1. **Data Ingestion 📥:** Import and load datasets effortlessly.
2. **Data Transformation 🔄:** Preprocess and clean data to prepare it for model training.
3. **Model Trainer 🧠:** Train a robust machine learning model using the processed data.
4. **Evaluation 📈:** Assess the model's performance using relevant metrics.
5. **Prediction 🎯:** Make predictions on new data with the trained model.

## Getting Started 🛠️

Follow these steps to get started with the StudentMarksPredictor project:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/StudentMarksPredictor.git
   cd StudentMarksPredictor

2. **Install Dependencies:**
    ```bash
   pip install -r requirements.txt

3. **Data Ingestion,Transformation,Model Trainer,Evaluation:**
Provide your dataset in the specified format. Use the data_ingestion.py script for importing data
Here data ingestion.py will do all the work for you i.e(Transformation,Model Trainer,Evaluation) 
delete the artifacts folder then execute app.py.After executing data_ingestion.py artifacts folder get created in artifacts model.pkl and preprocessor.pkl,train and test data is also created,O/P of data_ingestion.py gives you accuracy for best selected model for the project we have also integrated all the pipelines in data ingestion file only ,all you have to only start the data_ingestion then boom! all the work will be done.
 Example:
    ```bash
    python data_ingestion.py

    python app.py #To run flask application locally 


4. **🚀 Deployment on Azure Web App (UI Approach):**
Follow these steps to deploy the Student Marks Predictor as a web app on Azure using the Azure Portal:
- 4.1 create azure account
- 4.2 Sign in to Azure Portal Visit the [Azure Portal](https://portal.azure.com/) and sign in with your Azure account.
- 4.3. Create a New Azure Web App
    -  Navigate to the "Create a resource" page.
    - Search for "Web App" and select "Web App" from the list.
    - Click on the "Create" button.
    - Fill in the required information such as App name, Subscription, Resource Group, and OS.
    - Click "Review + create" and then "Create" to create the web app.
- 4.4  Deploy Your Model
    - Navigate to the "Deployment Center" in the Azure Portal.
    - Choose the deployment method based on your project (e.g., GitHub, Azure DevOps, Local Git).
    -  Configure the deployment settings, including repository and branch information.
- 4.5. Access the Web App URL

    - Once the deployment is complete, navigate to the "Overview" page of your web app.
    - Find the URL under the "URL" section. This is the endpoint where your web app is hosted.

- 4.6. Configure Environment Variables

    - Navigate to the "Configuration" or "Application settings" section in the Azure Portal.
    - Set any required environment variables (e.g., API keys, connection strings) for your application.

- 4.7. Monitor and Troubleshoot

    - Use the Azure Portal to monitor your web app's performance.
    - In case of issues, check the "Logs" or "Diagnose and solve problems" sections for troubleshooting.

 

5. **Conclusion:**
     This project help me to gain knowledge about how industry standards are followed when implementing the realtime machine learning projects , come to know about modular programming which helps to manage the coding neatly and follows clean directory structure 

      Happy coding! 🚀



 


