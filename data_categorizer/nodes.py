from aineko.core.node import AbstractNode
from typing import Optional
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class DataIngestionNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Connect to the database and fetch data
        # For the purpose of this example, we're using a CSV file as the database
        data = pd.read_csv('database.csv')
        self.producers['raw_data'].produce(data)

class DataCategorizationNode(AbstractNode):
    def _execute(self, params: Optional[dict] = None):
        # Consume the raw data
        raw_data = self.consumers['raw_data'].next()
        # Preprocess the data
        X = raw_data.drop('category', axis=1)
        y = raw_data['category']
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        # Train the model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        # Predict and evaluate
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        # Output the model and accuracy
        self.producers['categorized_data'].produce({'model': model, 'accuracy': accuracy})
