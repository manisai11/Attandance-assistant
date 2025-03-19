from flask import Flask,render_template,request,jsonify
from auth import auth  # Import the Blueprint for authentication
from dem import run_fun
import matplotlib.pyplot as plt
global graph_list
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')
def generate_graph(graph_list):
    dates, percentages = zip(*graph_list)
    colors = ["red" if p < 75 else "blue" for p in percentages]

    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(dates, percentages, color=colors, picker=True, s=50)

    step = max(1, len(dates) // 10)  # Show approximately 10 labels
    plt.xticks(dates[::step], rotation=45, fontsize=8)
    plt.yticks(fontsize=10)
    plt.title("Attendance Percentage Progress Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Attendance Percentage (%)", fontsize=12)
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.show()

@app.route('/run-python', methods=['GET'])
def run_python_code():
    curr_pres = int(request.args.get('curr_pres', 75))  
    curr_total = int(request.args.get('curr_total', 109)) 
    start_date=str(request.args.get('start_date'))
    graphclicked=int(request.args.get('graphclicked',0))
    if graphclicked==0:
        result,graph_list= run_fun(curr_pres=curr_pres, curr_total=curr_total,start_date=start_date)
        
    else:
        result,graph_list= run_fun(curr_pres=curr_pres, curr_total=curr_total,start_date=start_date)
        generate_graph(graph_list)
    return jsonify(result)

# Set a secret key for session management
app.secret_key = b'6bde59df5ac94025a9388b3f9d118430'  # Replace with a random secret key

# Register the Blueprint for authentication
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)
