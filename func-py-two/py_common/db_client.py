class DbClient:
    def __init__(self):
        print("DbClient initialized")

    def query(self):
        results = []
        for i in range(10):
            results.append(f"Test result {i+1}")
        return results
