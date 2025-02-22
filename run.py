# run.py
from app import create_app  
import os
app = create_app()  

env = os.getenv("FLASK_ENV", "production")  # Default to production

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
