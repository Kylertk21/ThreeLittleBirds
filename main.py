import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, 'src', 'app')
os.chdir(app_dir)

sys.path.insert(0, app_dir)

from src.app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))

#MUST be in app dir