from backend.types import UniqueViewsDocument
from typing import List

class MongoDbAdapter():
    def get_client(self):
        # Add your code here to create a mongo db client
        # that can read and write data from github_stats collection
        pass

    def get_data() -> List[UniqueViewsDocument]:
        # Add your code here to read data from github_stats collection
        pass
    
    def store_data(data: List[UniqueViewsDocument]):
        # Add your code here to store data in github_stats collection
        # Save each entry in the data list as a mongodb document
        pass