#  Water Potability Predictor 💧

This project is a Machine Learning-powered web application that predicts whether a given **water sample is safe (potable)** or **not safe (non-potable)** for drinking.  
It uses a pre-trained Random Forest model and is deployed via an interactive **Streamlit interface**.

---

## 📌 Features

- 🔮 Predicts **Safe** or **Not Safe** water samples  
- 🖥️ Clean, modern UI with **Streamlit**  
- 🧠 Powered by a trained ML model (`.joblib`)  
- 📊 Takes **17+ water quality input features** (pH, TDS, Turbidity, etc.)  
- 🌄 Uses a background image, styled layout, and reference safe range chart  

---

## 📊 Dataset

The dataset used for training the model is available on Kaggle:  
👉 [Water Potability Dataset](https://www.kaggle.com/datasetsvanthanadevi08water-quality-prediction/data)

---


## 🗂️ Project Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit application code |
| `main.ipynb` | Notebook for preprocessing, feature engineering, and model training |
| `final_model.joblib` | Trained Random Forest model pipeline |
| `Screenshot 2025-08-05 205916.png` | Reference safe water range image |

---

⚠️ **Note on Large Files:**  
- The trained model file (`final_model.joblib`, ~431 MB) is **not included** due to GitHub’s file size limits.  
- The raw dataset (`Water_Quality_Prediction.csv`, ~233 MB) is also **not included** for the same reason.  

👉 You can:  
- Download the dataset directly from Kaggle: [Water Potability Dataset](https://www.kaggle.com/datasets/vanthanadevi08/water-quality-prediction/data)  
- Retrain the model using `main.ipynb` and save your own version with:  
  ```python
  import joblib
  joblib.dump(model, "final_model.joblib")

---

## 🧪 Input Features

| Feature Name              | Description |
|----------------------------|-------------|
| pH                        | Acidity/alkalinity of water |
| Iron                      | Iron concentration |
| Nitrate                   | Nitrate concentration |
| Chloride                  | Chloride concentration |
| Lead                      | Lead concentration |
| Zinc                      | Zinc concentration |
| Color                     | Water color (categorical) |
| Turbidity                 | Cloudiness of water |
| Fluoride                  | Fluoride concentration |
| Conductivity              | Electrical conductivity |
| Chlorine                  | Chlorine concentration |
| Manganese                 | Manganese concentration |
| Total Dissolved Solids (TDS) | Dissolved mineral salts |
| Source                    | Water source type (Well, River, Reservoir, etc.) |
| Water Temperature         | Temperature of water sample |
| Air Temperature           | Surrounding air temperature |
| Month                     | Month of observation |
| Day                       | Day of observation |

---

## ⚙️ Model Workflow (from `main.ipynb`)

1. 📥 **Data Loading** – Loaded water quality dataset  
2. 🧹 **Preprocessing** – Removed duplicates, handled missing values, scaled numeric features  
3. 🔄 **Categorical Encoding** – Encoded `Color` and `Source`  
4. ⚖️ **Class Imbalance Handling** – Applied **SMOTE**  
5. 🏗️ **Feature Engineering** – Added time-based and temperature features  
6. 🤖 **Model Training** – Tested multiple models, selected **Random Forest Classifier**  
7. 📊 **Evaluation** – Used accuracy, f1-score, and confusion matrix  
8. 💾 **Model Saving** – Exported final pipeline as `final_model.joblib`  


---

## 🧰 Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend/Model**: Scikit-learn (Random Forest)  
- **Language**: Python   
- **Other Tools**: pandas, numpy, joblib, matplotlib, seaborn  

---

## 👩‍💻 Developed By

This project was **developed by Akshaya Jayakumar**   

---
