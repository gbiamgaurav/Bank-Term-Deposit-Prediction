import os
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, RobustScaler, LabelEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from mlproject import logger
from imblearn.over_sampling import RandomOverSampler


class DataTransformation:
    def __init__(self, config):
        self.config = config
        self.preprocessor = None 
        self.transformed_df = None

    def get_data_transformation(self):
        try:
            # Load the dataset
            df = pd.read_csv(self.config.data_path)

            df['contact'] = df['contact'].replace('cellular', 'telephone')
            df['poutcome'] = df['poutcome'].replace('unknown', 'other')

            # Divide the dataset into independent and dependent features
            X = df.drop(columns=["y"], axis=1)
            y = df["y"]

            logger.info("Dividing the dataset into independent and dependent features completed")

            # Create an instance of LabelEncoder
            label_encoder = LabelEncoder()

            # Fit the label encoder to your categorical labels (y) and transform them
            y_encoded = label_encoder.fit_transform(y)

            logger.info("Encoding Target variable completed")

            numeric_features = X.select_dtypes(exclude="object").columns
            categorical_features = X.select_dtypes(include="object").columns

            # Oversample the minority class using RandomOverSampler
            oversampler = RandomOverSampler()
            X_resampled, y_resampled = oversampler.fit_resample(X, y_encoded)

            # Define the pipeline
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", RobustScaler())
                ])

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("ordinalencoder", OrdinalEncoder()),
                ])

            # Define the Preprocessor
            preprocessor = ColumnTransformer(transformers=[
                ("OrdinalEncoder", OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), categorical_features),
                ("RobustScaler", RobustScaler(), numeric_features)
            ], remainder="passthrough")

            self.preprocessor = preprocessor

            # Transform the whole data using the preprocessor
            X_transformed = preprocessor.fit_transform(X_resampled)

            # Get the updated column names after ordinal encoding
            column_names = numeric_features.to_list() + categorical_features.to_list()

            # Combine X_transformed and y back into one Dataframe
            self.transformed_df = pd.DataFrame(X_transformed, columns=column_names)
            self.transformed_df["target"] = y_resampled

            logger.info("Data preprocessing completed")

        except Exception as e:
            raise e

    def save_preprocessor(self):
        if self.preprocessor is not None:
            joblib.dump(self.preprocessor, self.config.preprocessor_path)
            logger.info(f"Preprocessor saved to {self.config.preprocessor_path}")
        else:
            logger.warning("Preprocessor is not available. Please call get_data_transformation to create it.") 

    def train_test_split(self, test_size=0.2, random_state=None):
        if self.preprocessor is None:
            raise ValueError("Preprocessor is not available. Please call get_data_transformation.")

        # Split the data into train and test sets
        train, test = train_test_split(self.transformed_df, test_size=test_size, random_state=random_state)

        # Save the encoded train and test sets in the form of CSV files
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Split the data into train and test sets.")
        logger.info(f"Shape of train data: {train.shape}")
        logger.info(f"Shape of test data: {test.shape}")